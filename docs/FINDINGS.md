# Findings

## 1. The usable-RAM cap (16 GB installed, ~7.6 GB usable)

### Symptom
16 GB installed, but Windows/Linux saw only ~6 GB (later ~7.6 GB after tuning). The rest showed as "hardware reserved".

### Root cause
The two SODIMMs are **mismatched** (generic DDR4-2667 + Micron DDR4-3200). The firmware trains both to a common 2400 MT/s but then **falls back to mapping only about one stick's worth** of capacity into the physical address space. This is an AGESA memory-init decision, not an OS or kernel issue.

### Proven three independent ways (all firmware-level)

1. **Kernel e820 (the firmware-provided map):** usable RAM ends at `0x266ffffff`, with a reserved tail to `0x26effffff` (~10.5 GB) and **nothing mapped above that**. ~5.5 GB of the second stick never appears in the address space.
2. **SMBIOS type-17:** both DIMMs detected, 8 GB each, trained to 2400 MT/s at 1.20 V. Not a dead stick — the firmware sees both.
3. **UEFI shell `memmap` total:** `Total Memory = 8,021 MB (8,411,344,896 bytes)`, Available = 8,314,200,064 bytes (~7.74 GiB → OS reports ~7.6 GB). The firmware **counts only ~8 GB total** — about one stick. It does not see 16 GB and withhold half; the second stick's capacity is simply never counted.

### What was tried and failed
- `efivarfs` writes to `AmdSetup` (UMA mode, interleaving): persisted but AGESA ignored them.
- `memmap=` kernel parameters: region undecodable → hang.
- `Memory interleaving = None` (Data Fabric, via Smokeless_UMAF): applied, **no change**.
- Manual `Memory Clock Speed = 1067 MHz (DDR4-2133)` via Smokeless_UMAF: **3 beeps, no POST** (Fail_CNT auto-recovered, which also reset the UMA win).

### What worked
- **iGPU UMA Frame buffer Size → 128M** (Smokeless_UMAF → AMD CBS → NBIO → GFX Configuration). Freed ~1.5–2 GB. Took through the firmware's own setup engine (unlike efivar writes). Survived the Fail_CNT reset.
- Result: usable RAM **5.7 GB → 7.6 GB**.

### Conclusion
No firmware setting recovers memory the firmware never maps. The remaining ~8 GB needs a **matched kit** (2 × 8 GB DDR4-3200, or a single 16 GB SODIMM). A matched kit giving 16 GB confirms the mismatch; a matched kit still capped would indicate a slot/board hardware fault (cheap pre-check: one stick alone in the second slot should give full ~8 GB).

## 2. The boot hang (stuck on logo, must enter BIOS then restart)

- **Cause:** firmware **Fast Boot** was enabled (`Setup` byte `0x22E = 1`). Fast Boot skips full memory training on cold boot and reuses a saved training result, which is unreliable on the mismatched pair. A bad reuse stalls at the logo; entering BIOS forces a full retrain, so the next boot works.
- `Cmd2T = 2T` (looser command timing) did **not** fix it — confirms it's the training path, not timing margin.
- **Fix:** disable Fast Boot (visible in F2 BIOS, Main tab; or Smokeless_UMAF Main page). Forces a full memory train every boot — slightly slower POST, reliable boot.

## 3. The Acer boot logo (cannot change on this model)

- Firmware has the feature: `Setup` offset `0x24E` "Customize POST animation" — put `AcerLogo.gif`/`.jpg` (≤ panel resolution, 1920×1080) on a FAT32 USB root, enable the flag.
- The menu row is **hidden** (`SuppressIf True`), so it is not in the F2 BIOS.
- The `Setup` varstore is **OS-write-protected**: `dmpstore -l` from the UEFI shell returns "Failed to set variable Setup: Write Protected"; `setup_var.efi` returns error 0x8.
- NitroSense on this Nitro has only a generic "Personalize" section — **no** boot-logo feature (that is a Predator feature; no `AcerLogo`/`BootLogo`/`POST Animation` strings in the app).
- The only runtime bypass is **Insyde H2OUVE** (writes `Setup` via an SMM/SMI channel). Not pursued — it means running an unsigned OEM firmware tool from a modding forum on the main OS for a cosmetic change, with an uncertain payoff (unknown whether the Nitro firmware even loads the GIF).
- Guaranteed-but-brick-risk alternative: edit the logo module in the BIOS image and reflash the SPI chip. Not pursued.

## 4. Windows won't boot — BSOD `REFERENCE_BY_POINTER` (0x18), even safe mode

- **On-screen stop code:** `REFERENCE_BY_POINTER` (bugcheck 0x18) — a **driver fault** (a kernel object's reference count is wrong). Not a profile, hive, disk, or update problem.
- **Trigger:** the firmware **GPU change** — Integrated Graphics Controller set to **Forces** + UMA dropped to **128M** via Smokeless_UMAF. The installed Windows AMD display driver was configured against the original GPU topology; at boot it now sees a different one and mis-references a GPU object → 0x18, before Windows can write a dump.
- **Ruled out by offline checks (all healthy):** profile `visalakshi` intact (NTUSER.DAT 46 MB, UsrClass.dat present); C: had 12 GB free; **no `pending.xml`** (not an interrupted update); SYSTEM (29 MB) / SOFTWARE (181 MB) hives normal; `ntfsfix -n` clean; `C:\Windows\Minidump` empty and no event-log entry (Windows never boots far enough to log the crash — the code exists only on screen). `RegBack` is empty (Windows 11 default), so no offline registry restore.
- **Red herring:** Windows **Fast Startup** `hiberfil.sys` (3.3 GB) was present from the last normal shutdown. Renaming it from Linux (`mv hiberfil.sys hiberfil.sys.bak`) did **not** fix the boot — confirming the cause was the driver/firmware fault, not a stale resume.
- **Fix:** revert the GPU change in Smokeless_UMAF — **AMD CBS → NBIO → GFX Configuration → Integrated Graphics Controller → `Auto`** (returns UMA to automatic), F10. This restores the GPU topology the Windows driver expects. Costs the 128M UMA RAM win.
- **If it still BSODs after the GPU revert:** a driver damaged by the repeated hard power-offs — recover via **WinRE → System Restore** to a point before the changes.
- **Lesson:** do not leave the iGPU forced / UMA shrunk on a dual-boot machine whose Windows AMD driver was installed against the default topology; and run `powercfg /h off` in Windows so Fast Startup can't clash with firmware changes.

## 5. The Arch black-screen (needed `nomodeset 3` every boot)

- **Cause:** the boot display-manager symlink `display-manager.service` pointed to **`sddm-plymouth.service`** (broken), so no GUI started — just the framebuffer cursor. amdgpu itself was fine (`[drm] Initialized amdgpu`, fb0 primary).
- Also, GRUB carried leftovers: `mem=15G` (RAM cap), a typo'd `amd.gpu.gtsize=512`, and `splash` (plymouth, blanking the screen pre-login).
- **Fix:** `systemctl disable sddm-plymouth`, `systemctl enable --force sddm` (repoints `display-manager.service` to plain `sddm`), and clean `GRUB_CMDLINE_LINUX_DEFAULT` (drop `quiet splash mem=15G amd.gpu.gtsize=512`), then `grub-mkconfig`. Boots straight to the Archcraft desktop, no `nomodeset`.
