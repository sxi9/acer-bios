# Windows won't boot — `0xc0000001` — offline diagnosis & repair

The definitive write-up of the Windows 11 boot failure on the Acer Nitro 5 AN515-43 and
exactly how it was fixed **without losing the profile, apps, cookies or any data**.

> **Root cause:** a corrupted / mismatched **boot configuration** on the NVMe EFI System
> Partition (ESP) — the Windows Boot Manager (`bootmgfw.efi`) on the ESP was a *different build*
> than the installed OS loader (`winload.efi`), and the BCD had accumulated bad offline edits.
> **Fix:** rebuild the whole boot config with **`bcdboot`** from Hiren's WinPE.
> Everything else (registry, drivers, disk mode, partitions) turned out to be fine.

---

## Symptom

- Boot via GRUB → **Windows Boot Manager** → blue recovery screen, **error code `0xc0000001`**.
- Persisted through every OS-level repair attempt (safe mode, driver disable, firmware reset).
- **No minidumps**, **no `SrtTrail.txt`** → Windows never reached the kernel. This is a pure
  **boot-loader (bootmgr/winload) failure**, not a kernel bugcheck. (Earlier graphics stop codes
  like `REFERENCE_BY_POINTER` were a red herring from a different, earlier state.)

`0xc0000001` from the Windows Boot Manager = *"a required device/file could not be accessed or
loaded"* — i.e. the boot chain itself, not the OS.

## What was ruled out (all verified correct, offline from Arch over SSH)

| Checked | Result |
|---|---|
| Right partition? | ✅ `nvme0n1p3` ("Acer") has `\Windows` + all profiles (`visalakshi`, `sai787`, …). The `sda2` Windows is an **empty stub** on the Arch SSD — ignore it. |
| Boot files present? | ✅ `bootmgfw.efi`, `winload.efi` both present |
| SYSTEM hive corrupt? | ✅ No — header magic `regf`, **primary seq == secondary seq** (clean, not dirty) |
| BCD readable / correct? | ✅ Loader path `\Windows\system32\winload.efi`; `device` == `osdevice` |
| BCD points to right disk? | ✅ BCD partition GUID `5fbb6293-2971-4c7e-b07d-813f998d90f4` == actual `nvme0n1p3` PARTUUID |
| Disk controller mode | ✅ BIOS **SATA Mode = AHCI** (not RAID) |
| Boot-start driver missing? | ❌ inconclusive — `ntfs3` mounts are **case-sensitive**, so offline `test -f` gives false "missing" for core drivers. Don't trust that check. |

## The actual cause — boot-manager / OS-loader version mismatch

Comparing the ESP's boot manager against the OS's own pristine copy:

| File | Size | Date | md5 |
|---|---|---|---|
| ESP `\EFI\Microsoft\Boot\bootmgfw.efi` (what boots) | **2.85 MB** | **Mar 2026** | `5a2a56ec…` |
| OS `C:\Windows\Boot\EFI\bootmgfw.efi` (pristine) | 1.70 MB | Nov 2025 | `ef471261…` |
| OS `C:\Windows\System32\winload.efi` (what loads) | 2.04 MB | Nov 2025 | `1135201e…` |

A **Mar-2026 boot manager trying to load a Nov-2025 Windows** (different build *and* size) is a
textbook `0xc0000001`. Likely cause: an earlier `DISM /revertpendingactions` rolled the OS back to
Nov 2025, but the ESP's boot manager stayed on the newer build. Plus the BCD had accumulated bad
offline edits over the session.

Swapping just `bootmgfw.efi` to the matching copy was **not enough** — the real fix is a full
rebuild.

## The fix — `bcdboot` from Hiren's WinPE  (keeps everything)

Booted **Hiren's BootCD PE** (already on the `/iso` partition, chainloaded via GRUB → *ISO Boot
Manager* → `grubfm` → `HBCD_PE_x64.iso`). In its Command Prompt:

```bat
rem 1. find the drives
diskpart
  list vol
  rem  Volume 2  C:  Acer        NTFS  240 GB   <- Windows
  rem  Volume 4      (no letter)  FAT32 100 MB   <- NVMe ESP  (NOT the 600 MB Arch ESP!)
  select volume 4
  assign letter=s
  exit

rem 2. rebuild ALL boot files + a fresh BCD matched to the OS  (THE FIX)
bcdboot C:\Windows /s S: /f UEFI
rem -> "Boot files successfully created."

rem 3. (optional, for OS file / FS health)
chkdsk C: /f
sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows
```

Reboot → GRUB → **Windows Boot Manager** → **desktop**. `bcdboot` alone cleared `0xc0000001`;
`chkdsk`/`sfc` were not even needed. **Profile, apps, cookies, files — all intact.**

> `bcdboot` is the single highest-value fix for `0xc0000001` when the files exist but boot fails:
> it regenerates `bootmgfw.efi` + the full BCD on the ESP, matched to `C:\Windows`, discarding
> every accumulated bad edit. GRUB still chainloads the regenerated `bootmgfw.efi`, so the dual
> boot menu keeps working.

## Post-boot — re-enable the AMD graphics driver

During diagnosis the AMD display driver had been disabled offline (set `Start=4`) to test a
graphics theory. Windows booted on the Microsoft Basic Display Adapter (low res). Re-enabled it
**over SSH into the now-booted Windows** (see below), then rebooted for full resolution + dGPU:

```bat
reg add "HKLM\SYSTEM\CurrentControlSet\Services\amdkmdag" /v Start /t REG_DWORD /d 3 /f
reg add "HKLM\SYSTEM\CurrentControlSet\Services\amdwddmg" /v Start /t REG_DWORD /d 3 /f
```
(`Start=3` = demand-start, the stock value. Verify with `reg query … /v Start` → `0x3`.)

If the AMD driver ever misbehaves after this: **DDU + fresh AMD driver** from inside Windows.

---

## Remote access to this laptop (both OSes share one IP)

The laptop answers on **`192.168.29.229`** in *both* OSes (same DHCP lease), but with different
SSH servers depending on which is booted:

| Booted OS | SSH user | Notes |
|---|---|---|
| **Archcraft** | `samurai@192.168.29.229` | Linux OpenSSH; `sudo` password below; used for all offline NTFS/registry work |
| **Windows 11** | `visalakshi@192.168.29.229` | `OpenSSH_for_Windows_9.5`; SSH session runs **elevated** (High Mandatory Level, Administrators) — `reg add` to `HKLM` works directly |

Password for both: the project standard (`<REDACTED-PASSWORD>`).

### Driving SSH from a Windows box (no `sshpass` / `setsid` / `plink`)

Git-Bash on Windows can't do non-interactive password SSH the usual way. Use **paramiko via
`uv`** — reads the remote command from stdin:

```python
# lssh.py  — run: echo '<remote cmd>' | uv run --with paramiko python lssh.py
import sys, os, paramiko
c = paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(os.environ["LHOST"], 22, os.environ.get("LUSER","visalakshi"),
          os.environ.get("LPASS"), timeout=12, allow_agent=False, look_for_keys=False)
i,o,e = c.exec_command(sys.stdin.read())
sys.stdout.write(o.read().decode("replace"))
if e.read(): sys.stdout.write("\n--STDERR--\n")
```
```bash
export LHOST=192.168.29.229 LUSER=samurai LPASS=<REDACTED-PASSWORD>
echo 'command here' | uv run --quiet --with paramiko python lssh.py
```

Gotchas:
- The remote **non-login shell has no PATH** — prepend
  `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin` on Arch.
- For `sudo`, pipe the password: `echo <pw> | sudo -S <cmd>`.
- On Windows OpenSSH the default shell is **cmd** — chain commands with `&`, not newlines
  (a single `exec_command` string runs only the first line otherwise).

### Useful offline-from-Arch commands

```bash
# mount Windows C: (NVMe) and the ESP
sudo mount -t ntfs3 -o ro /dev/nvme0n1p3 /mnt       # Windows  (rw to edit)
sudo mount -t vfat  -o rw /dev/nvme0n1p1 /mnt2      # NVMe ESP

# read/compare boot files
md5sum /mnt2/EFI/Microsoft/Boot/bootmgfw.efi /mnt/Windows/Boot/EFI/bootmgfw.efi

# which partition holds Windows + profiles
for p in nvme0n1p3 nvme0n1p5 sda2; do sudo mount -t ntfs3 -o ro /dev/$p /mnt3 2>/dev/null; \
  [ -d /mnt3/Windows/System32 ] && { echo "$p:"; ls /mnt3/Users; }; sudo umount /mnt3; done

# SYSTEM hive clean check (primary seq @0x4 must equal secondary @0x8)
sudo dd if=/mnt/Windows/System32/config/SYSTEM bs=1 count=16 2>/dev/null | od -A x -t x1

# read/write offline registry (BCD is a hive too)
sudo hivexget /mnt/Windows/System32/config/SYSTEM '\ControlSet001\Services\amdkmdag' Start
echo -e 'cd \\ControlSet001\\Services\\amdkmdag\nsetval 1\nStart\nhex:4:04,00,00,00\ncommit\nquit' \
  | sudo hivexsh -w /mnt/Windows/System32/config/SYSTEM     # DWORD value = hex:4:<LE bytes>
```

## Partition map (for reference)

| Device | Size | FS | What |
|---|---|---|---|
| `nvme0n1p1` | 100 MB | FAT32 | **Windows ESP** (bcdboot target) |
| `nvme0n1p2` | 16 MB | — | MSR |
| `nvme0n1p3` | 240 GB | NTFS | **Windows C:** ("Acer") + all profiles |
| `nvme0n1p4` | 1 GB | NTFS | Recovery (`winre.wim` missing) |
| `nvme0n1p5` | 224 GB | NTFS | "New Volume" (data) |
| `sda2` | 465 GB | NTFS | "ssd" data; also an empty stub `\Windows` |
| `sda3` | 600 MB | FAT32 | **Arch ESP / GRUB** (do not touch for Windows) |
| `sda5` | — | ext4 | Archcraft root |

## Lessons

1. **`0xc0000001` is a boot-chain failure, not a driver crash.** No minidump / no `SrtTrail`
   confirms Windows never reached the kernel — stop chasing graphics drivers.
2. When every offline component checks out but it still won't boot, **rebuild the boot config with
   `bcdboot`** rather than editing the BCD by hand. It fixes `bootmgfw`/`winload` mismatches and
   bad BCD entries in one step, and keeps 100% of the install.
3. **`ntfs3` is case-sensitive** — offline "missing file" checks against a Windows volume produce
   false positives; don't rely on them.
4. A **reinstall/clean install cannot keep installed apps** — only an in-place repair upgrade does,
   and that needs a *booting* Windows. So repairing the boot is almost always worth trying first.
5. Keep a CMOS-reset path and don't over-edit the BCD offline; cumulative hand edits were part of
   what got the boot into this state.
