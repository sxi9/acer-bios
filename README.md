# Acer Nitro 5 AN515-43 — BIOS / firmware deep-dive

Everything learned while recovering, diagnosing and tuning an **Acer Nitro 5 AN515-43** at the firmware level: hidden BIOS settings, the usable-RAM cap, boot hangs, the Linux desktop, a Windows boot failure, and the limits of what Insyde/Acer firmware lets you change.

## The machine

| | |
|---|---|
| Model | Acer Nitro 5 AN515-43 |
| APU | AMD Ryzen 5 3550H (Picasso / Raven2, FP5) |
| iGPU | Radeon Vega 8 (UMA from system RAM) |
| dGPU | Radeon RX 560X (4 GB GDDR5, separate) |
| BIOS | Insyde H2O, Acer **V1.12** (FH50P, AMD AGESA PicassoPI-FP5 1.0.0.B) |
| RAM | 2 × 8 GB DDR4 SODIMM, **mismatched**: generic 2667 (`CB8GS2666.C8JT`) + Micron 3200 (`8ATF1G64HZ-3G2J1`), both trained to 2400 |
| Storage | Crucial BX500 1 TB SATA SSD (Archcraft Linux) + Kingston NVMe (Windows 11 Home) |
| Dual boot | Windows 11 on NVMe (`nvme0n1`), Archcraft on SATA SSD (`sda`) |

## TL;DR outcomes

| Issue | Status | Fix |
|---|---|---|
| Only ~6 GB of 16 GB usable | **Partly recovered → 7.6 GB** | iGPU UMA frame buffer set to 128M via Smokeless_UMAF |
| Remaining ~8 GB reserved | **Not fixable in software** | Firmware never maps the mismatched pair's full capacity — proven 3 ways. Matched RAM kit only |
| Arch boots to black screen | **Fixed** | Display-manager was `sddm-plymouth` (broken); repointed to plain `sddm` + cleaned GRUB |
| Logo hang (must enter BIOS to boot) | **Fix identified** | Firmware **Fast Boot** was enabled (stale memory-training context); disable it |
| Change the Acer boot logo | **Blocked** | Row is `SuppressIf True`; the `Setup` variable is OS-write-protected (`dmpstore` fails). Only H2OUVE (SMI) could, risk not worth it |
| Windows won't boot (BSOD, even safe mode) | **Fixed** | Stale **Fast Startup** `hiberfil.sys` resume failed after firmware/memory changes; renamed it from Linux |

## Contents

- [`docs/FINDINGS.md`](docs/FINDINGS.md) — the RAM investigation with firmware-level proof, the hang, the logo lock, the Windows BSOD
- [`docs/COMMANDS.md`](docs/COMMANDS.md) — every important command: passwordless SSH automation, Smokeless_UMAF staging, UEFI shell, memory checks, the hiberfil + GRUB fixes
- [`docs/BIOS_OPTIONS_GUIDE.md`](docs/BIOS_OPTIONS_GUIDE.md) — curated guide to the hidden AMD CBS and Acer menus, with safety flags, factory defaults and known-good values
- [`docs/BIOS_SETTINGS_FULL.md`](docs/BIOS_SETTINGS_FULL.md) — the full 3,361-setting reference decoded from the firmware IFR (every option, defaults marked `★`)
- [`scripts/parse_ifr.py`](scripts/parse_ifr.py) — turns an `ifrextractor` dump into the deduped settings reference
- [`scripts/patch_dmpstore.py`](scripts/patch_dmpstore.py) — patches a byte in a `dmpstore`-saved EFI variable and fixes its CRC

## Key firmware facts for this board

- **Acer `Setup` varstore**: GUID `A04A27F4-DF00-4D42-B552-39511302113D`, size `0x2BC`. Holds the visible+hidden Acer settings. **OS-write-protected** — `dmpstore -l` and `setup_var.efi` both fail with "Write Protected" / error 0x8. Writable only through the firmware's own setup engine (F2 BIOS, or Smokeless_UMAF's SetupBrowser) or Insyde's H2OUVE (SMI channel).
- **AMD `AmdSetup` varstore**: GUID `3a997502-647a-4c82-998e-52ef9486a247`. Direct `efivarfs` writes persist but AGESA **ignores** them; changes only take through the setup engine (Smokeless_UMAF).
- Useful `Setup` byte offsets (VarStore `0x1234`): `0x22E` Fast Boot, `0x22D` POST Animation & Sound, `0x24E` Customize POST animation (logo), `0x24F` Customize POST audio, `0x212` D2D Recovery.
- UMA frame buffer lives at `AmdSetup` VarStore `0x5000`, offset `0xD4` (32-bit), prompt "UMA Frame buffer Size".

## Safety

Firmware edits can brick the machine or lock Windows. See the per-section flags in the guide. Short version: never touch the DRAM **timing** menu (proven 3-beep no-POST), the controller/USB/SATA/I2C enables, Boot Mode, Secure Boot, TPM state, or voltage pages. Keep a CMOS-reset path ready (RTC cell under the main battery).

*Not affiliated with Acer or Insyde. Model-specific — offsets and variable names differ on other machines.*
