# Commands & procedures

LAN: laptop at `192.168.29.229`. Arch user `samurai`, Windows user `visalakshi`, password `<REDACTED-PASSWORD>` (this machine).

## Passwordless SSH automation

Both OSes run OpenSSH. Arch's `sshd` and Windows' `OpenSSH_for_Windows` listen on port 22 (whichever OS is booted answers). An askpass helper feeds the password so commands run non-interactively.

```bash
# /tmp/ap.sh  (chmod +x)
#!/bin/bash
echo '<REDACTED-PASSWORD>'
```

```bash
# Run a command over SSH without a password prompt
SSH_ASKPASS=/tmp/ap.sh SSH_ASKPASS_REQUIRE=force \
  ssh -o NumberOfPasswordPrompts=1 -o ConnectTimeout=12 \
      -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
      samurai@192.168.29.229 '<command>'
```

- `StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null` avoids "host key verification failed" when the same IP answers with the Arch key one boot and the Windows key the next.
- Arch: `samurai@`, default shell bash/zsh. Windows: `visalakshi@`, default shell `cmd.exe` (run PowerShell with `powershell -NoProfile -Command "..."`).
- On Arch, non-login shells lack PATH; prefix: `export PATH=/usr/sbin:/usr/bin:/sbin:/bin;`.
- For `sudo`: `echo <REDACTED-PASSWORD> | sudo -S <cmd>`.

## Memory diagnostics (Arch)

```bash
free -h                                   # usable RAM
sudo dmidecode -t memory | grep -E "Size:|Speed:|Configured|Part Number|Locator"
sudo dmesg | grep -E "BIOS-e820" | grep -iE "usable|reserved"   # firmware memory map
cat /proc/cmdline                         # active kernel params
```

## Smokeless_UMAF (the AMD hidden-settings form browser)

Repo: `DavidS95/Smokeless_UMAF` (ships as `UMAF_BETA.zip`). It unregisters the BIOS FormBrowser and loads its own, exposing AMD CBS/PBS and the suppressed Acer rows.

```bash
# Stage on the ESP (modules at root + loader in a folder)
curl -sL -o umaf.zip https://github.com/DavidS95/Smokeless_UMAF/raw/main/UMAF_BETA.zip
mkdir umaf && cd umaf && unzip -o ../umaf.zip
sudo cp Loader.efi SetupBrowser.efi DisplayEngine.efi UiApp.efi SuppressIFPatcher.efi SREP_Config.cfg /boot/efi/
sudo mkdir -p /boot/efi/EFI/UMAF
sudo cp EFI/Boot/BOOTX64.efi /boot/efi/EFI/UMAF/
sudo cp Loader.efi SetupBrowser.efi DisplayEngine.efi UiApp.efi SuppressIFPatcher.efi SREP_Config.cfg /boot/efi/EFI/UMAF/

# Boot entry (this Acer firmware reshuffles order, so force it with BootNext each time)
sudo efibootmgr -c -d /dev/sda -p 3 -L "Smokeless UMAF" -l "\EFI\UMAF\BOOTX64.efi"
sudo efibootmgr -n 0000      # BootNext = the entry number it printed
sudo reboot
```

Navigation inside UMAF: Device Manager → AMD CBS → submenu. Arrows move, Enter opens, Esc backs out (Esc at top = exit), **F10** saves, **F9** resets to defaults.

- UMA frame buffer: NBIO Common Options → GFX Configuration → set Integrated Graphics Controller = **Forces**, UMA Mode = **UMA_SPECIFIED**, UMA Frame buffer Size = **128M**.
- Fast Boot: the Acer **Main** page → **Fast Boot = Disabled**.
- Memory interleaving: DF Common Options → Memory interleaving (None/Channel/Die/Socket — Channel/Die/Socket are ignored on unsupported populations).

## UEFI shell (EDK2) — reading protected variables

```bash
# Stage the shell on the ESP (Arch)
sudo pacman -S --needed edk2-shell
sudo mkdir -p /boot/efi/EFI/SHELL
sudo cp /usr/share/edk2-shell/x64/Shell_Full.efi /boot/efi/EFI/SHELL/shellx64.efi
sudo efibootmgr -c -d /dev/sda -p 3 -L "UEFI Shell" -l "\EFI\SHELL\shellx64.efi"
sudo efibootmgr -n 000A && sudo reboot
```

In the shell (`map -r` lists filesystems; `fs1:` is the Arch ESP on this box):
```
fs1:
dmpstore -guid A04A27F4-DF00-4D42-B552-39511302113D            # list Acer vars (Setup, Custom)
dmpstore -guid A04A27F4-DF00-4D42-B552-39511302113D -s sysconf.bin   # save them to a file
memmap                                                          # firmware memory map + Total Memory
smbiosview -t 17 > smbios17.txt                                 # per-DIMM tables
dmpstore -all -l sysconf_patched.bin                           # load vars back (FAILS on Setup: Write Protected)
reset
```

> The `Setup` variable is write-protected: `dmpstore -l` loads it but the firmware rejects the write. Reading/saving works; writing does not.

## Patch a dmpstore variable file (host side)

`scripts/patch_dmpstore.py` reads a `dmpstore -s` file, flips a byte in a named variable, and fixes the CRC32:
```bash
python -I scripts/patch_dmpstore.py sysconf.bin sysconf_patched.bin   # flips Setup[0x24E]=1 (logo)
```
(Edit `target_name` / `patches` in the script for other bytes.)

## Decode the full BIOS settings (host side)

```bash
# On a machine with the BIOS image extracted:
uefiextract FH50P.bin            # extract the BIOS image
ifrextractor <Setup PE32 body> all   # -> ifr_all.txt
# Then dedupe into a readable reference:
grep -aE 'Form FormId: 0x[0-9A-Fa-f]+, Title:|OneOf Prompt:|OneOfOption Option:|CheckBox Prompt:|Numeric Prompt:' ifr_all.txt > ifr_raw.txt
python -I scripts/parse_ifr.py ifr_raw.txt BIOS_SETTINGS_FULL.md
```

## Fix: Windows won't boot after firmware changes (stale hibernation)

From Arch, with Windows on `nvme0n1p3`:
```bash
sudo mkdir -p /mnt/win
sudo ntfsfix -n /dev/nvme0n1p3                      # check (no-action) — should be clean
sudo mount -t ntfs3 -o rw /dev/nvme0n1p3 /mnt/win
sudo mv /mnt/win/hiberfil.sys /mnt/win/hiberfil.sys.bak   # discard stale resume (reversible)
sudo sync && sudo umount /mnt/win
```
Then boot Windows (cold boot) and disable Fast Startup permanently:
```powershell
powercfg /h off
```

## Fix: Arch black screen on boot (needed nomodeset every time)

```bash
# Repoint the boot display-manager from the broken plymouth unit to plain sddm
echo <REDACTED-PASSWORD> | sudo -S systemctl disable sddm-plymouth
echo <REDACTED-PASSWORD> | sudo -S systemctl enable --force sddm

# Clean experiment leftovers out of the kernel cmdline
sudo cp /etc/default/grub /etc/default/grub.bak
sudo sed -i -E "s/ ?mem=15G//g; s/ ?amd\.gpu\.gtsize=512//g; s/ ?splash//g; s/ ?quiet//g" /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

One-time recovery (at the GRUB menu, if a boot ever black-screens): highlight the entry, press `e`, go to the `linux` line (Ctrl+E for end), append ` nomodeset 3`, Ctrl+X to boot to a text console.

## CMOS reset (last-resort firmware recovery)

If a firmware write stops the machine POSTing: power-cycle 2–5× (Fail_CNT = 5 auto-reverts memory settings). Else open the bottom panel, disconnect the main battery, unplug the coin-cell RTC lead (red/black twisted wires under the battery, right side), hold power 30 s, reconnect. Resets **all** settings to defaults.
