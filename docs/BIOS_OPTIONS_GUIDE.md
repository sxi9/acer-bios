# Acer Nitro 5 AN515-43 — Hidden BIOS Options Guide (Smokeless_UMAF)

**Machine:** Ryzen 5 3550H (Picasso) + Vega 8 iGPU + RX 560X dGPU, BIOS V1.12 (FH50P 05.32.42)
**Source:** decoded from the official BIOS image's own setup forms (IFR). 3,361 unique settings in 490 menus.
**Companion file:** `BIOS_SETTINGS_FULL.md` = every setting, every option, with factory default marked ★.

## How to read this
- 🟢 **Safe to change** — reversible, won't stop the laptop booting.
- 🟡 **Change with care** — works, but has side effects (perf/thermals/power) or needs a specific revert.
- 🔴 **Don't touch** — can cause no-POST (needs CMOS reset) or lock you out of Windows/data.
- ★ = firmware factory default.  **now:** = what is set on your laptop right now (as of this session).
- Navigation in UMAF: **Device Manager → AMD CBS → …**  Save = **F10**.  **F9 = Reset to Defaults** (shown in UMAF footer).

## Recovery, always
- Any no-POST → power-cycle 2–5× (firmware `Fail_CNT = 5` auto-reverts memory settings), else CMOS reset (RTC cell under battery).
- A CMOS reset wipes **everything**, including the UMA win below → you re-apply it.
- Changing Secure Boot / TPM can make Windows demand a **BitLocker recovery key**. Have it before touching those.

---

## 0. What's already changed on your laptop (current state)
| Setting | Where | now | ★ default | Effect |
|---|---|---|---|---|
| Integrated Graphics Controller | NBIO → GFX Configuration | **Forces** | Auto | needed to unhide UMA options |
| UMA Mode | NBIO → GFX Configuration | **UMA_SPECIFIED** | Auto | unlocks frame buffer size |
| UMA Frame buffer Size | NBIO → GFX Configuration | **128M** | Auto (≈2 GB grabbed) | **+~2 GB usable RAM → 7.6 GB total** ✅ |
| Memory interleaving | DF Common Options | Auto (reset by Fail_CNT) | Auto | tested None: no change |
| Overclock / Memory Clock Speed | UMC → DDR4 → DRAM Timing | Auto / Auto (reset) | Auto | tested 1067 MHz: **3 beeps, no-POST** ❌ |

**Hard conclusion:** the remaining ~8 GB is never placed in the memory map by the firmware (mismatched 2667 + 3200 sticks). No setting below recovers it; a matched kit does.

---

## 1. AMD CBS (the hidden menu) — Device Manager → AMD CBS

### 1a. NBIO Common Options → GFX Configuration
| Setting | Options | now | Flag | Notes |
|---|---|---|---|---|
| Integrated Graphics Controller | Disabled / Forces / Auto★ | Forces | 🟢 | **Never pick Disabled** (panel runs on iGPU) → treat *Disabled* as 🔴 |
| UMA Mode | Auto★ / UMA_SPECIFIED / UMA_AUTO | UMA_SPECIFIED | 🟢 | |
| UMA Frame buffer Size | Auto★ / 64M / 80M / 96M / 128M / 256M / 384M / 512M / 768M / 1G / 2G / 3G / 4G / 8G / 16G | 128M | 🟢 | 128M is fine for desktop (rest comes from shared GTT). Go 256M+ if you see glitches |
| UMA Version | Legacy / Non-Legacy / Hybrid Secure / Auto★ | Auto | 🟡 | leave Auto |
| Display Resolution | 1920x1080 and below / 2560x1600 / 3840x2160 / Auto★ | Auto | 🟢 | sizing hint for the framebuffer |
| NB Azalia | Disabled / Enabled / Auto★ | Auto | 🟡 | iGPU HDMI audio — Disabled kills HDMI sound |

### 1b. NBIO Common Options (top level)
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| **System Configuration (cTDP)** | 12W / 15W / 25W / **35W★** / 45W / 54W POR (Consumer) ; 35/45/54W Embedded ; Auto | 35W | 🟡 | **The power limit of the CPU.** 25W = cooler/quieter, less perf. 45W = more perf, much hotter — this chassis is built for 35W. Most interesting legit tuning knob here |
| Audio IOs | MIN HDA★ / MAX HDA / SoundWire variants / I2S-TDM / DISABLE | MIN HDA | 🔴 | wrong value = no audio at all |
| System Temperature Tracking | Auto★ / Disable / Enable | Auto | 🟡 | firmware thermal tracking; leave |
| NB Configuration → IOMMU | Disabled / Enabled / Auto★ | Auto | 🟢 | Enabled = needed for VM PCI passthrough; harmless |
| PCIe Configuration → PSPP Policy | Disabled / Performance / Balanced / Power Saving / Auto★ | Auto | 🟢 | PCIe link power policy. *Performance* = dGPU link never downclocks (slightly more heat/battery) |

### 1c. Zen Common Options (CPU)
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| Core Performance Boost | Disabled / Auto★ | Auto | 🟡 | Disabled = no turbo → cooler, slower |
| Global C-state Control | Disabled / Enabled / Auto★ | Auto | 🟡 | Disabled = less idle power saving; sometimes fixes sleep bugs |
| OC Mode | Normal Operation★ / OC1 / Customized | Normal | 🔴 | CPU overclock profiles on a laptop — no |
| Streaming Stores Control | Disabled / Enabled / Auto★ | Auto | 🟡 | niche perf; leave |
| Enable IBS | Disabled / Enabled / Auto★ | Auto | 🟡 | profiling; leave |
| Platform First Error Handling | Enable / Disable / Auto★ | Auto | 🔴 | error-handling plumbing |
| RedirectForReturnDis / L2 TLB Associativity | Auto★ | Auto | 🔴 | errata workarounds |
| ("Agree" page) Downcore control | ONE / TWO / THREE / Auto★ | Auto | 🟡 | run with fewer cores (test/thermal). Reversible, but weird |
| ("Agree" page) SMTEN | Disable / Auto★ | Auto | 🟡 | turn off SMT (4C/4T instead of 4C/8T) |

### 1d. DF Common Options (Data Fabric)
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| Memory interleaving | Auto★ / None / Channel / Die / Socket | Auto | 🟢 | tested None → no RAM change. Channel/Die/Socket are *ignored* on unsupported populations |
| Memory interleaving size | Auto★ / 256B / 512B / 1K / 2K | Auto | 🟡 | only matters if interleaving active |
| Channel interleaving hash | Disabled / Enabled / Auto★ | Auto | 🟡 | leave |
| Location of private memory regions | Distributed / Consolidated / Auto★ | Auto | 🟡 | where PSP/SMU/CC6 reserved blocks live (top of DRAM vs spread). Moves, doesn't shrink them |
| DRAM scrub time | Disabled / 1h / 4h / 8h / 16h / 24h / 48h / Auto★ | Auto | 🟢 | ECC scrub cadence — irrelevant on non-ECC SO-DIMMs |
| Redirect scrubber / Sync flood / GMI & xGMI encryption / CC6 encryption / System probe filter / DF C-state / xGMI DLWM / Freeze DF queues | Auto★ | Auto | 🔴 | fabric internals; no user value |

### 1e. UMC Common Options (memory controller)
**DDR4 Common Options → DRAM Timing Configuration ("I Accept" page)** — 42 settings
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| Overclock | Auto★ / Enabled | Auto | 🔴 | **Proven: Enabled + manual clock = 3 beeps / no-POST on these sticks.** Leave Auto |
| Memory Clock Speed | Auto★ / 333…2100 MHz (DDR rate = 2×) | Auto (=2400) | 🔴 | same as above |
| Tcl, Trcdrd, Trcdwr, Trp, Tras, Trc, TrrdS/L, Tfaw, Twtr, Twr, Trfc… (all timings) | Auto★ / manual clocks | Auto | 🔴 | DRAM timings; no-POST territory |
| ProcODT, Fail_CNT, Tcwl, Trtp, Tcke… | Auto★ | Auto | 🔴 | Fail_CNT=5 is your auto-recovery; keep |

**DDR4 Common Options → DRAM Controller Configuration**
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| Cmd2T | 1T / 2T / Auto★ | Auto | 🟡 | **2T = more stable command timing**, ~1–2% slower. The one memory knob that is a *stability* lever rather than a speed one |
| Gear Down Mode | Disabled / Enabled / Auto★ | Auto | 🟡 | stability helper at high clocks; leave |
| Data Mask | Auto★ / Enabled / Disabled | Auto | 🔴 | leave |
| DRAM Power Options → Power Down Enable | Disabled / Enabled / Auto★ | Auto | 🟢 | Disabled = tiny perf gain, more idle power |

**DDR4 Common Options → CAD Bus / Data Bus Configuration** — drive strengths, setup times, ODT: 🔴 all of it (training stability).

**DRAM Memory Mapping**
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| Chipselect Interleaving | Disabled / Auto★ | Auto | 🟢 | within-stick interleave; no capacity effect |
| BankGroupSwap / BankGroupSwapAlt | APU / CPU / Disabled / Auto★ ; Enabled / Disabled / Auto★ | Auto | 🟡 | address-mapping perf tweaks; harmless, no capacity effect |
| Address Hash Bank / Address Hash CS | Disabled / Enabled / Auto★ | Auto | 🟡 | same |

**Memory MBIST (built-in memory test at boot)**
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| MBIST Enable | Auto★ / Disabled / Enabled | Auto | 🟡 | Enabled runs a firmware memory self-test every boot (slow POST). Diagnostic only |
| MBIST Test Mode | Auto★ / Interface Mode / Data Eye Mode | Auto | 🟡 | Data Eye = measures voltage/timing margins of your sticks (results go to the firmware ABL log, not the screen) |
| MBIST Aggressors / Per-Bit Reporting | Auto★ | Auto | 🟡 | |

**Common RAS / ECC / Security**
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| Data Poisoning | Disabled / Enabled / Auto★ | Auto | 🔴 | RAS internals |
| DRAM ECC Enable / Symbol Size | Disabled / Enabled / Auto★ ; x4 / x8 / Auto★ | Auto | 🟢 | SO-DIMMs are non-ECC → no effect |
| TSME (memory encryption) | Disabled★ / Enabled / Auto | Disabled | 🟡 | Transparent memory encryption; small perf cost, no visible change. Leave |

### 1f. FCH Common Options (chipset I/O)
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| SATA Controller | Disabled / Enabled / Auto★ | Auto | 🔴 | **Arch lives on the SATA SSD** — Disabled = Arch gone |
| SATA Mode | AHCI / AHCI as ID 0x7904 / Auto★ / RAID | Auto | 🔴 | help text itself says Raven FP5 doesn't support RAID |
| Aggressive SATA Device Sleep Port 0/1 | Disable / Enable / Auto★ | Auto | 🟢 | power saving on the SSD |
| XHCI0 / XHCI1 controller enable | Enabled / Disabled / Auto★ | Auto | 🔴 | Disabled = USB ports (and maybe internal devices) dead |
| I2C 0–5 Enable | Disabled / Enabled / Auto★ | Auto (I2C3 ★Enabled) | 🔴 | **Touchpad is on I2C** — disabling the wrong bus kills it |
| Uart 0–3 Enable (+ Legacy Options) | Disabled / Enabled / Auto★ | Auto | 🟢 | Enabling UART0 exposes a serial port to the OS (you asked about UART earlier — this is the knob). Reversible |
| ESPI Enable | Disabled / Enabled / Auto★ | Auto | 🔴 | link to the embedded controller — keyboard/power/battery |
| Ac Loss Control | Always Off★ / Always On / Previous | Always Off | 🟢 | laptop: mostly moot |
| System Control → Toggle All PwrGood On Cf9 | Disabled / Enabled / Auto★ | Auto | 🔴 | reset plumbing |

### 1g. Fan Control (AMD CBS)
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| Fan Control | Manual / Auto★ | Auto | 🟡 | Manual unlocks the curve below |
| Force PWM Control / Force PWM | Force / Unforce★ ; 0–100 | Unforce | 🟡 | pin the fan at a fixed % (test only) |
| Fan Table Control | Manual / Auto★ | Auto | 🟡 | custom curve |
| Low / Medium / High / Critical Temperature | °C numbers | — | 🟡 | curve breakpoints |
| Low / Medium / High Pwm | 0–100 | — | 🟡 | curve duty cycles |
| Temperature Hysteresis | °C | — | 🟡 | |
| Pwm Frequency | 100Hz / 25kHz★ | 25kHz | 🔴 | wrong freq = fan whine or no spin |
| Fan Polarity | Negative★ / Positive | Negative | 🔴 | wrong polarity = fan never runs |
*Note: on this Acer the EC (via Predator Sense / NitroSense) usually owns the fan; CBS fan tables may be overridden by the EC.*

---

## 2. Acer's normal Setup menu (the F2 BIOS you already see)

**Main**
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| F12 Boot Menu | Disabled★ / Enabled | Disabled | 🟢 | you already use F12 — worth confirming Enabled |
| Network Boot | Disabled★ / Enabled | Disabled | 🟢 | PXE; leave off |
| Touchpad | I2C★ / PS2 | I2C | 🟡 | PS2 = legacy mode (fallback if the I2C driver is missing) |
| Function key behavior | Function Key★ / Media Key | Function Key | 🟢 | swap Fn default |
| Lid Open Resume | Disabled / Enabled★ | Enabled | 🟢 | |
| Wake on LAN / Wake on USB while lid closed / USB & TBT wake from S4 | Disabled★ mostly | — | 🟢 | |
| D2D Recovery | Disabled / Enabled★ | Enabled | 🟡 | Alt+F10 Acer recovery during POST |
| Fast Boot / xHCI Support / SATA Mode (AHCI★) | — | — | 🟡 / 🟢 / 🔴 | SATA Mode: don't change |

**Boot**
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| Boot Mode | UEFI★ / Legacy | UEFI | 🔴 | Legacy = neither Windows nor Arch boots |
| Secure Boot | Enabled★ / Disabled | Enabled | 🔴 | can trigger BitLocker recovery; leave as is |
| Secure Boot key mgmt (X509 / PK / KEK / db) | enroll / delete / restore factory | — | 🔴 | |

**Power**
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| **Thermal Fan Control** | Auto / Disabled★ | Disabled | 🟡 | ships *Disabled* — setting Auto hands fan control to firmware thermal logic. Interesting if the EC fan behaviour annoys you |
| ACPI S3 | Disabled / Enabled★ | Enabled | 🔴 | S3 sleep — leave on |
| ACPI S1 | Disabled★ / Enabled | Disabled | 🟢 | |
| Wake on PME | Disabled / Enabled★ | Enabled | 🟢 | |
| Auto Wake on S5 / Day of Month | Disabled★ / Every Day / Day of Month | Disabled | 🟢 | scheduled power-on |

**CPU Related setting / Advanced CPU Control**
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| SVM support | Disabled / Enabled★ | Enabled | 🟢 | AMD-V virtualization — needed for VMs/WSL2 |
| SVM Lock / SMM Code Lock | Disabled / Enabled★ | Enabled | 🔴 | security locks |
| CPU P-State Setting | Auto★ / Lowest Speed | Auto | 🟡 | Lowest = permanent slow mode |
| Cool N' Quiet | Disabled / Enabled★ | Enabled | 🟡 | |
| Multi CORE Support | Disabled / Auto★ | Auto | 🔴 | Disabled = single core |

**Security**
| Setting | Options | ★ | Flag | Notes |
|---|---|---|---|---|
| Change TPM (TCM) State | No Change★ / Enable & Active / Deactive & Disable / Enabled / Disabled | No Change | 🔴 | **BitLocker** / Windows Hello break if changed |
| Password on Boot | Enabled / Disabled★ | Disabled | 🟡 | needs a supervisor password first |
| Above 4GB MMIO (PicassoPI page) | Enabled / Disabled | — | 🟡 | leave; needed for large-BAR devices |

---

## 3. Menus the extractor could NOT decode reliably
**AMD PBS / "Enable-Disable PCIe x8 Slot D3Cold" / HybridGraphics / Discrete GPU D3Cold / DPTC / VDD18 voltage pages.**
Their prompt/help strings came out scrambled (string IDs mis-resolved), so the full dump shows nonsense pairs there. They *do* exist in UMAF and contain real things: Discrete GPU D3Cold, HybridGraphics toggle, NVIDIA DGPU power, DPTC interface, VDD18 / 5V rails (🔴 voltages). **Read them in UMAF only; don't act on the dump's labels for these.**

---

## 4. The "never" list (one screen)
- Timing menu: Overclock / Memory Clock Speed / any Tcl…Trfc / CAD & Data bus → **no-POST (proven)**
- Integrated Graphics Controller = Disabled; Audio IOs; XHCI; I2C; ESPI; SATA Controller/Mode; Multi CORE → **loses display / USB / touchpad / keyboard / Arch disk / cores**
- Boot Mode = Legacy; Secure Boot; TPM state; SVM/SMM locks → **Windows won't boot or asks BitLocker key**
- OC Mode; Fan Pwm Frequency / Polarity; VDD voltages (PBS) → **hardware risk**

## 5. Worth trying (ranked, all reversible)
1. **System Configuration = 25W** (NBIO) — cooler/quieter laptop; or 45W for more sustained perf if you accept heat. Revert: 35W.
2. **Thermal Fan Control = Auto** (Power) — see if firmware fan logic is nicer than the EC default.
3. **Cmd2T = 2T** (UMC → DRAM Controller) — a *stability* lever for mismatched sticks; costs ~1–2%. Won't add RAM, may reduce the random boot-logo hang.
4. **PSPP Policy = Performance** (NBIO → PCIe) — keeps the dGPU link at full speed; small heat/battery cost.
5. **F12 Boot Menu = Enabled** (Main) — convenience.
6. **Uart 0 Enable = Enabled** (FCH) — only if you want to poke at the serial port you asked about earlier.
7. **MBIST Data Eye Mode** (UMC → Memory MBIST) — pure diagnostic; longer POST; results hidden in ABL log. Low value, zero gain.
