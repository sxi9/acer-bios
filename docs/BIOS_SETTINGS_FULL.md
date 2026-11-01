# Acer Nitro AN515-43 — Full BIOS Settings Reference (from firmware IFR)

Unique settings: 3361   |   Menus/forms: 490

Legend: [select] = dropdown, [toggle] = on/off, [number] = numeric field, ★ = firmware factory default

---

## EFI Floppy  (3 settings)

- [select] **Do you want to recovery ROM part? (Caution: Not every OS is bootable in Recovery Mode.)** — Execution of the selected file has been blocked by the current security policy.★ /  boot failed.
    - _Flash Status_
- [select] **YES,this choice will flash Rom part.** — Execution of the selected file has been blocked by the current security policy.★ /  boot failed.
    - _NO, abort Recovery mode and restart system._
- [select] **Rebooting !** — Execution of the selected file has been blocked by the current security policy.★ /  boot failed.
    - _% of the system memory tested OK_

## List all the Driver Health instances to manage  (1 settings)

- [number] **Press Esc for boot options**
    - _Esc is pressed. Go to boot options._

## SATA Port 2     (15 settings)

- [select] **Press [ESC] Abort Harddisk Security** —   Fermer    / Enter incorrect password 3 times★ /   Lock    
    - _Harddisk Security_
- [select] **Please press Enter to continue**
    - _[ENTER]_
- [select] **HDD Security count expired bit is acted** —   Fermer   ★ / SATA Port 5    /   Lock    
    - _Please shutdown the system_
- [select] **Please input password for ** —   Fermer    / SATA Port 5   ★ /   Lock    
- [select] **Error Status** —   Fermer   ★ / SATA Port 5    /   Lock    
    - _Enter incorrect password too many times_
- [select] **Press any key** — HDD0          ★ / HDD1          
    - _HDD           _
- [select] **HDD2          ** —   Lock    ★ / HDD4          
    - _HDD3          _
- [select] **HDD(OPAL)     ** —   Lock    ★ / SATA Port 5   
    - _HDD0(OPAL)    _
- [number] **HDD1(OPAL)    **
    - _HDD2(OPAL)    _
- [number] **HDD3(OPAL)    **
    - _HDD4(OPAL)    _
- [number] **Press Esc for boot options**
    - _Esc is pressed. Go to boot options._
- [toggle] **SATA Port 4   **
    - _SATA Port 5   _
- [toggle] **SATA Port 6   **
- [number] **HDD           **
    - _HDD0          _
- [select] **HDD1          ** — HDD3          ★ / HDD4          
    - _HDD2          _

## ￱錯誤狀態￰  (1 settings)

- [toggle] **￱請重置系統￰**

## デバイス パラメタを構成します。  (64 settings)

- [select] **バージョン：** — 固定 MAC アドレス
    - _^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$_
- [select] **PCI アドレス** — プライマリ DNS
- [select] **リンク ステータス** — 固定 MAC アドレス
    - _接続完了_
- [select] **切断完了** — 固定 MAC アドレス★
    - _LED を点滅させる_
- [select] **PCIバス：デバイス：機能。** — 固定 MAC アドレス
    - _リンク ステータス_
- [select] **LED を最大 15 秒点滅させる。** — 旧式ブート プロトコル★ / UEFI 以外のブート プロトコルを選択：Preboot Execution Environment (PXE)/iSCSI。
    - _旧式ブート プロトコル_
- [select] **PXE** — ナシ
    - _iSCSI_
- [select] **ナシ** — 固定 MAC アドレス
    - _ブート ストラップのタイプ_
- [number] **ブート ストラップのタイプ**
    - _ブート ストラップのタイプを選択する。_
- [number] **リンク速度**
- [number] **リンク速度を設定する。**
    - _プリブート Wake On LAN_
- [number] **プリブート Wake on LAN (WOL) を設定する。**
    - _Wake On LAN_
- [select] **Wake on LAN (WOL) を構成します。**
- [select] **無効な TCP ポート** — HP共有メモリ機能を無効にします / 予約されたメモリ領域の使用状況のデバイス割り当てを直接ゲスト仮想マシンに許可をディセーブルにします。 / 新しい画像はこのデバイスではサポートされていません。 / 容量が不足しているために画像を保存できません。 / 新しい画像のバージョンは現在の画像と同じか、それよりも古いバージョンです。 / 処理中にエラーが発生しました。★ / イメージ：
    - _無効な VLAN ID_
- [select] **iSCSI ファースト ターゲット パラメタ** — 固定 MAC アドレス
- [select] **iSCSI ファースト ターゲット パラメタを設定する。** — 固定 MAC アドレス
    - _iSCSI セカンド ターゲット パラメタ_
- [select] **iSCSI セカンド ターゲット パラメタ** — 固定 MAC アドレス
- [select] **iSCSI 名** — CHAP ID / CHAP ID を設定する (32 文字まで)。 / CHAP ID を設定する (128 文字まで)。 / 固定 MAC アドレス
    - _iSCSI 名を設定する。_
- [select] **CHAP ID** — CHAP ID / CHAP ID を設定する (32 文字まで)。 / CHAP ID を設定する (128 文字まで)。
- [select] **CHAP ID を設定する (32 文字まで)。** — CHAP ID / CHAP ID を設定する (32 文字まで)。 / CHAP ID を設定する (128 文字まで)。
    - _CHAP ID を設定する (128 文字まで)。_
- [select] **CHAP 秘密情報** — CHAP 秘密情報★ / CHAP 秘密情報を設定する (12 ～ 16 文字)。 / 固定 MAC アドレス
- [select] **CHAP 秘密情報を設定する (12 ～ 16 文字)。** — CHAP 秘密情報★ / CHAP 秘密情報を設定する (12 ～ 16 文字)。
    - _CHAP 秘密情報_
- [select] **リンク アップの遅延時間を秒単位で設定する (0 ～ 255 秒)。** — 固定 MAC アドレス★ / CHAP 秘密情報
    - _TCP タイムスタンプを使用_
- [select] **TCP タイムスタンプ** — 固定 MAC アドレス★
    - _TCP タイムスタンプをイネーブル/ディスエーブルする。_
- [select] **ターゲットをファースト HDD として表示** — 固定 MAC アドレス★
    - _ターゲットをシステムのファースト ハード ディスク ドライブ (HDD) として表示することをイネーブル/ディスエーブルする。_
- [select] **LUN ビジー再試行カウント** — IP バージョン★ / IP バージョンのサポート。このパラメタを変更するとすべての IP 関連のフィールドがリセットされます。
    - _LUN がビジーな場合に、2 秒置きに何回再試行するか設定する (0 ～ 60 回)。_
- [select] **iSCSI セカンダリ デバイス パラメタ** — 固定 MAC アドレス
- [select] **サブネット マスク プリフィックス** — 固定 MAC アドレス
    - _IP サブネット マスク プリフィックス長を設定する。_
- [select] **デフォルト ゲートウェイ** — プライマリ DNS
    - _デフォルト ゲートウェイの IP アドレスを設定する。_
- [select] **セカンダリ DNS** — 仮想 MAC アドレス
    - _セダンダリ DNS の IP アドレスを設定する。_
- [select] **IP アドレス** — 固定 MAC アドレス★ / MAC アドレス
    - _ターゲット IP アドレスを設定する。_
- [select] **IP 自動コンフィギュレーション** — 固定 MAC アドレス★
    - _ステートフルまたはステートレスな自動コンフィギュレーションで TCP/IP コンフィギュレーションを取得する。_
- [select] **iSCSI ターゲットでのブート** — 固定 MAC アドレス★
    - _ターゲットでのブート_
- [select] **ログオン後の iSCSI ターゲットでのブートをイネーブル/ディスエーブルする。** — 固定 MAC アドレス
    - _DHCP ベンダ ID_
- [select] **サブネット マスク** — 固定 MAC アドレス★ / MAC アドレス
    - _IP サブネットマスクを設定する。_
- [select] **仮想 LAN** — 固定 MAC アドレス★
    - _仮想 LAN モードを設定する。_
- [select] **VLAN ID (1..4094)** — バーチャル LAN ID (1..4094) を構成します。★ / 自動ネゴシエーション
    - _バーチャル LAN ID_
- [select] **10 Mbps 半二重** — 100 Mbps 半二重★ / 100 Mbps 全二重
    - _10 Mbps 全二重_
- [select] **自動ネゴシエート済み** — 10 Mbps 全二重 / 100 Mbps 半二重★ / 100 Mbps 全二重
    - _10 Mbps 半二重_
- [select] **無効** — 固定 MAC アドレス
    - _有効_
- [select] **IPv6** — 固定 MAC アドレス
    - _MBA コンフィギュレーション メニュー_
- [select] **一時的に無効** — 固定 MAC アドレス★ / チップ タイプ
    - _IPv4_
- [select] **MBA コンフィギュレーション メニュー** — 固定 MAC アドレス★
    - _MBA (Multiple Boot Agent) パラメタを設定する。_
- [select] **NICの設定** — 固定 MAC アドレス
- [select] **DHCP 経由の iSCSI パラメタ** — DHCP 経由で iSCSI パラメタを取得する。 / CHAP 認証 / CHAP 認証をイネーブル/ディスエーブルする。★
- [select] **iSCSI ブート コンフィギュレーション メニュー** — 固定 MAC アドレス★
- [select] **iSCSI ブート パラメタを設定する。** — 固定 MAC アドレス★
    - _iSCSI の設定_
- [select] **iSCSI の設定** — 固定 MAC アドレス★
    - _ファームウェア イメージ メニュー_
- [select] **ファームウェア イメージ メニュー** — 固定 MAC アドレス★
    - _ファームウェア イメージの情報。_
- [select] **現在 NVRAM 上にプログラムされているファームウェア イメージ コンポーネント (およびそれらに対応するバージョン) のリスト。[該当なし] はイメージが存在しないことを示します。** — 固定 MAC アドレス★
- [select] **ファームウェア イメージのプロパティ** — 固定 MAC アドレス★
    - _DHCP 経由の TCP/IP パラメタ_
- [select] **DHCP 経由で TCP/IP コンフィギュレーションを取得する。** — 固定 MAC アドレス
    - _IP 自動コンフィギュレーション_
- [select] **DHCP ベンダ ID を設定する (32 バイトまで)。** — 固定 MAC アドレス★
    - _リンク アップ遅延時間_
- [number] **ターゲットの確立をイネーブル/ディスエーブルする。** — ターゲット TCP ポート番号を設定する (1 ～ 65535)。★ / TCP ポート
    - _接続_
- [select] **ターゲット TCP ポート番号を設定する (1 ～ 65535)。** — ターゲット ブート LUN 番号を設定する (0 ～ 255)。★ / ブート LUN / セカンダリ デバイス / セカンダリ デバイスの MAC アドレスを入力する。XX:XX:XX:XX:XX:XX 形式を使用する。 / セカンダリ デバイス MAC アドレス / 独立したターゲット ポータルを使用 / multipath I/O がイネーブルな場合、独立したターゲット ポータルを使用する。 / 独立したターゲット名を使用 / multipath I/O がイネーブルな場合、独立したターゲット名を使用する。 / ファミリ ファームウェア バージョン / ブートコード / MBA / iSCSI ブート / ASF / NC-SI / SMASH / CCM
    - _ブート LUN_
- [select] **UMP** — Fcode★ / コントローラのBIOSバージョン / MBA / iSCSI ブート / ASF / NC-SI / SMASH / CCM / UMP / EFI バージョン / ブート コード / 複数のブート エージェント / UEFI オプション ROM / Fcode オプション ROM / 管理ファームウェア
    - _EFI_
- [select] **構成 ROM** — iSCSI 全般パラメタ★
    - _メイン コンフィギュレーション ページ_
- [select] **iSCSI の全般的なブート パラメタを設定する。** — iSCSI イニシエータ パラメタ / チップ タイプ★
    - _iSCSI イニシエータ パラメタ_
- [select] **iSCSI イニシエータ パラメタを設定する。** — 固定 MAC アドレス
    - _iSCSI ファースト ターゲット パラメタ_
- [select] **iSCSI セカンド ターゲット パラメタを設定する。** — 固定 MAC アドレス★ / セカンダリ デバイス / セカンダリ デバイスのパラメタを設定する。
    - _セカンダリ デバイス_
- [select] **FlexAddressing** — 固定 MAC アドレス
    - _TX 帯域幅コントロール最大_
- [number] **旧式ブート プロトコル**
- [select] **UEFI 以外のブート プロトコルを選択：Preboot Execution Environment (PXE)/iSCSI。** — iSCSI★ / ナシ
    - _PXE_
- [toggle] **MAC アドレス**
    - _固定 MAC アドレス_

## 10 Mbps 全二重  (2 settings)

- [select] **IPv4** — バス：デバイス：機能★ / チップのタイプと改訂番号。
    - _IPv6_
- [select] **iSCSI の設定** — バス：デバイス：機能★ / チップのタイプと改訂番号。

## TCP タイムスタンプ  (6 settings)

- [select] **ターゲットをファースト HDD として表示** — バス：デバイス：機能★ / チップのタイプと改訂番号。
    - _ターゲットをシステムのファースト ハード ディスク ドライブ (HDD) として表示することをイネーブル/ディスエーブルする。_
- [select] **IP バージョン** — バス：デバイス：機能★ / チップのタイプと改訂番号。
    - _IP バージョンのサポート。このパラメタを変更するとすべての IP 関連のフィールドがリセットされます。_
- [select] **IP アドレス** — バス：デバイス：機能★ / チップのタイプと改訂番号。
    - _ターゲット IP アドレスを設定する。_
- [select] **サブネット マスク** — バス：デバイス：機能★ / チップのタイプと改訂番号。
    - _IP サブネットマスクを設定する。_
- [select] **デフォルト ゲートウェイ** — バス：デバイス：機能★ / チップのタイプと改訂番号。
    - _デフォルト ゲートウェイの IP アドレスを設定する。_
- [select] **セカンダリ DNS** — バス：デバイス：機能★ / チップのタイプと改訂番号。
    - _セダンダリ DNS の IP アドレスを設定する。_

## ￱エラー状態￰  (1 settings)

- [toggle] **￱システムを再起動してください￰**

## IPv6 Current Setting  (17 settings)

- [select] **The hardware address of the network interface.** — Host addresses    :★
- [select] **Press ENTER to enter configuration menu for IPv6 configuration.** — The name of the interface.★
- [select] **The address list which contain the local IPv6 addresses and the corresponding prefix length information.**
    - _Route Table       :_
- [select] **Current gateway IPv6 addresses.** — The name of the interface.
    - _DNS addresses     :_
- [select] **Current DNS server list.** — The name of the interface.★
    - _Interface ID_
- [select] **The route table of the IPv6 network stack runs on this interface.** — The name of the interface.
    - _Gateway addresses :_
- [select] **The 64 bit alternative interface ID for the device. The string is colon separated. e.g. ff:dd:88:66:cc:1:2:3** — The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address. A value of zero indicates that Duplicate Address Detection is not performed.★ / Policy
    - _DAD Transmit Count_
- [select] **automatic or manual** — manual
    - _automatic_
- [select] **Advanced Configuration** — The name of the interface.
    - _Configure the interface manually. IP address, gateway address, and DNS server address can be configured._
- [number] **New IPv6 address**
    - _Manual IP address can only be configured under manual policy. Separate the IP address with blank space to configure more than one address. e.g. 2002::1/64 20..._
- [number] **New Gateway addresses**
    - _Gateway IP address can only be configured under manual policy. e.g. 2002::3. Separate the IP address with blank space to configure more than one address._
- [number] **New DNS addresses**
    - _DNS addresses can only be configured under manual policy. e.g. 2002::4. Separate the IP address with blank space to configure more than one address._
- [number] **Save Changes and Exit**
    - _Save Changes for interface ID, DAD transmit count, policy, and data in advanced configuration._
- [select] **Commit Changes and Exit** — Enter Configuration Menu
    - _Discard Changes and Exit_
- [number] **DAD Transmit Count**
    - _The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address. A value of zero indicates ..._
- [select] **Policy** — automatic★ / manual
    - _automatic or manual_
- [toggle] **Interface Name    :**
    - _The name of the interface._

## Execution of the selected file has been blocked by the current security policy.  (1 settings)

- [toggle] **Esc is pressed. Go to boot options.**

## Le Statut de l'Erreur  (1 settings)

- [toggle] **Veuillez redémarrer le système**

## Bus:Gerät:Funktion  (1 settings)

- [select] **iSCSI-Offload-Support** — MAC-Adresse / Permanente MAC-Adresse★
    - _iSCSI-Boot-Support_

## Fcode  (4 settings)

- [select] **BootCode** — MAC-Adresse / UEFI – optionales ROM / Fcode – optionales ROM / iSCSI Boot★ / Management FW
    - _Multiple Boot Agent_
- [select] **ブート コード** — MAC アドレス / UEFI オプション ROM / Fcode オプション ROM / iSCSI ブート★ / 管理ファームウェア
    - _複数のブート エージェント_
- [select] **Bootcode** — Dirección MAC / Opción UEFI ROM / Opción Fcode ROM / Arranque iSCSI★ / Administración FW / MAC Address / UEFI Option ROM / Fcode Option ROM / iSCSI Boot / Management FW
    - _Multiple Boot Agent_
- [select] **Code d'initialisation** — Adresse MAC / ROM en option UEFI / ROM en option Fcode / Initialisation iSCSI★ / Micrologiciel de gestion
    - _Multiple Boot Agent_

## Management FW  (2 settings)

- [select] **Erste iSCSI-Zielparameter** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **iSCSI First Target Parameters** — MAC Address / Permanent MAC Address★

## Hauptkonfigurationsseite  (5 settings)

- [select] **Erste iSCSI-Zielparameter** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **HP Shared-Memory-Funktion deaktivieren** — Deaktiviert / Aktiviert★
    - _Deaktivieren Sie die Verwendung des reservierten Speichers Regionen zu ermöglichen direkte Zuordnung von Gerät zu virtuellen Gastcomputer._
- [number] **Blinkende LEDs**
    - _Blinkende LEDs für bis zu 15 Sekunden_
- [select] **Pre-boot Wake On LAN** — Deaktiviert / Aktiviert
    - _Pre-boot Wake On LAN (WOL) konfigurieren_
- [select] **Verbindungsstatus** — Verbindung getrennt / Verbunden

## Allgemeine iSCSI-Parameter  (14 settings)

- [select] **Erste iSCSI-Zielparameter** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **TCP/IP-Parameter über DHCP** — Deaktiviert / Aktiviert★
    - _TCP/IP-Konfigurationseinstellungen über DHCP erhalten._
- [select] **IP-Autokonfiguration** — Deaktiviert / Aktiviert★
    - _TCP/IP-Konfigurationseinstellungen über zustandbehaftete oder zustandslose Autokonfiguration erhalten._
- [select] **Automatische IP-Konfiguration** — Deaktiviert / Aktiviert★
    - _TCP/IP-Konfigurationseinstellungen über zustandbehaftete oder zustandslose Autokonfiguration erhalten._
- [select] **iSCSI-Parameter über DHCP** — Deaktiviert / Aktiviert★
    - _iSCSI-Parameter über DHCP erhalten._
- [select] **CHAP-Authentifizierung** — Deaktiviert★ / Aktiviert
    - _CHAP-Authentifizierung aktivieren/deaktivieren_
- [select] **Booten von iSCSI-Ziel** — Deaktiviert / Aktiviert★ / Einmalige Deaktivierung
    - _Booten von iSCSI-Ziel nach dem Einloggen aktivieren/deaktivieren_
- [select] **Booten von Ziel** — Deaktiviert / Aktiviert★ / Einmalige Deaktivierung
    - _Booten von iSCSI-Ziel nach dem Einloggen aktivieren/deaktivieren_
- [number] **Verzögerung nach Verbindungsaufbau**
    - _Verzögerung nach Verbindungsaufbau in Sekunden (0..255) konfigurieren._
- [select] **TCP-Zeitstempel verwenden** — Deaktiviert★ / Aktiviert
    - _TCP-Zeitstempel aktivieren/deaktivieren_
- [select] **TCP-Zeitstempel** — Deaktiviert★ / Aktiviert
    - _TCP-Zeitstempel aktivieren/deaktivieren_
- [select] **Ziel als erstes HDD** — Deaktiviert★ / Aktiviert
    - _Ziel erscheint als erstes Festplattenlaufwerk (HDD) im System._
- [number] **Anzahl Wiederholungen bei 'LUN besetzt'**
    - _Konfiguration der Anzahl der Wiederholungen auf 2 Sekunden wenn LUN besetzt ist (0..60)._
- [select] **IP-Version** — IPv4★ / IPv6
    - _IP-Version-Support. Eine Änderung dieses Parameters setzt alle IP-bezogenen Felder zurück._

## Allgemeine iSCSI-Bootparameter konfigurieren.  (1 settings)

- [select] **Erste iSCSI-Zielparameter** — MAC-Adresse / Permanente MAC-Adresse★

## Initiator-iSCSI-Parameter  (1 settings)

- [select] **Erste iSCSI-Zielparameter** — MAC-Adresse / Permanente MAC-Adresse★

## Initiator-iSCSI-Parameter konfigurieren.  (1 settings)

- [select] **Erste iSCSI-Zielparameter** — MAC-Adresse / Permanente MAC-Adresse★

## PCI-Bus:Gerät:Funktionsnummer für dieses Gerät.  (2 settings)

- [select] **VLAN-ID (1..4094)** — MAC-Adresse★ / Permanente MAC-Adresse
    - _Virtuelle LAN-ID_
- [select] **Virtuellen LAN-Modus** — MAC-Adresse★ / Permanente MAC-Adresse
    - _Virtuellen LAN-Modus konfigurieren._

## Verbindungsstatus  (4 settings)

- [select] **Int. 18 Std.** — MAC-Adresse / Banner-Nachricht Zeitüberschreitung / iqn.1995-05.com.broadcom.iscsiboot★
    - _Int. 19 Std._
- [select] **Wert für Zeitüberschreitung auswählen. (0 ist standardmäßig auf 4 Sekunden eingestellt, 15 bedeutet keine Zeitüberschreitung, 1-14 ist der Wert der Zeitüberschreitung in Sekunden)** — BRCM ISAN / 0.0.0.0★
- [select] **Eingabeaufforderung ausblenden** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **100 Mbps Halb** — MAC-Adresse
    - _100 Mbps Voll_

## Verbindung getrennt  (6 settings)

- [select] **SMASH** — MAC-Adresse
    - _CCM_
- [select] **IPv4** — IPv6 / MBA-Konfigurationsmenü★
    - _iSCSI-Boot-Konfigurationsmenü_
- [select] **100 Mbps Voll** — Aktiviert★ / Einmalige Deaktivierung
    - _Deaktiviert_
- [select] **iSCSI-Bootparameter konfigurieren.** — MAC-Adresse★ / Permanente MAC-Adresse
    - _iSCSI-Konfiguration_
- [select] **iSCSI-Konfiguration** — MAC-Adresse / Permanente MAC-Adresse★
    - _Menü Firmware Image_
- [select] **Menü Firmware Image** — MAC-Adresse / Permanente MAC-Adresse★
    - _Firmware-Image-Information_

## Blinkende LEDs für bis zu 15 Sekunden  (2 settings)

- [select] **Parameter des sekundären Geräts konfigurieren.** — MAC-Adresse / Permanente MAC-Adresse★
    - _iSCSI-Parameter des sekundären Geräts_
- [select] **iSCSI-Parameter des sekundären Geräts** — Option ROM★
    - _Parameter des sekundären Geräts konfigurieren._

## Bootprotokolle älterer Geräte  (28 settings)

- [select] **ASF** — MAC-Adresse / Permanente MAC-Adresse★
    - _NC-SI_
- [select] **Präfix für Subnetzmaske** — Permanente MAC-Adresse / CHAP-Geheimnis konfigurieren (12 – 16 Zeichen lang)★
    - _Länge des IP-Präfixes für Subnetzmaske konfigurieren._
- [select] **Standard-Gateway** — MAC-Adresse / Permanente MAC-Adresse★
    - _IP-Adresse des Standard-Gateways konfigurieren_
- [select] **Subnetzmaske** — MAC-Adresse / Permanente MAC-Adresse★
    - _Subnetzmaske konfigurieren._
- [select] **CCM** — MAC-Adresse / Permanente MAC-Adresse★
    - _UMP_
- [select] **EFI** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **Fcode** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **BIOS-Version des Controllers** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **MBA** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **iSCSI Boot** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **Boot-Strap-Typ auswählen.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Übertragungsrate_
- [select] **Übertragungsrate** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Übertragungsrate konfigurieren._
- [select] **Multiple-Boot-Agent-Parameter (MBA) konfigurieren.** — NIC-Konfiguration★
    - _NIC-Konfiguration_
- [select] **Virtuellen LAN-Modus** — VLAN-ID (1..4094)★ / Virtuelle LAN-ID
    - _Virtuellen LAN-Modus konfigurieren._
- [select] **10 Mbps Voll** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _100 Mbps Halb_
- [select] **100 Mbps Voll** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Deaktiviert_
- [select] **Aktiviert** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Einmalige Deaktivierung_
- [select] **IPv4** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _IPv6_
- [select] **Virtuelle LAN-ID (1..4094) konfigurieren.** — 10 Mbps Halb★ / 10 Mbps Voll
    - _Auto Neg_
- [select] **100 Mbps Halb** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _100 Mbps Voll_
- [select] **Automatische Aushandlung** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _10 Mbps Halb_
- [select] **Pre-boot Wake On LAN** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Pre-boot Wake On LAN (WOL) konfigurieren_
- [select] **Erste iSCSI-Zielparameter** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Erste iSCSI-Zielparameter konfigurieren.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Zweite iSCSI-Zielparameter_
- [select] **PCI-Geräte-ID** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
- [select] **Zweite iSCSI-Zielparameter** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Zweite iSCSI-Zielparameter konfigurieren.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Sekundäres Gerät_
- [select] **Booten von Ziel** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Booten von iSCSI-Ziel nach dem Einloggen aktivieren/deaktivieren_

## PXE  (10 settings)

- [select] **Sekundäre DNS** — iSCSI-Name / iSCSI-Name konfigurieren.★ / CHAP-ID
    - _Sekundäre DNS-IP-Adresse konfigurieren._
- [toggle] **Boot-Strap-Typ**
- [select] **セカンダリ DNS** — iSCSI 名 / iSCSI 名を設定する。★ / CHAP ID
    - _セダンダリ DNS の IP アドレスを設定する。_
- [toggle] **ブート ストラップのタイプ**
- [select] **DNS secundario** — Nombre de iSCSI / Configurar nombre de iSCSI.★ / ID CHAP
    - _Configurar dirección IP del DNS secundario._
- [toggle] **Tipo de autocarga**
- [select] **Serveur DNS secondaire** — Nom iSCSI / Configurer le nom iSCSI.★ / Réf. CHAP
    - _Configurer l'adresse IP du serveur DNS secondaire._
- [toggle] **Type d'amorçage**
- [select] **Secondary DNS** — iSCSI Name / Configure iSCSI name.★ / CHAP ID
    - _Configure secondary DNS IP address._
- [toggle] **Boot Strap Type**

## NONE  (13 settings)

- [select] **CHAP-ID** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **CHAP-ID konfigurieren (bis zu 32 Zeichen lang)** — MAC-Adresse / Permanente MAC-Adresse★
    - _CHAP-ID konfigurieren (bis zu 128 Zeichen lang)_
- [select] **CHAP-Kennwort** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **Zweite iSCSI-Zielparameter** — MAC-Adresse / Permanente MAC-Adresse★
    - _Zweite iSCSI-Zielparameter konfigurieren._
- [number] **Delete Boot Option**
    - _Will be valid immediately_
- [select] **Réf. CHAP** — Adresse MAC / Adresse MAC permanente★
- [select] **Configurer la réf. CHAP (jusqu'à 32 caractères).** — Adresse MAC / Adresse MAC permanente★
    - _Configurer la réf. CHAP (jusqu'à 128 caractères)._
- [select] **Clé secrète CHAP** — Adresse MAC / Adresse MAC permanente★
- [select] **Paramètres de la deuxième cible iSCSI** — Adresse MAC / Adresse MAC permanente★
    - _Configurer les paramètres de la deuxième cible iSCSI._
- [select] **CHAP ID** — MAC Address / Permanent MAC Address★
- [select] **Configure CHAP ID (up to 32 characters in length).** — MAC Address / Permanent MAC Address★
    - _Configure CHAP ID (up to 128 characters in length)._
- [select] **CHAP Secret** — MAC Address / Permanent MAC Address★
- [select] **iSCSI Second Target Parameters** — MAC Address / Permanent MAC Address★
    - _Configure iSCSI second target parameters._

## UMP  (21 settings)

- [select] **Erste iSCSI-Zielparameter konfigurieren.** — Zweite iSCSI-Zielparameter
    - _Zweite iSCSI-Zielparameter_
- [select] **MAC-Adresse des sekundären Geräts** — MAC-Adresse / Permanente MAC-Adresse★
    - _Unabhängiges Zielportal verwenden_
- [select] **Unabhängiges Zielportal verwenden** — MAC-Adresse / Permanente MAC-Adresse★
    - _Unabhängiges Zielportal verwenden wenn Multipath I/O aktiviert ist._
- [select] **Unabhängigen Zielnamen verwenden** — MAC-Adresse / Permanente MAC-Adresse★
- [select] **iSCSI ファースト ターゲット パラメタを設定する。** — iSCSI セカンド ターゲット パラメタ
    - _iSCSI セカンド ターゲット パラメタ_
- [select] **セカンダリ デバイス MAC アドレス** — MAC アドレス / 固定 MAC アドレス★
    - _独立したターゲット ポータルを使用_
- [select] **独立したターゲット ポータルを使用** — MAC アドレス / 固定 MAC アドレス★
    - _multipath I/O がイネーブルな場合、独立したターゲット ポータルを使用する。_
- [select] **独立したターゲット名を使用** — MAC アドレス / 固定 MAC アドレス★
- [select] **Configurar parámetros de primer destino de iSCSI.** — Parámetros de segundo destino de iSCSI
    - _Parámetros de segundo destino de iSCSI_
- [select] **Dirección MAC de dispositivo secundario** — Dirección MAC / Dirección MAC permanente★
    - _Utilizar portal de destino independiente_
- [select] **Utilizar portal de destino independiente** — Dirección MAC / Dirección MAC permanente★
    - _Utilizar portal de destino independiente cuando esté habilitada la E/S de múltiples rutas._
- [select] **Utilizar nombre de destino independiente** — Dirección MAC / Dirección MAC permanente★
- [select] **Configurer les paramètres de la première cible iSCSI.** — Paramètres de la deuxième cible iSCSI
    - _Paramètres de la deuxième cible iSCSI_
- [select] **Adresse MAC du périphérique secondaire** — Adresse MAC / Adresse MAC permanente★
    - _Utiliser le portail cible indépendant_
- [select] **Utiliser le portail cible indépendant** — Adresse MAC / Adresse MAC permanente★
    - _Utiliser le portail cible indépendant lorsque les E/S multivoies sont activées._
- [select] **Utiliser le nom de cible indépendante** — Adresse MAC / Adresse MAC permanente★
- [select] **Configure iSCSI first target parameters.** — iSCSI Second Target Parameters
    - _iSCSI Second Target Parameters_
- [select] **Secondary Device MAC Address** — MAC Address / Permanent MAC Address★
    - _Use Independent Target Portal_
- [select] **Use Independent Target Portal** — MAC Address / Permanent MAC Address★
    - _Use independent target portal when multipath I/O is enabled._
- [select] **Use Independent Target Name** — MAC Address / Permanent MAC Address★
- [select] **Initiator** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★

## ￱您確定￰? (Y/N)  (1 settings)

- [toggle] **￱變更已儲存￰**

## +/- =￱調整值￰  (10 settings)

- [select] **￱請輸入新密碼￰**
    - _￱請確認新密碼￰_
- [select] **￱密碼不相同￰**
    - _￱密碼錯誤￰_
- [select] **￱按下￰Enter/ESC ￱離開￰** — ￱按下￰PageDown  ￱下一頁￰★
    - _￱按下￰PageUp    ￱上一頁￰_
- [select] **Setup Warning** — ￱變更已儲存￰★ / [￱繼續￰]
    - _￱設定通知￰_
- [select] **Esc=Exit Menu**
    - _F10=Save and Exit_
- [select] **￱無效的密碼￰!￱請重輸設定密碼￰**
    - _￱離開並儲存設定￰_
- [select] **￱確定￰**
    - _￱取消￰_
- [select] **￱是￰**
    - _￱否￰_
- [select] **Press 'Y' to save and exit, 'N' to discard and exit.**
    - _￱系微設置工具￰_
- [select] **￱按￰ENTER￱以繼續￰**
    - _￱請輸入您的資料￰_

## =￱移動反白項￰  (1 settings)

- [toggle] **<￱空白鍵￰>￱勾選查核方塊￰**
    - _￱請輸入密碼￰_

## Broadcom NetXtreme Gigabit Ethernet  (40 settings)

- [select] **Etat de la liaison** — PXE★ / iSCSI
    - _Connecté_
- [select] **Déconnecté** — PXE★ / iSCSI
    - _Clignotement des voyants_
- [select] **Fait clignoter les voyants pendant une durée de 15 secondes.** — PXE★ / iSCSI
    - _Protocole de démarrage hérité_
- [select] **Prise en charge du déchargement iSCSI** — PXE Boot Support★ / Prise en charge de l'initialisation FCoE
    - _Prise en charge de l'initialisation iSCSI_
- [select] **Prise en charge du partitionnement NIC** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _AdressageFlex_
- [number] **Maximale pour contrôle de la bande passante TX**
    - _Minimale pour contrôle de la bande passante TX_
- [number] **xxxxxxxxx-Bus:Pér:Fcn**
    - _Port TCP non valide_
- [number] **ID de VLAN non valide**
    - _Désactiver la fonction de mémoire partagée HP_
- [select] **iSCSI オフロード サポート** — PXE Boot Support★ / FCoE ブート サポート
    - _iSCSI ブート サポート_
- [select] **NIC パーティション化サポート** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _FlexAddressing_
- [number] **TX 帯域幅コントロール最大**
    - _TX 帯域幅コントロール最小_
- [number] **xxxxxxxxx-バス：デバイス：機能**
    - _無効な TCP ポート_
- [number] **無効な VLAN ID**
    - _HP共有メモリ機能を無効にします_
- [select] **Link Status** — PXE★ / iSCSI
    - _Connected_
- [select] **Disconnected** — PXE★ / iSCSI
    - _Blink LEDs_
- [select] **Blink LEDs for a duration up to 15 seconds.** — PXE★ / iSCSI
    - _Legacy Boot Protocol_
- [select] **Estado del enlace** — PXE★ / iSCSI
    - _Conectado_
- [select] **Desconectado** — PXE★ / iSCSI
    - _LED intermitentes_
- [select] **LED intermitentes con una duración de hasta 15 segundos.** — PXE★ / iSCSI
    - _Protocolo de arranque heredado_
- [select] **Soporte de descarga iSCSI** — PXE Boot Support★ / Compatibilidad con arranque FCoE
    - _Compatibilidad con arranque iSCSI_
- [select] **Compatibilidad con partición NIC** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Dirección flexible_
- [number] **Control de banda ancha TX máximo**
    - _Control de banda ancha TX mínimo_
- [number] **xxxxxxxxx-Bus:Dis:Fcn**
    - _Puerto TCP no válido_
- [number] **ID de VLAN no válido**
    - _Desactivar función de memoria compartida de HP_
- [select] **iSCSI-Offload-Support** — PXE Boot Support★ / FCoE-Boot-Support
    - _iSCSI-Boot-Support_
- [select] **NIC-Partitionierung Support** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _FlexAddressing_
- [number] **TX-Bandbreitensteuerung – Maximum**
    - _TX-Bandbreitensteuerung – Minimum_
- [number] **xxxxxxxxx-Bus:Ger:Fcn**
    - _Ungültiger TCP-Port_
- [number] **Ungültige VLAN-ID**
    - _HP Shared-Memory-Funktion deaktivieren_
- [select] **リンク ステータス** — PXE★ / iSCSI
    - _接続完了_
- [select] **切断完了** — PXE★ / iSCSI
    - _LED を点滅させる_
- [select] **LED を最大 15 秒点滅させる。** — PXE★ / iSCSI
    - _旧式ブート プロトコル_
- [select] **iSCSI Offload Support** — PXE Boot Support★ / FCoE Boot Support
    - _iSCSI Boot Support_
- [select] **NIC Partitioning Support** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$
    - _FlexAddressing_
- [number] **TX Bandwidth Control Maximum**
    - _TX Bandwidth Control Minimum_
- [number] **xxxxxxxxx-Bus:Dev:Fcn**
    - _Invalid TCP Port_
- [number] **Invalid VLAN ID**
    - _Disable HP Shared Memory features_
- [select] **Verbindungsstatus** — PXE★ / iSCSI
    - _Verbunden_
- [select] **Verbindung getrennt** — PXE★ / iSCSI
    - _Blinkende LEDs_
- [select] **Blinkende LEDs für bis zu 15 Sekunden** — PXE★ / iSCSI
    - _Bootprotokolle älterer Geräte_

##    (55 settings)

- [toggle] **Secure Boot Mode**
    - _Setup Mode_
- [toggle] **User Mode**
- [select] **Special Display Features** — HybridGraphics★ / Discrete GPU Hotplug Mode / Select Discrete GPU Hotplug Mode - HotplugEnhanced or HotplugBasic
    - _Enable/Disable HybridGraphics_
- [select] **Non-Eval Discrete GPU Support** — Select Discrete GPU Hotplug Mode - HotplugEnhanced or HotplugBasic / Discrete GPU Hotplug Mode / HybridGraphics★
    - _Enable to support Non-Eval Discrete GPU that doesn't have specific EVAL_PWRGD(A5), EVAL_PRESENT#(B30)_
- [select] **Discrete GPU D3Cold HPD Support** — PME Turn Off Support / Enable to support sending PME_Turn_Off message to Discrete GPU when going to D3Cold / HybridGraphics★
    - _Enable/Disable Discrete GPU D3Cold HPD function_
- [select] **Discrete GPU HPD Circuitry** — OR Circuitry / HybridGraphics★
    - _Enable/Disable Discrete GPU Display HPD Circuitry_
- [select] **Pulse Circuitry** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _Discrete GPU's Audio_
- [select] **Keep ROM Strap Setting** — Enable/Disable Discrete GPU BOMACO Support★ / MACO-PWR Timing   (us) / MACO-PWR Timing: MACO_EN assert to PWR_EN deassert
    - _Discrete GPU BOMACO Support_
- [select] **PWRON-RST Timing  (ms)** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _PWRON-RST Timing: PWR_EN assert to PERSTb deassert_
- [select] **RST-MACO Timing   (ms)** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _RST-MACO Timing: PERSTb deassert to MACO_EN deassert_
- [select] **Secure Boot Status** — Unlocked / YES★
    - _User Customized Security_
- [select] **NO**
    - _Options:_
- [select] **Enforce Secure Boot** — Unlocked★ / Setup Mode
    - _Select Disable to Suspend enforcement of Secure Boot Checks._
- [select] **Erase all Secure Boot Settings** — Unlocked / Setup Mode★
    - _Enable this option will erase all Secure Boot Settings. This action will clear four variables PK, KEK, db, and dbx._
- [select] **Select a UEFI file as trusted for execution** — Unlocked★ / Setup Mode
    - _Add sepecific EFI image hash to allowed database._
- [select] **Restore Secure Boot to Factory Settings** — Restore Secure Boot to Backup Settings★ / Restore all of the secure boot Settings to backup factory settings and enable Secure Boot.
    - _Restore all of the Secure Boot Settings to default factory settings and enable Secure Boot._
- [select] **Désactiver** — Unlocked★ / Operation is completed. System will reset!!
    - _Activer_
- [select] **This isn't a vaild EFI image. Please select another file!!** — Unlocked★ / Setup Mode
    - _Add this hash image to allowed database (db)_
- [number] **Exit Discarding Change**
    - _Exit saving changes_
- [number] **Cannot find file!!**
    - _File size is too large!!_
- [number] **File format is incorrect!!**
    - _Select Secure Mode_
- [number] **Select different secure boot mode. User can select one of 4 different modes (Setup Mode, User Mode, Audit mode and Deployed mode).**
- [select] **Delete PK** — Unlocked / Setup Mode★
    - _Enter into Delete PK Form_
- [select] **Disabled** — Unlocked★ / Operation is completed. System will reset!!
    - _Enabled_
- [select] **Enroll/Delete PK** — Enroll PK★ / Enroll PK Using File
    - _PK Signature List:_
- [select] **KEK Options** — Unlocked / Setup Mode★
    - _Enroll/Delete KEK_
- [select] **KEK Signature List:** — Enroll KEK Using File★ / Delete KEK
    - _Enroll KEK_
- [select] **Enter into Delete KEK Form** — Enroll/Delete Signature★ / DB Signature List:
    - _DB Options_
- [select] **DBX Options** — DBX Signature List: / Enroll Signature★ / Delete Signature
    - _Enroll/Delete DBX_
- [select] **Unknown** — Unlocked★ / Setup Mode
    - _RSA2048_SHA256_
- [select] **SHA256** — Unlocked★ / Setup Mode
    - _SHA512_
- [select] **PKCS7** — Unlocked / Setup Mode★ / Installed and Locked
    - _SHA1_
- [select] **X509_SHA256** — Unlocked / Setup Mode★
    - _X509_SHA384_GUID_
- [select] **X509_SHA512_GUID** — Unlocked★ / Setup Mode
    - _Select Signature Format_
- [select] **Delete this signature** — Unlocked / Setup Mode★
    - _[Error] PK already exists._
- [select] **[Error] There is already an identical signature in signature list.** — Unlocked / Setup Mode★
    - _[Error] Invalid GUID string. GUID string should be in 12345678-1234-1234-1234-1234567890ab format._
- [select] **Input Owner_GUID in 12345678-1234-1234-1234-1234567890ab format.** — Unlocked / Setup Mode★
    - _The operation is only allowed before booting any boot device!!! Please reset system and enter this menu directly if need use this operation._
- [select] **Press Esc for boot options** — Unlocked / Setup Mode★
    - _Esc is pressed. Go to boot options._
- [number] **Restore all of the Secure Boot Settings to default factory settings and enable Secure Boot.**
    - _Restore Secure Boot to Backup Settings_
- [select] **Restore all of the secure boot Settings to backup factory settings and enable Secure Boot.** — Enabled★ / Operation is completed. System will reset!! / Activer
    - _Disabled_
- [select] **Modify next boot behavior** — Set Legacy HardDisk Drive Order★ / Set Legacy CD-ROM Drive Order
    - _Set Time Out Value_
- [select] **Modify automatic boot time-out value** — Set Legacy HardDisk Drive Order★ / Set Legacy CD-ROM Drive Order
    - _Console Options_
- [select] **Modify system console options** — Set Legacy HardDisk Drive Order★ / Set Legacy CD-ROM Drive Order
    - _Console Input Device Select_
- [select] **HDD : ** — [Invoke] / Use <↑> or <↓> to select a device, then press <F6> to move it up the list, or <F5> to move it down the list. Press <Esc> to escape the menu / UEFI★ / Revert OPAL Device / The available boot devices will not change until a reboot!
    - _HDD%d : _
- [select] **AHCI** — USB Boot:★ / ASF Support:
    - _RAID_
- [toggle] **ASF Support**
    - _ASF Configuration_
- [select] **AMD-IOMMU:** — AMD-SVM: / This is AMD Secure Virtual Machine function switch★ / Revert OPAL Device / The available boot devices will not change until a reboot!
    - _This is AMD virtualization function switch_
- [toggle] **Enables you to charge mobile devices when your computer is off or in Sleep mode.**
    - _ Battery Threshold:_
- [toggle] **Set a computer battery charge limit, below which charging stops.**
    - _10%_
- [toggle] **20%**
    - _30%_
- [toggle] **Intel VTX:**
    - _This is Intel VTX function switch_
- [toggle] **Intel VTD:**
    - _This is Intel VTD function switch_
- [toggle] **CPU Speed:** — CPU Speed:★
- [select] **Lid Open Resume** — Video Memory: / [Not Detected]★
    - _System will resume from S3 state by Lid open._
- [select] **PS2** — [Media Key]: Perform the media function by default. Hold the <Fn> key to activate F1 to F12. [Function Key]: Activate F1 to F12 by default, Hold the <Fn> key to perform media function. / Function Key / Media Key★
    - _Function key behavior:_

## DAD Transmit Count  (3 settings)

- [select] **Manual IP address can only be configured under manual policy. Separate the IP address with blank space to configure more than one address. e.g. 2002::1/64 2002::2/64**
    - _New Gateway addresses_
- [select] **Gateway IP address can only be configured under manual policy. e.g. 2002::3. Separate the IP address with blank space to configure more than one address.**
    - _New DNS addresses_
- [select] **DNS addresses can only be configured under manual policy. e.g. 2002::4. Separate the IP address with blank space to configure more than one address.**
    - _Save Changes and Exit_

## HybridGraphics  (1 settings)

- [select] **0** — Manual / Enabled ★
    - _USB PD Section 1 FW Version_

## VDD18 voltage (ANPEC:+130mv/TI:+137.5mv)  (1 settings)

- [select] **VDD18 voltage (ANPEC:-50mv/TI:-37.5mv)** — Manual / VDD18 voltage (ANPEC:-70mv/TI:-62.5mv) / VDD18 voltage (ANPEC:-80mv/TI:-75mv) / VDD18 voltage (ANPEC:-90mv/TI:-87.5mv)★ / VDD18 voltage (ANPEC:-100mv/TI:-100mv) / Enabled (x4)
    - _VDD18 voltage (ANPEC:-60mv/TI:-50mv)_

## VDD18 voltage (ANPEC:-110mv/TI:-112.5mv)  (1 settings)

- [select] **StallForUnlock** — Manual / Enabled ★
    - _StallForUnlock Enable/Disable_

## VDD18 voltage (ANPEC:-130mv/TI:-137.5mv)  (1 settings)

- [select] **StallForUnlock** — Manual / Enabled ★
    - _StallForUnlock Enable/Disable_

## 5V_S5 voltage setting for ANPEC PSA  (7 settings)

- [select] **StallForUnlock** — Manual / Enabled ★
    - _StallForUnlock Enable/Disable_
- [number] **Show all of AMD Firmware Version**
- [select] **35bit (32GB)** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support.★
    - _36bit (64GB)_
- [number] **Enable to support sending PME_Turn_Off message to Discrete GPU when going to D3Cold**
    - _Discrete GPU HPD Circuitry_
- [select] **Select Internal/External Graphics** — SATA D3cold Enable / Ext Graphics (PEG)
    - _Int Graphics (IGD)_
- [select] **PWRON-RST Timing: PWR_EN assert to PERSTb deassert** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support.
    - _RST-MACO Timing   (ms)_
- [select] **Enable to support Non-Eval Discrete GPU that doesn't have specific EVAL_PWRGD(A5), EVAL_PRESENT#(B30)** — PME Turn Off Support / Enable/Disable Discrete GPU D3Cold HPD function
    - _Discrete GPU D3Cold HPD Support_

## 5v_ALW +60mv  (1 settings)

- [select] **StallForUnlock** — Manual / Enabled ★
    - _StallForUnlock Enable/Disable_

## AMD KVM Mouse Protocol  (1 settings)

- [select] **StallForUnlock** — Manual / Enabled ★
    - _StallForUnlock Enable/Disable_

## Absolute  (1 settings)

- [select] **StallForUnlock** — Manual / Enabled ★
    - _StallForUnlock Enable/Disable_

## AMD DPTC interface  (1 settings)

- [select] **StallForUnlock** — Manual / Enabled ★
    - _StallForUnlock Enable/Disable_

## Non-Eval Discrete GPU Support  (3 settings)

- [select] **D3Cold Support** — Disabled★ / Enabled (x1) (Lane 0)
    - _Enable/Disable PCIe x8 Slot D3Cold_
- [select] **UCSI tunnel location** — Manual★ / Enabled 
    - _UCSI tunnel can be put on ECRAM or MMIO space, this option specify which one is selected._
- [select] **UCSI Support** — Manual★ / Enabled 
    - _Enable/Disable UCSI (USB Type-C Connector System Software Interface)_

## Discrete GPU D3Cold HPD Support  (2 settings)

- [select] **0** — Manual / SMU RV2 FW Version / MP2 FW Version★ / DXIO FW Version / 0 / Enabled 
    - _ABL Version_
- [select] **S3 Enable** — Manual / Enabled (x4)★
    - _Modern Standby Enable_

## PME Turn Off Support  (6 settings)

- [select] **VDD18 voltage (ANPEC:+90mv/TI:+87.5mv)** — Manual / Enabled (x4)★
    - _VDD18 voltage (ANPEC:+100mv/TI:+100mv)_
- [select] **Auto: USB interrupt resource is controlled automatically; Enable: Enable USB current resource for MS; Disable: Disable USB current resource for MS.** — Reduce Hardware Support / Wake on PME★
    - _Turn Unused GPP Clocks Off_
- [select] **Modern Standby + S0i2 + S0i3** — Enable/Disable SATA devies D3-COLD support.★ / MS Resource
    - _SATA D3cold Enable_
- [select] **Clock PM: CLK_REQ0** — Manual★ / Enabled 
    - _Enable or disable CLK_REQ0# for M.2 WLAN Slot J3711_
- [select] **Clock PM: CLK_REQ1** — Manual / Enabled ★
    - _Enable or disable CLK_REQ1# for Onboard LAN U1301_
- [select] **Clock PM: CLK_REQ2** — Manual / Enabled ★
    - _Enable or disable CLK_REQ2# for M.2 WWAN Slot J3712_

## Discrete GPU HPD Circuitry  (2 settings)

- [select] **GPIO 11 Output High** — Manual / Enabled ★
    - _Serial Debug Message Under OS_
- [select] **Enable Serial Debug Message Under OS** — Show all of AMD Firmware Version / AGESA Version★
    - _AMD Firmware Version_

## OR Circuitry  (10 settings)

- [select] **VDD18 voltage (ANPEC:+70mv/TI:+62.5mv)** — Manual / Enabled ★
    - _VDD18 voltage (ANPEC:+80mv/TI:+75mv)_
- [select] **DT Hotplug Enable** — Enabled  / HDMI over USB-C1★
    - _Enable or Disable DT Hotplug, it uses EC DOCK_IN# pin as plug-in event._
- [select] **DT Hotplug Mode** — Manual / Enabled ★ / Enhanced Mode
    - _Select DT Hotplug Mode - DxioHotplugEnhanced or DxioHotplugBasic_
- [select] **WWAN Power Enable** — Manual / Enabled ★
    - _Enable or disable the power of WWAN_
- [select] **VDDP voltage (-100mv)** — Manual / Enabled ★
    - _VDD18 voltage_
- [select] **VDD18 voltage  Setting.** — Manual / Enabled ★
- [select] **VDD18 voltage (1.8V)** — Manual / Enabled ★
- [select] **VDD18 voltage (ANPEC:+40mv/TI:+25mv)** — Manual / Enabled ★
- [select] **VDD18 voltage (ANPEC:+50mv/TI:+37.5mv)** — Manual / Enabled ★
- [select] **VDD18 voltage (ANPEC:+60mv/TI:+50mv)** — Manual / Enabled ★

## Discrete GPU's Audio  (2 settings)

- [select] **DT Slot Power Enable** — Eval Auto Detection / Disable or enable EVAL card auto detection★ / Touch Panel Support / Enable/Disable exposing of _HID(PNP0C50) in ACPI ASL code to OS / Touch Pad Support / Nfc Support / Enable/Disable exposing of _HID(BCM2F25) in ACPI ASL code to OS
    - _Enable or disable the power of DT SLOT_
- [toggle] **Enable/Disable Discrete GPU BOMACO Support**
    - _MACO-PWR Timing   (us)_

## Keep ROM Strap Setting  (6 settings)

- [select] **Under I2C 0 Bus** — Manual / Enabled ★
    - _Under I2C 1 Bus_
- [select] **Under I2C 2 Bus** — Manual / Enabled ★
    - _Under I2C 3 Bus_
- [select] **ELAN TSP Under I2C 0 Bus** — Manual / Enabled ★
    - _ELAN TSP Under I2C 1 Bus_
- [select] **ELAN TSP Under I2C 2 Bus** — Manual / Enabled ★
    - _ELAN TSP Under I2C 3 Bus_
- [select] **Manual by jumper** — Manual / Enabled ★
    - _HDMI over USB-C0_
- [select] **SW BreakPoint for S3 Enable/Disable** — Manual / Enabled ★
    - _BLINK LED_

## VDD18 voltage (ANPEC:+110mv/TI:+112.5mv)  (4 settings)

- [select] **HDT BreakPoint for Boot** — Enabled (x4)★ / SW BreakPoint for S3
    - _HDT BreakPoint for Boot Enable/Disable_
- [select] **VDDP voltage (+50mv)** — Manual / Enabled ★
    - _VDDP voltage (+60mv)_
- [select] **VDDP voltage (+70mv)** — Manual / Enabled ★
    - _VDDP voltage (+80mv)_
- [select] **VDDP voltage (+90mv)** — Manual / Enabled ★
    - _VDDP voltage (+100mv)_

## Devices List  (5 settings)

- [select] **Network Device List** — Select the network device according the MAC address / Primary Video BIOS★
    - _Network Device_
- [toggle] **Network Device**
- [select] **Set primary video BIOS**
    - _PCI_
- [select] **Esc is pressed. Go to boot options.** — Select the network device according the MAC address★ / Press ESC to exit.
- [select] **AGP** — Select the network device according the MAC address★ / Press ESC to exit.
    - _Press Esc for boot options_

## Device Manager  (1 settings)

- [select] **Esc is pressed. Go to boot options.**

## EFI DVD/CDROM  (1 settings)

- [number] **EFI Network**

## EFI Hard Drive  (12 settings)

- [number] **% of the system memory tested OK**
    - _Boot Succeeded - _
- [select] ** has been blocked by the current security policy.** —  boot failed.★ / Execution of the selected file boot failed.
    - _Execution of the selected file has been blocked by the current security policy._
- [select] **V1.12** — EFI Network / 05.32.42★
    - _FH50P_
- [select] **BIOS Version**
    - _BIOS Build Date_
- [select] **Do you want to recovery ROM part? (Caution: Not every OS is bootable in Recovery Mode.)** — EFI Network★ / EFI ISCSI Device
    - _Flash Status_
- [select] **YES,this choice will flash Rom part.** — EFI Network / EFI ISCSI Device★
    - _NO, abort Recovery mode and restart system._
- [select] **Processor Type** — EFI Network★ / EFI ISCSI Device
    - _System Memory Speed_
- [select] **Rebooting !** — Boot Succeeded - ★ /  has been blocked by the current security policy.
    - _% of the system memory tested OK_
- [select] **Execution of the selected file has been blocked by the current security policy.** — EFI Network★ / Execution of the selected file boot failed.
    - _ boot failed._
- [select] **Press Esc for boot options** — EFI Network★ / EFI ISCSI Device
    - _Esc is pressed. Go to boot options._
- [toggle] **EFI SCSI Device**
    - _EFI ISCSI Device_
- [toggle] **EFI SD/MMC Card**

## Realtek Ethernet Controller Configuration  (53 settings)

- [number] **Realtek UEFI UNDI driver information**
    - _Driver Name:_
- [select] **%s** — %s★ / Driver Released Date: / 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.
    - _Driver Version:_
- [select] **10 Mpbs HALF Duplex** — 100 Mpbs Half Duplex / Disabled★
    - _Enabled_
- [select] **Save RealManage Configuration** — Hash5 Value / Set or change DASH fifth PKI hash value★
    - _Save RealManage Configuration to NvRam_
- [select] **Configuration Menu** — 100 Mpbs Half Duplex★ / Change link speed and duplex for current adapter.
    - _Advanced Settings_
- [select] **Configure Realtek ethernet controller parameter** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
- [select] **Exit RealManage Setup** — 100 Mpbs Half Duplex★ / Change link speed and duplex for current adapter.
- [select] **Driver Information** — Driver Name:★ / %s
    - _Realtek UEFI UNDI driver information_
- [select] **Driver Version:** — 100 Mpbs Half Duplex★ / Driver Released Date:
    - _%s_
- [number] **Device Name:**
    - _%s_
- [number] **MAC Address:**
    - _Current network address_
- [number] **%02x:%02x:%02x:%02x:%02x:%02x**
    - _PCI Slot:_
- [number] **The PCI address of Realtek ethernet controller**
    - _%02d:%02d:%02d_
- [select] **Driver Provider:** — Patent Information★ / This product is covered by one or more of the following patents:
    - _%s_
- [select] **FQDN** — 100 Mpbs Half Duplex★
    - _Set or change DASH PKI FQDN_
- [select] **PKI DNS Suffix** — 100 Mpbs Half Duplex★
    - _Set or change DASH PKI DNS suffix_
- [select] **Please Enter Username & Password** — 100 Mpbs Half Duplex★
    - _Please Input Password_
- [select] **Set or change DASH PSK PPS** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _TLS PKI_
- [select] **Manage Certificate Hashes** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Configure DASH PKI hash tables_
- [select] **Certificate Hash1 for PKI** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Affirmative or negative DASH first PKI hash value_
- [select] **Hash1 Value** — 100 Mpbs Half Duplex / Certificate Hash2 for PKI★ / Affirmative or negative DASH second PKI hash value
    - _Set or change DASH first PKI hash value_
- [select] **Hash4 Value** — 100 Mpbs Half Duplex★ / Change link speed and duplex for current adapter.
    - _Set or change DASH forth PKI hash value_
- [select] **Certificate Hash5 for PKI** — Hash5 Value / Set or change DASH fifth PKI hash value★
    - _Affirmative or negative DASH fifth PKI hash value_
- [select] **Certificate Hash6 for PKI** — 100 Mpbs Half Duplex★ / Auto Negotiation / 1.0 Gbps Full Duplex / 100 Mpbs Full Duplex
    - _Affirmative or negative DASH sixth PKI hash value_
- [select] **Hash3 Value** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★ / Link Speed & Duplex
    - _Set or change DASH third PKI hash value_
- [select] **Un-Provisioned** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Prepared Provisioned_
- [select] **Modify password** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Set or change DASH password_
- [select] **TLS PSK** — 100 Mpbs Half Duplex★ / Change link speed and duplex for current adapter.
    - _PID for PSK_
- [select] **Certificate Hash4 for PKI** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★ / Link Speed & Duplex
    - _Affirmative or negative DASH forth PKI hash value_
- [select] **Hash6 Value** — 100 Mpbs Half Duplex★ / Change link speed and duplex for current adapter.
    - _Set or change DASH sixth PKI hash value_
- [select] **Hash2 Value** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Set or change DASH second PKI hash value_
- [select] **Certificate Hash3 for PKI** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Affirmative or negative DASH third PKI hash value_
- [select] **Configure DASH(Desktop and Mobile Architecture for System Hardware) setting. DASH is a web services-based standard that can support both in-band and out-of-band management.** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Realtek RealManage Setup_
- [select] **Host Configuration** — Host Configuration★ / TCP/IP Configuration
    - _Configure DASH host settings_
- [select] **Configure DASH TCP/IP settings** — Provisioning Model★ / Configure DASH provision settings
    - _TCP/IP Configuration_
- [select] **Provisioning Model** — Configure DASH security settings / Setup and Configuration★ / Host Name
    - _Setup and Configuration_
- [select] **Set or change DASH host name** — 100 Mpbs Half Duplex★ / Change link speed and duplex for current adapter.
    - _Domain Name_
- [select] **Enable or Disble DASH DHCP service** — 100 Mpbs Half Duplex★ / Change link speed and duplex for current adapter.
    - _OOBip_
- [select] **Set or change DASH domain name** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★ / 10 Mpbs Full Duplex
    - _DHCPv4_
- [select] **Set or change DASH IP** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Subnetmask_
- [select] **Set or change DASH subnetmask** — 100 Mpbs Half Duplex★ / Change link speed and duplex for current adapter.
    - _Gateway_
- [select] **Security Configuration** — Configure DASH account settings / Modify username / Set or change DASH username★
- [select] **Set or change DASH gateway** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _DNS_
- [select] **Set or change DASH DNS** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Echoservice_
- [select] **Enable or Disble DASH Echoservice** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Provision Mode_
- [select] **Change DASH provision mode. Provision mode support Enterprise/Small business** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Provision State_
- [select] **Change DASH provision state. Provision state support Un-provisioned/Prepared provision/Provisioned** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Provision ServerIP_
- [select] **Set or change DASH provision server IP** — 100 Mpbs Half Duplex★ / Change link speed and duplex for current adapter.
    - _Provision Port_
- [select] **Set or change DASH provision port** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _Enterprise_
- [select] **Small Business** — 100 Mpbs Half Duplex★ / Change link speed and duplex for current adapter.
    - _Provisioned_
- [select] **Set or change DASH PSK PID** — 100 Mpbs Half Duplex / Change link speed and duplex for current adapter.★
    - _PPS for PSK_
- [toggle] **Link Speed & Duplex**
    - _Change link speed and duplex for current adapter._
- [toggle] **Auto Negotiation**

## TCP/IP Configuration  (2 settings)

- [select] **DHCPv4** — Disabled★ / Enabled
    - _Enable or Disble DASH DHCP service_
- [select] **Echoservice** — Disabled★ / Enabled
    - _Enable or Disble DASH Echoservice_

## Manage Certificate Hashes  (6 settings)

- [select] **Certificate Hash1 for PKI** — Disabled★ / Enabled
    - _Affirmative or negative DASH first PKI hash value_
- [select] **Certificate Hash2 for PKI** — Disabled★ / Enabled
    - _Affirmative or negative DASH second PKI hash value_
- [select] **Certificate Hash3 for PKI** — Disabled★ / Enabled
    - _Affirmative or negative DASH third PKI hash value_
- [select] **Certificate Hash4 for PKI** — Disabled★ / Enabled
    - _Affirmative or negative DASH forth PKI hash value_
- [select] **Certificate Hash5 for PKI** — Disabled★ / Enabled
    - _Affirmative or negative DASH fifth PKI hash value_
- [select] **Certificate Hash6 for PKI** — Disabled★ / Enabled
    - _Affirmative or negative DASH sixth PKI hash value_

## AMD PBS Option  (76 settings)

- [number] **Enable/Disable Discrete GPU Display HPD Circuitry**
    - _OR Circuitry_
- [select] **Pulse Circuitry** — Disable Discrete GPU's Audio or keep its ROM strap setting★ / Keep ROM Strap Setting
    - _Discrete GPU's Audio_
- [toggle] **Manual**
    - _Enabled _
- [toggle] **Enabled (x4)**
- [select] **Special Display Features** — Disabled / HybridGraphics★
    - _Enable/Disable HybridGraphics_
- [select] **D3Cold Support** — Disabled / Enabled ★
    - _Enable/Disable PCIe x8 Slot D3Cold_
- [select] **NVIDIA DGPU Power Enable** — Disabled★ / Enabled 
    - _For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state._
- [select] **Discrete GPU Hotplug Mode** — Basic Mode / Enhanced Mode★
    - _Select Discrete GPU Hotplug Mode - HotplugEnhanced or HotplugBasic_
- [select] **Discrete GPU D3Cold HPD Support** — Disabled★ / Enabled 
    - _Enable/Disable Discrete GPU D3Cold HPD function_
- [select] **PME Turn Off Support** — Disabled / Enabled ★
    - _Enable to support sending PME_Turn_Off message to Discrete GPU when going to D3Cold_
- [select] **Non-Eval Discrete GPU Support** — Disabled★ / Enabled 
    - _Enable to support Non-Eval Discrete GPU that doesn't have specific EVAL_PWRGD(A5), EVAL_PRESENT#(B30)_
- [select] **Discrete GPU HPD Circuitry** — OR Circuitry★ / Pulse Circuitry
    - _Enable/Disable Discrete GPU Display HPD Circuitry_
- [select] **Discrete GPU's Audio** — Disabled★ / Keep ROM Strap Setting
    - _Disable Discrete GPU's Audio or keep its ROM strap setting_
- [select] **Discrete GPU BOMACO Support** — Disabled★ / Enabled 
    - _Enable/Disable Discrete GPU BOMACO Support_
- [number] **MACO-PWR Timing   (us)**
    - _MACO-PWR Timing: MACO_EN assert to PWR_EN deassert_
- [number] **PWROFF-RST Timing (ms)**
    - _PWROFF-RST Timing: PWR_EN deassert to PERSTb assert_
- [number] **PWRON-RST Timing  (ms)**
    - _PWRON-RST Timing: PWR_EN assert to PERSTb deassert_
- [number] **RST-MACO Timing   (ms)**
    - _RST-MACO Timing: PERSTb deassert to MACO_EN deassert_
- [select] **Primary Video Adaptor** — Int Graphics (IGD)★ / Ext Graphics (PEG)
    - _Select Internal/External Graphics_
- [select] **Above 4GB MMIO Limit** — 35bit (32GB) / 36bit (64GB) / 37bit (128GB) / 38bit (256GB) / 39bit (512GB) / 40bit (1TB)★ / 41bit (2TB) / 42bit (4TB) / 43bit (8TB) / 44bit (16TB) / 45bit (32TB) / 46bit (64TB) / 47bit (128TB) / 48bit (256TB)
    - _Select Above 4GB MMIO Limit to 35~48bits limit._
- [select] **StallForUnlock** — Disabled★ / Enabled 
    - _StallForUnlock Enable/Disable_
- [select] **HDT BreakPoint for Boot** — Disabled★ / Enabled 
    - _HDT BreakPoint for Boot Enable/Disable_
- [select] **SW BreakPoint for S3** — Disabled★ / Enabled 
    - _SW BreakPoint for S3 Enable/Disable_
- [select] **Touch Panel Support** — Disabled★ / Under I2C 0 Bus / Under I2C 1 Bus / Under I2C 2 Bus / Under I2C 3 Bus / ELAN TSP Under I2C 0 Bus / ELAN TSP Under I2C 1 Bus / ELAN TSP Under I2C 2 Bus / ELAN TSP Under I2C 3 Bus
    - _Enable/Disable exposing of _HID(PNP0C50) in ACPI ASL code to OS_
- [select] **Touch Pad Support** — Disabled★ / Under I2C 0 Bus / Under I2C 1 Bus / Under I2C 2 Bus / Under I2C 3 Bus
    - _Enable/Disable exposing of _HID(PNP0C50) in ACPI ASL code to OS_
- [select] **Nfc Support** — Disabled★ / Under I2C 0 Bus / Under I2C 1 Bus / Under I2C 2 Bus / Under I2C 3 Bus
    - _Enable/Disable exposing of _HID(BCM2F25) in ACPI ASL code to OS_
- [select] **ALS Support** — Disabled★ / Under I2C 0 Bus / Under I2C 1 Bus / Under I2C 2 Bus / Under I2C 3 Bus
    - _Enable/Disable exposing of _HID(CPLM3218) in ACPI ASL code to OS_
- [select] **HDMI over USB-C0** — Native USB Type-C★ / HDMI over USB Type-C
    - _Force HDMI signals route over USB Type C port_
- [select] **HDMI over USB-C1** — Native USB Type-C★ / HDMI over USB Type-C
    - _Force HDMI signals route over USB Type C port_
- [select] **HDD Power Enable** — Disabled / Enabled ★ / Manual by jumper
    - _Enable or disable the power of HDD_
- [select] **ODD Power Enable** — Disabled / Enabled ★
    - _Enable or disable the power of ODD_
- [select] **Zero-Power ODD** — Disabled / Enabled ★
    - _Enable/Disable Zero-Power ODD Feature_
- [select] **SSD Power Enable** — Disabled / SSD x2★ / SSD x4
    - _Enable or disable the power of SSD_
- [select] **Serial Debug Message Under OS** — Disabled★ / Enabled 
    - _Enable Serial Debug Message Under OS_
- [select] **DT Hotplug Enable** — Disabled★ / Enabled 
    - _Enable or Disable DT Hotplug, it uses EC DOCK_IN# pin as plug-in event._
- [select] **DT Hotplug Mode** — Basic Mode / Enhanced Mode★
    - _Select DT Hotplug Mode - DxioHotplugEnhanced or DxioHotplugBasic_
- [select] **DT Slot Power Enable** — Disabled★ / Enabled (x4) / Enabled (x2) (Lane 0 + 1) / Enabled (x1) (Lane 0)
    - _Enable or disable the power of DT SLOT_
- [select] **WLAN/WIFI Power Enable** — Disabled / Enabled ★ / Manual
    - _Enable or disable the power of WLAN/WIFI_
- [select] **Wireless LAN Recovery** — Disabled / Enabled ★
    - _Wireless LAN Recovery suppport Enable/Disable_
- [select] **LAN Power Enable** — Disabled / Enabled ★
    - _Enable or disable LAN Power_
- [select] **LAN Low Power Mode** — Disabled★ / Enabled 
    - _Enable or disable LAN Low Power Mode_
- [select] **WWAN Power Enable** — Disabled / Enabled ★ / Manual
    - _Enable or disable the power of WWAN_
- [select] **Eval Auto Detection** — Disabled★ / Enabled 
    - _Disable or enable EVAL card auto detection_
- [select] **Camera 0 Enable** — Disabled / Enabled ★
    - _Enable or disable the power of REAR CAMERA_
- [select] **Camera 1 Enable** — Disabled / Enabled ★
    - _Enable or disable the power of FRONT CAMERA_
- [select] **UCSI Support** — Disabled / Enabled ★
    - _Enable/Disable UCSI (USB Type-C Connector System Software Interface)_
- [select] **UCSI tunnel location** — UCSI tunnel at EC RAM★ / UCSI tunnel at MMIO 0xFEEC2000
    - _UCSI tunnel can be put on ECRAM or MMIO space, this option specify which one is selected._
- [select] **S3/Modern Standby Support** — S3 Enable★ / Modern Standby Enable
    - _Switch S3/Modern Standby_
- [select] **Modern Standby Type** — Modern Standby + S0i2 / Modern Standby + S0i3★ / Modern Standby + S0i2 + S0i3
    - _Select S0I2 or S0I3 type for Modern Standby._
- [select] **SATA D3cold Enable** — Disabled★ / Enabled 
    - _Enable/Disable SATA devies D3-COLD support._
- [select] **Reduce Hardware Support** — Disabled★ / Enabled 
    - _Enable/Disable Reduce Hardware Support. Please disable PME wakeup, when Reduce Hardware enabled._
- [select] **MS Resource** — Disabled / Enabled ★ / Auto
    - _Auto: USB interrupt resource is controlled automatically; Enable: Enable USB current resource for MS; Disable: Disable USB current resource for MS._
- [select] **Wake on PME** — Disabled / Enabled ★
    - _Determines the action taken when the system power is off and a PCI Power Management Enable wake up event occurs._
- [select] **Sensor Fusion User Mode Driver** — Disabled★ / Enabled 
    - _Enable/Disable Sensor Fusion User Mode Driver_
- [select] **MITT/WITT Selection** — MITT Only / WITT Only / Both disable★
- [select] **Unused GPP Clocks Off** — Disabled / Enabled ★
    - _Turn Unused GPP Clocks Off_
- [select] **Clock PM: CLK_REQ0** — Disabled / Enabled ★
    - _Enable or disable CLK_REQ0# for M.2 WLAN Slot J3711_
- [select] **Clock PM: CLK_REQ1** — Disabled / Enabled ★
    - _Enable or disable CLK_REQ1# for Onboard LAN U1301_
- [select] **Clock PM: CLK_REQ2** — Disabled / Enabled ★
    - _Enable or disable CLK_REQ2# for M.2 WWAN Slot J3712_
- [select] **Clock PM: CLK_REQ3** — Disabled / Enabled ★
    - _Enable or disable CLK_REQ3# for M.2 WIFI Slot J3709_
- [select] **Clock PM: CLK_REQ4** — Disabled★ / Enabled 
    - _Enable or disable CLK_REQ4# for DT x4 Slot J3606_
- [select] **Clock PM: CLK_REQ5** — Disabled / Enabled ★
    - _Enable or disable CLK_REQ5# for M.2 SSD Slot J3704_
- [select] **Clock PM: CLK_REQ6** — Disabled★ / Enabled 
    - _Enable or disable CLK_REQ6# for MXM x8 Slot J3604_
- [select] **KBC Support** — Disabled / Enabled ★
    - _Enable/Disable KBC Support under OS_
- [select] **AcDcSwitch** — Disabled★ / Enabled 
    - _Enable/disable AcDcSwitch._
- [number] **AmdDcTimer**
    - _AmdDcTimer Setting._
- [number] **AmdAcTimer**
    - _AmdAcTimer Setting._
- [select] **SATA/ SATA express selection** — SATA★ / SATA express
    - _SATA/ SATA express selection  Setting._
- [select] **VDDP voltage** — VDDP voltage (0.9V)★ / VDDP voltage (+10mv) / VDDP voltage (+20mv) / VDDP voltage (+30mv) / VDDP voltage (+40mv) / VDDP voltage (+50mv) / VDDP voltage (+60mv) / VDDP voltage (+70mv) / VDDP voltage (+80mv) / VDDP voltage (+90mv) / VDDP voltage (+100mv) / VDDP voltage (-10mv) / VDDP voltage (-20mv) / VDDP voltage (-30mv) / VDDP voltage (-40mv) / VDDP voltage (-50mv) / VDDP voltage (-60mv) / VDDP voltage (-70mv) / VDDP voltage (-80mv) / VDDP voltage (-90mv) / VDDP voltage (-100mv)
    - _VDDP voltage  Setting._
- [select] **VDD18 voltage** — VDD18 voltage (1.8V)★ / VDD18 voltage (ANPEC:+40mv/TI:+25mv) / VDD18 voltage (ANPEC:+50mv/TI:+37.5mv) / VDD18 voltage (ANPEC:+60mv/TI:+50mv) / VDD18 voltage (ANPEC:+70mv/TI:+62.5mv) / VDD18 voltage (ANPEC:+80mv/TI:+75mv) / VDD18 voltage (ANPEC:+90mv/TI:+87.5mv) / VDD18 voltage (ANPEC:+100mv/TI:+100mv) / VDD18 voltage (ANPEC:+110mv/TI:+112.5mv) / VDD18 voltage (ANPEC:+120mv/TI:+125mv) / VDD18 voltage (ANPEC:+130mv/TI:+137.5mv) / VDD18 voltage (ANPEC:-40mv/TI:-25mv) / VDD18 voltage (ANPEC:-50mv/TI:-37.5mv) / VDD18 voltage (ANPEC:-60mv/TI:-50mv) / VDD18 voltage (ANPEC:-70mv/TI:-62.5mv) / VDD18 voltage (ANPEC:-80mv/TI:-75mv) / VDD18 voltage (ANPEC:-90mv/TI:-87.5mv) / VDD18 voltage (ANPEC:-100mv/TI:-100mv) / VDD18 voltage (ANPEC:-110mv/TI:-112.5mv) / VDD18 voltage (ANPEC:-120mv/TI:-125mv) / VDD18 voltage (ANPEC:-130mv/TI:-137.5mv)
    - _VDD18 voltage  Setting._
- [select] **5V_S5 voltage.** — 5v_ALW(default)★ / 5v_ALW +60mv / 5v_ALW +100mv
    - _5V_S5 voltage setting for ANPEC PSA_
- [select] **AMD KVM Mouse Protocol** — Absolute / Simple / Auto★
    - _Swtich KVM Mouse Protocol between Absolut/Simple_
- [select] **AMD DPTC interface** — Disabled★ / Enabled 
    - _Dynamic Power and Thermal Control Interface Enable/Disable_
- [select] **BLINK LED** — Disabled / Enabled ★ / GPIO 11 Output Low / GPIO 11 Output High
    - _Enable/Disable BLINK LED to identify S3/S4 state_
- [select] **iLA TraceMemoryEn** — Disabled★ / Enabled 
    - _Reserved 1M bytes MMIO space on 1M boundary when iLA TraceMemoryEn enabled_
- [select] **RT3663 VRM PSI0 Workaround** — Disabled★ / Enabled 
    - _For NRT3663 VRM only. Enable PSI0 Workaround To Save Power._

## F9=￱重設回預設值￰  (3 settings)

- [select] **N**
    - _￱請輸入足夠字元￰_
- [select] **￱變更已儲存￰**
    - _[￱繼續￰]_
- [select] **Setup Warning**
    - _￱設定通知￰_

## Changes have not saved. Save Changes or not?  (8 settings)

- [select] **Oui**
    - _Non_
- [select] **Sélect. élément**
    - _F5/F6_
- [select] **Yes** — textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★ / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFFFFFFFF' bkcolor='0' bkcolor2='0' bkcolor3='0' bkimagestyle='' bkimage='@ButtonNormal' scale9grid='12,12,12,12' 
    - _No_
- [select] **Select Item** — textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★ / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFFFFFFFF' bkcolor='0' bkcolor2='0' bkcolor3='0' bkimagestyle='' bkimage='@ButtonNormal' scale9grid='12,12,12,12' 
    - _F5/F6_
- [select] **￱是￰**
    - _￱否￰_
- [select] **￱選擇項目￰**
    - _F5/F6_
- [select] **￱はい￰**
    - _￱いいえ￰_
- [select] **￱アイテム選択￰**
    - _F5/F6_

## NC-SI  (46 settings)

- [select] **SMASH** — バス：デバイス：機能★ / iSCSI / Bus:Dispositivo:Función / Bus:Périphérique:Fonction / Bus:Device:Function / Bus:Gerät:Funktion
    - _CCM_
- [select] **UMP** — バス：デバイス：機能★ / Fcode / ブート コード / 複数のブート エージェント / UEFI オプション ROM / Fcode オプション ROM / iSCSI ブート / 管理ファームウェア / 構成 ROM / メイン コンフィギュレーション ページ / iSCSI 全般パラメタ / iSCSI の全般的なブート パラメタを設定する。 / iSCSI イニシエータ パラメタ / iSCSI イニシエータ パラメタを設定する。 / iSCSI ファースト ターゲット パラメタ / iSCSI ファースト ターゲット パラメタを設定する。 / iSCSI セカンド ターゲット パラメタ / iSCSI セカンド ターゲット パラメタを設定する。 / セカンダリ デバイス / セカンダリ デバイスのパラメタを設定する。 / iSCSI セカンダリ デバイス パラメタ / Bus:Dispositivo:Función / Bootcode / Multiple Boot Agent / Opción UEFI ROM / Opción Fcode ROM / Arranque iSCSI / Administración FW / Configuración ROM / Página de configuración principal / Parámetros generales de iSCSI / Configurar parámetros generales de arranque iSCSI. / Parámetros de iniciador de iSCSI / Configurar parámetros de iniciador de iSCSI. / Parámetros de primer destino de iSCSI / Configurar parámetros de primer destino de iSCSI. / Parámetros de segundo destino de iSCSI / Configurar parámetros de segundo destino iSCSI. / Dispositivo secundario / Configurar parámetros de dispositivo secundario. / Parámetros de dispositivo secundario iSCSI / Bus:Périphérique:Fonction / Code d'initialisation / ROM en option UEFI / ROM en option Fcode / Initialisation iSCSI / Micrologiciel de gestion / ROM de configuration / Page de configuration principale / Paramètres généraux iSCSI / Configurer les paramètres généraux iSCSI de démarrage. / Paramètres de l'initiateur iSCSI / Configurer les paramètres de l'initiateur iSCSI. / Paramètres de la première cible iSCSI / Configurer les paramètres de la première cible iSCSI. / Paramètres de la deuxième cible iSCSI / Configurer les paramètres de la deuxième cible iSCSI. / Périphérique secondaire / Configurer les paramètres du périphérique secondaire. / Paramètres iSCSI du périphérique secondaire / Bus:Device:Function / Firmware Package / UEFI Option ROM / Fcode Option ROM / iSCSI Boot / Management FW / Configuration ROM / Main Configuration Page / iSCSI General Parameters / Configure iSCSI general boot parameters. / iSCSI Initiator Parameters / Configure iSCSI initiator parameters. / iSCSI First Target Parameters / Configure iSCSI first target parameters. / iSCSI Second Target Parameters / Configure iSCSI second target parameters. / Secondary Device / Configure Secondary device parameters. / iSCSI Secondary Device Parameters / Bus:Gerät:Funktion / BootCode / UEFI – optionales ROM / Fcode – optionales ROM / Hauptkonfigurationsseite / Allgemeine iSCSI-Parameter / Allgemeine iSCSI-Bootparameter konfigurieren. / Initiator-iSCSI-Parameter / Initiator-iSCSI-Parameter konfigurieren. / Erste iSCSI-Zielparameter / Erste iSCSI-Zielparameter konfigurieren. / Zweite iSCSI-Zielparameter / Zweite iSCSI-Zielparameter konfigurieren. / Sekundäres Gerät / Parameter des sekundären Geräts konfigurieren. / iSCSI-Parameter des sekundären Geräts
    - _EFI バージョン_
- [select] **セカンダリ デバイスのパラメタを設定する。** — オプション ROM / ブート オプション ROM をイネーブル/ディスネーブルする / 自動検出 / BBS / Int 18h / Int 19h / セットアップ プロンプトを隠す / ROM の初期化中にセットアップ プロンプトを表示するかどうかを設定する。 / キー操作のセットアップ / バス：デバイス：機能★ / コンフィギュレーション メニューを呼び出すキー操作を設定する。 / Ctrl-S / Ctrl-B / バナー メッセージのタイムアウト / タイムアウト値を選択する。(0 はデフォルトの 4 秒、15 は遅延なし、1 ～ 14 は秒単位のタイムアウト値) / BRCM ISAN / 0.0.0.0 / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / PCI デバイス ID
- [select] **FlexAddressing** — オプション ROM / ブート オプション ROM をイネーブル/ディスネーブルする / 自動検出 / BBS / Int 18h / Int 19h / セットアップ プロンプトを隠す / ROM の初期化中にセットアップ プロンプトを表示するかどうかを設定する。 / キー操作のセットアップ / バス：デバイス：機能★ / コンフィギュレーション メニューを呼び出すキー操作を設定する。 / Ctrl-S / Ctrl-B / バナー メッセージのタイムアウト / タイムアウト値を選択する。(0 はデフォルトの 4 秒、15 は遅延なし、1 ～ 14 は秒単位のタイムアウト値) / BRCM ISAN / 0.0.0.0 / Option ROM / Enable/Disable Boot Option ROM / Auto Detect / Hide Setup Prompt / Configure whether Setup Prompt is displayed during ROM initialization. / Setup Key Stroke / Bus:Device:Function / Configure key strokes to invoke configuration menu. / Banner Message Timeout / Select timeout value. (0 defaults to 4 seconds, 15 is no delay, 1-14 is timeout value in seconds) / Boot Option ROM aktivieren/deaktivieren / Auto Erkennung / Int. 18 Std. / Int. 19 Std. / Eingabeaufforderung ausblenden / Konfigurieren, ob die Eingabeaufforderung während der ROM-Initialisierung angezeigt wird. / Tastenanschlag eingeben / Bus:Gerät:Funktion / Tastenanschläge konfigurieren, um das Konfigurationsmenü aufzurufen. / Strg-S / Strg-B / Banner-Nachricht Zeitüberschreitung / Wert für Zeitüberschreitung auswählen. (0 ist standardmäßig auf 4 Sekunden eingestellt, 15 bedeutet keine Zeitüberschreitung, 1-14 ist der Wert der Zeitüberschreitung in Sekunden)
    - _TX 帯域幅コントロール最大_
- [select] **TX 帯域幅コントロール最小** — Ctrl-S / Ctrl-B / バナー メッセージのタイムアウト / タイムアウト値を選択する。(0 はデフォルトの 4 秒、15 は遅延なし、1 ～ 14 は秒単位のタイムアウト値) / BRCM ISAN / 0.0.0.0 / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / PCI デバイス ID / 無効な TCP ポート / 無効な VLAN ID / HP共有メモリ機能を無効にします / 予約されたメモリ領域の使用状況のデバイス割り当てを直接ゲスト仮想マシンに許可をディセーブルにします。 / 新しい画像はこのデバイスではサポートされていません。 / 容量が不足しているために画像を保存できません。 / 新しい画像のバージョンは現在の画像と同じか、それよりも古いバージョンです。 / 処理中にエラーが発生しました。 / バス：デバイス：機能★ / イメージ： / バージョン： / ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^[-0-9a-zA-Z.:_]{0,128}$ / ^([A-Fa-f0-9]{2}:){5}([0-9a-fA-F]{2})$ / ISCSIInitiatorParameters_CHAPSecret / ISCSIFirstTargetParameters_CHAPSecret
    - _xxxxxxxxx-バス：デバイス：機能_
- [select] **ISCSISecondTargetParameters_CHAPSecret** — バス：デバイス：機能★ / Bus:Dispositivo:Función / Bus:Périphérique:Fonction / Bus:Device:Function / ISCSISecondTargetParameters_BootLUN / Bus:Gerät:Funktion
- [number] **PCI-E x1**
- [select] **Configurar parámetros de dispositivo secundario.** — Opción ROM / Habilitar/Deshabilitar opción ROM de arranque / Detección automática / BBS / Int 18 h / Int 19 h / Ocultar solicitud de configuración / Configurar si se muestra la solicitud de configuración durante la inicialización ROM. / Configurar pulsación de tecla / Bus:Dispositivo:Función★ / Configurar pulsaciones de teclas para llamar al menú de configuración. / Ctrl-S / Ctrl-B / Tiempo de espera de mensaje de banner / Seleccionar valor para el tiempo de espera. (0 establece de forma predeterminada 4 segundos, 15 es sin retraso, 1-14 es el valor de tiempo de espera en segundos) / BRCM ISAN / 0.0.0.0 / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / ID de dispositivo PCI
- [select] **Dirección flexible** — Opción ROM / Habilitar/Deshabilitar opción ROM de arranque / Detección automática / BBS / Int 18 h / Int 19 h / Ocultar solicitud de configuración / Configurar si se muestra la solicitud de configuración durante la inicialización ROM. / Configurar pulsación de tecla / Bus:Dispositivo:Función★ / Configurar pulsaciones de teclas para llamar al menú de configuración. / Ctrl-S / Ctrl-B / Tiempo de espera de mensaje de banner / Seleccionar valor para el tiempo de espera. (0 establece de forma predeterminada 4 segundos, 15 es sin retraso, 1-14 es el valor de tiempo de espera en segundos) / BRCM ISAN / 0.0.0.0
    - _Control de banda ancha TX máximo_
- [select] **Control de banda ancha TX mínimo** — Ctrl-S / Ctrl-B / Tiempo de espera de mensaje de banner / Seleccionar valor para el tiempo de espera. (0 establece de forma predeterminada 4 segundos, 15 es sin retraso, 1-14 es el valor de tiempo de espera en segundos) / BRCM ISAN / 0.0.0.0 / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / ID de dispositivo PCI / Puerto TCP no válido / ID de VLAN no válido / Desactivar función de memoria compartida de HP / Desactivar el uso de regiones de memoria reservada para permitir la asignación directa de dispositivo para las máquinas virtuales invitadas. / La nueva imagen no se admite en este dispositivo. / Espacio insuficiente para almacenar la imagen. / La versión de la nueva imagen es la misma o anterior que la de la imagen actual. / Error de procesamiento. / Bus:Dispositivo:Función★ / Imagen: / Versión: / ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^[-0-9a-zA-Z.:_]{0,128}$ / ^([A-Fa-f0-9]{2}:){5}([0-9a-fA-F]{2})$ / ISCSIInitiatorParameters_CHAPSecret / ISCSIFirstTargetParameters_CHAPSecret
    - _xxxxxxxxx-Bus:Dis:Fcn_
- [select] **Configurer les paramètres du périphérique secondaire.** — ROM en option / Activer/Désactiver la ROM en option d'initialisation / Détecter automatiquement / BBS / Int 18h / Int 19h / Masquer l'invite de configuration / Configurer l'affichage de l'invite de configuration pendant l'initialisation de la ROM. / Configurer la séquence de touches / Bus:Périphérique:Fonction★ / Configurer la séquence de touches permettant d'appeler le menu de configuration. / Ctrl-S / Ctrl-B / Délai d'inactivité du message de bannière / Sélectionner une valeur pour le délai d'inactivité. (0 : par défaut, 4 secondes ; 15 : aucun délai ; 1-14 : valeur du délai d'inactivité en secondes) / BRCM ISAN / 0.0.0.0 / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / ID du périphérique PCI
- [select] **AdressageFlex** — ROM en option / Activer/Désactiver la ROM en option d'initialisation / Détecter automatiquement / BBS / Int 18h / Int 19h / Masquer l'invite de configuration / Configurer l'affichage de l'invite de configuration pendant l'initialisation de la ROM. / Configurer la séquence de touches / Bus:Périphérique:Fonction★ / Configurer la séquence de touches permettant d'appeler le menu de configuration. / Ctrl-S / Ctrl-B / Délai d'inactivité du message de bannière / Sélectionner une valeur pour le délai d'inactivité. (0 : par défaut, 4 secondes ; 15 : aucun délai ; 1-14 : valeur du délai d'inactivité en secondes) / BRCM ISAN / 0.0.0.0
    - _Maximale pour contrôle de la bande passante TX_
- [select] **Minimale pour contrôle de la bande passante TX** — Ctrl-S / Ctrl-B / Délai d'inactivité du message de bannière / Sélectionner une valeur pour le délai d'inactivité. (0 : par défaut, 4 secondes ; 15 : aucun délai ; 1-14 : valeur du délai d'inactivité en secondes) / BRCM ISAN / 0.0.0.0 / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / ID du périphérique PCI / Port TCP non valide / ID de VLAN non valide / Désactiver la fonction de mémoire partagée HP / Désactiver l'utilisation de régions de mémoire réservée pour permettre l'affectation directe de périphérique pour les ordinateurs virtuels invités. / La nouvelle image n'est pas prise en charge par le périphérique. / Espace insuffisant pour stocker l'image. / La nouvelle version de l'image est identique ou plus ancienne que l'image en cours. / Erreur de traitement / Bus:Périphérique:Fonction★ / Image : / Version : / ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^[-0-9a-zA-Z.:_]{0,128}$ / ^([A-Fa-f0-9]{2}:){5}([0-9a-fA-F]{2})$ / ISCSIInitiatorParameters_CHAPSecret / ISCSIFirstTargetParameters_CHAPSecret
    - _xxxxxxxxx-Bus:Pér:Fcn_
- [select] **Configure Secondary device parameters.** — Option ROM / Enable/Disable Boot Option ROM / Auto Detect / BBS / Int 18h / Int 19h / Hide Setup Prompt / Configure whether Setup Prompt is displayed during ROM initialization. / Setup Key Stroke / Bus:Device:Function★ / Configure key strokes to invoke configuration menu. / Ctrl-S / Ctrl-B / Banner Message Timeout / Select timeout value. (0 defaults to 4 seconds, 15 is no delay, 1-14 is timeout value in seconds) / BRCM ISAN / 0.0.0.0 / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / 0 / PCI Device ID
- [select] **TX Bandwidth Control Minimum** — Ctrl-S / Ctrl-B / Banner Message Timeout / Select timeout value. (0 defaults to 4 seconds, 15 is no delay, 1-14 is timeout value in seconds) / BRCM ISAN / 0.0.0.0 / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / 0 / PCI Device ID / Invalid TCP Port / Invalid VLAN ID / Disable HP Shared Memory features / Disable usage of reserved memory regions to allow direct assignment of device to guest virtual machines. / The new image is not supported by this device. / Insufficient space to store image. / The new image version is the same or older than the current image. / Processing error. / Port Enablement / Bus:Device:Function★ / Enable all ports / Disable port 3 / Disable ports 2 & 3 / Disable ports 1, 2, & 3 / 2107-Slot X Error- The firmware update did not complete successfully. Action: Ensure the proper firmware image is being used and attempt to update the firmware again. / Image: / Version: / ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}|[A-Fa-f0-9]{0,4}\:([A-Fa-f0-9]{0,4}\:?){5}[A-Fa-f0-9]{0,4}\:[A-Fa-f0-9]{0,4}$ / ^[0-9]{1,3}$ / ^[-0-9a-zA-Z.:_]{0,128}$ / ^([A-Fa-f0-9]{2}:){5}([0-9a-fA-F]{2})$ / ISCSIInitiatorParameters_CHAPSecret / ISCSIFirstTargetParameters_CHAPSecret
    - _xxxxxxxxx-Bus:Dev:Fcn_
- [number] **ISCSIFirstTargetParameters_TCPPort**
    - _ISCSISecondTargetParameters_TCPPort_
- [select] **ISCSIFirstTargetParameters_Connect** — Bus:Device:Function★ / ISCSIInitiatorParameters_IPAddress / ISCSIFirstTargetParameters_IPAddress / ISCSISecondTargetParameters_IPAddress / ISCSIInitiatorParameters_IscsiName / Option ROM / Enable/Disable Boot Option ROM / Auto Detect / BBS
    - _ISCSISecondTargetParameters_Connect_
- [select] **ISCSIFirstTargetParameters_IscsiName** — Bus:Device:Function★ / ISCSIInitiatorParameters_IPAddress / ISCSIFirstTargetParameters_IPAddress / ISCSISecondTargetParameters_IPAddress / ISCSIInitiatorParameters_IscsiName / Option ROM / Enable/Disable Boot Option ROM / Auto Detect / BBS
    - _ISCSISecondTargetParameters_IscsiName_
- [select] **ISCSIInitiatorParameters_CHAPID** — Bus:Device:Function★ / ISCSISecondTargetParameters_BootLUN
    - _ISCSIFirstTargetParameters_CHAPID_
- [number] **ISCSISecondTargetParameters_CHAPID**
    - _Broadcom NetXtreme PCIe x-Port RJ45 Ethernet Adapter--PhysicalPortxLogicalPort1_
- [select] **PCI Generic Information** — Bus:Device:Function★ / UUID / Card Name / ISCSIInitiatorParameters_IPAddress / ISCSIFirstTargetParameters_IPAddress / ISCSISecondTargetParameters_IPAddress / ISCSIInitiatorParameters_IscsiName / Option ROM / Enable/Disable Boot Option ROM / Auto Detect / BBS / Int 18h / Int 19h
    - _BRCM AIM Formset_
- [select] **Manufacturer** — Bus:Device:Function★ / UUID / Card Name / ISCSIInitiatorParameters_IPAddress / ISCSIFirstTargetParameters_IPAddress / ISCSISecondTargetParameters_IPAddress / ISCSIInitiatorParameters_IscsiName / Option ROM / Enable/Disable Boot Option ROM / Auto Detect / BBS / Int 18h / Int 19h
    - _Serial Number_
- [select] **Part Number** — Bus:Device:Function★ / ISCSISecondTargetParameters_BootLUN
    - _Model_
- [number] **Card SKU**
    - _FoD UID_
- [select] **Max Data Width** — Bus:Device:Function★ / ISCSISecondTargetParameters_BootLUN
    - _Connector Layout_
- [number] **Package Type**
    - _Other Package Type_
- [select] **Module/Card** — Bus:Device:Function★ / ISCSISecondTargetParameters_BootLUN
    - _Onboard_
- [number] **FlexSystem Mezzanine Connector**
    - _ML2_
- [select] **Onboard** — Bus:Device:Function★ / ISCSISecondTargetParameters_BootLUN
    - _PCI-E x4_
- [select] **Firmware Information 1** — Bus:Device:Function★ / ISCSISecondTargetParameters_BootLUN
- [number] **Firmware Name**
    - _Version String_
- [select] **Description** — Bus:Device:Function★ / ISCSISecondTargetParameters_BootLUN
    - _Release Date_
- [select] **Software ID** — Bus:Device:Function★ / ISCSISecondTargetParameters_BootLUN
    - _Network Information_
- [number] **Physical Port 1**
    - _Physical Port 2_
- [number] **Physical Port 3**
    - _Physical Port 4_
- [select] **Logical Port 1** — Bus:Device:Function★ / Logical Port 3 / Logical Port 4 / Number of Physical Ports / Max Number of Logical Ports / Physical Port's Connector Layout / Physical Port Index / Number of Logical Ports / Permanent Address
    - _Logical Port 2_
- [select] **Permanent Address** — Bus:Device:Function★ / Option ROM / Enable/Disable Boot Option ROM / Auto Detect / BBS / Int 19h / Hide Setup Prompt / Setup Key Stroke / Configure key strokes to invoke configuration menu. / Permanent Address / UUID / Card Name / ISCSIInitiatorParameters_IPAddress / ISCSIFirstTargetParameters_IPAddress / ISCSISecondTargetParameters_IPAddress / ISCSIInitiatorParameters_IscsiName / Int 18h
- [select] **Max Data Size** — Option ROM / Enable/Disable Boot Option ROM / Auto Detect / Bus:Device:Function★ / BBS / Int 18h / ISCSIFirstTargetParameters_IPAddress / ISCSISecondTargetParameters_IPAddress / ISCSIInitiatorParameters_IscsiName / Int 19h / Permanent Address / UUID / Card Name / ISCSIInitiatorParameters_IPAddress / Hide Setup Prompt / Configure whether Setup Prompt is displayed during ROM initialization. / Setup Key Stroke / Configure key strokes to invoke configuration menu. / Ctrl-S / Ctrl-B / Banner Message Timeout / Select timeout value. (0 defaults to 4 seconds, 15 is no delay, 1-14 is timeout value in seconds) / BRCM ISAN / 0.0.0.0 / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / 0
- [select] **Network Addresses** — UUID / Card Name / ISCSIInitiatorParameters_IPAddress / ISCSIFirstTargetParameters_IPAddress / ISCSISecondTargetParameters_IPAddress / ISCSIInitiatorParameters_IscsiName / Option ROM / Enable/Disable Boot Option ROM / Auto Detect / Bus:Device:Function★ / Permanent Address / BBS / Int 18h / Int 19h / Hide Setup Prompt
- [select] **Logical Port Index** — UUID / Card Name / ISCSIInitiatorParameters_IPAddress / ISCSIFirstTargetParameters_IPAddress / ISCSISecondTargetParameters_IPAddress / ISCSIInitiatorParameters_IscsiName / Option ROM / Enable/Disable Boot Option ROM / Auto Detect / Bus:Device:Function★ / Permanent Address / BBS / Int 18h / Int 19h / Hide Setup Prompt
- [select] **Link Technology** — UUID / Card Name / ISCSIInitiatorParameters_IPAddress / ISCSIFirstTargetParameters_IPAddress / ISCSISecondTargetParameters_IPAddress / ISCSIInitiatorParameters_IscsiName / Option ROM / Enable/Disable Boot Option ROM / Auto Detect / BBS / Int 18h / Int 19h / Hide Setup Prompt / Configure whether Setup Prompt is displayed during ROM initialization. / Setup Key Stroke / Configure key strokes to invoke configuration menu. / Ctrl-S / Ctrl-B / Banner Message Timeout / Select timeout value. (0 defaults to 4 seconds, 15 is no delay, 1-14 is timeout value in seconds) / BRCM ISAN / 0.0.0.0 / Bus:Device:Function★ / Permanent Address / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / 0 / vNIC Mode / Max Speed
- [select] **Max Speed** — Protocol Type / Bus:Device:Function★
- [select] **Protocol Type** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★
- [select] **Current Work Protocol Ethernet** — Bus:Device:Function★ / iSCSI / Legacy Boot Protocol
- [select] **Parameter des sekundären Geräts konfigurieren.** — Option ROM / Boot Option ROM aktivieren/deaktivieren / Auto Erkennung / BBS / Int. 18 Std. / Int. 19 Std. / Eingabeaufforderung ausblenden / Konfigurieren, ob die Eingabeaufforderung während der ROM-Initialisierung angezeigt wird. / Tastenanschlag eingeben / Bus:Gerät:Funktion★ / Tastenanschläge konfigurieren, um das Konfigurationsmenü aufzurufen. / Strg-S / Strg-B / Banner-Nachricht Zeitüberschreitung / Wert für Zeitüberschreitung auswählen. (0 ist standardmäßig auf 4 Sekunden eingestellt, 15 bedeutet keine Zeitüberschreitung, 1-14 ist der Wert der Zeitüberschreitung in Sekunden) / BRCM ISAN / 0.0.0.0 / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / PCI-Geräte-ID
- [select] **TX-Bandbreitensteuerung – Minimum** — Strg-S / Strg-B / Banner-Nachricht Zeitüberschreitung / Wert für Zeitüberschreitung auswählen. (0 ist standardmäßig auf 4 Sekunden eingestellt, 15 bedeutet keine Zeitüberschreitung, 1-14 ist der Wert der Zeitüberschreitung in Sekunden) / BRCM ISAN / 0.0.0.0 / iqn.1995-05.com.broadcom.iscsiboot / 00:00:00:00:00:00 / PCI-Geräte-ID / Ungültiger TCP-Port / Ungültige VLAN-ID / HP Shared-Memory-Funktion deaktivieren / Deaktivieren Sie die Verwendung des reservierten Speichers Regionen zu ermöglichen direkte Zuordnung von Gerät zu virtuellen Gastcomputer. / Das neue Bild wird von diesem Gerät nicht unterstützt. / Nicht genügend Speicherplatz, um das Bild zu speichern. / Die neue Bildversion ist die gleiche wie oder älter als das aktuelle Bild. / Verarbeitungsfehler. / Bus:Gerät:Funktion★ / Bild: / Version: / ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^[-0-9a-zA-Z.:_]{0,128}$ / ^([A-Fa-f0-9]{2}:){5}([0-9a-fA-F]{2})$ / ISCSIInitiatorParameters_CHAPSecret / ISCSIFirstTargetParameters_CHAPSecret
    - _xxxxxxxxx-Bus:Ger:Fcn_

## Entrer Mot de Passe Present:  (1 settings)

- [toggle] **Press YES **

## +/- =Adjust Value  (13 settings)

- [select] **Enter New Password**
    - _Confirm New Password_
- [select] **Password do not match**
    - _Invalid password_
- [select] **Push Enter/ESC - Leave** — Push PageDown  - Next Page★
    - _Push PageUp    - previous_
- [select] **Setup Warning** — Changes have been saved.★ / [continue]
    - _Setup Notice_
- [select] **Esc=Exit Menu**
    - _F10=Save and Exit_
- [select] **Invalid password! Please enter new string for setting password.**
    - _Exit Saving Changes_
- [select] **Ok**
    - _Cancel_
- [select] **Yes**
    - _No_
- [select] **Changes have been saved after press ** — Question value mismatch with Option value!★ / Changes have not saved. Save Changes or not?
    - _Changes have not saved. Save Changes and exit?_
- [select] **Press 'Y' to save and exit, 'N' to discard and exit.**
    - _InsydeH2O Setup Utility_
- [select] **InsydeH2O Setup Utility (Manufacture)**
    - _Rev. 5.0_
- [select] **Re-enter Password**
    - _Please type in your data_
- [select] **Setup Default**
    - _Exit_

## Realtek UEFI UNDI driver information  (12 settings)

- [select] **%s**
    - _MAC Address:_
- [select] **Current network address**
    - _%02x:%02x:%02x:%02x:%02x:%02x_
- [select] **Subnetmask** — Gateway★
    - _Set or change DASH subnetmask_
- [select] **Configure DASH(Desktop and Mobile Architecture for System Hardware) setting. DASH is a web services-based standard that can support both in-band and out-of-band management.** — Host Configuration★ / Configure DASH host settings
    - _Realtek RealManage Setup_
- [select] **Configure DASH security settings**
    - _Setup and Configuration_
- [select] **Host Name**
    - _Set or change DASH host name_
- [select] **Domain Name**
    - _Set or change DASH domain name_
- [select] **DHCPv4**
    - _Enable or Disble DASH DHCP service_
- [select] **Host Configuration** — Configure DASH TCP/IP settings★ / TCP/IP Configuration
    - _TCP/IP Configuration_
- [select] **Provisioning Model**
    - _Configure DASH provision settings_
- [select] **PCI Slot:**
    - _The PCI address of Realtek ethernet controller_
- [select] **Set or change DASH password**
    - _TLS PSK_

## % of the system memory tested OK  (1 settings)

- [number] **System doesn't have any CD/DVD boot option. Please select other boot option in Boot Manager Menu.**
    - _System doesn't have any Network boot option. Please select other boot option in Boot Manager Menu or Enable PXE Boot Option in SCU._

## Boot Option Menu  (8 settings)

- [toggle] **Legacy BEV**
    - _Legacy Floppy_
- [toggle] **Legacy Hard Drive**
- [select] **Legacy Unknown Device** — Legacy USB / HDD : ★
    - _EFI Boot Devices_
- [select] **HDD%d : **
    - _ATAPI CDROM : _
- [select] **USB CDROM : ** — Legacy USB★ / Legacy Floppy
    - _Network Boot : _
- [select] **EMMC : ** — Legacy USB / Legacy Floppy★
    - _Press Esc for boot options_
- [select] **USB FDD : ** — Legacy USB★ / Legacy Floppy
    - _USB HDD : _
- [select] **Esc is pressed. Go to boot options.**

## HDD             (3 settings)

- [select] **HDD2(OPAL)    **
    - _HDD3(OPAL)    _
- [select] **HDD4(OPAL)    **
    - _Press Esc for boot options_
- [select] **Esc is pressed. Go to boot options.**

## to approve future Operating System requests   (1 settings)

- [toggle] **Press YES **

## Boot Manager  (3 settings)

- [select] **USB CDROM : **
    - _Network Boot : _
- [select] **EMMC : **
    - _Press Esc for boot options_
- [select] **Esc is pressed. Go to boot options.**

## Press DEL key to skip memory test  (4 settings)

- [select] **Which USB boot option do you want to select?** — System doesn't have any CD/DVD boot option. Please select other boot option in Boot Manager Menu. / Which network boot option do you want to select?★
    - _Which CD/DVD boot option do you want to select?_
- [select] **The timeout value is %d seconds and it is larger than maximum timeout value %d. Restore timeout variable to %d!!!**
- [select] **Esc is pressed. Go to boot options.** — System doesn't have any CD/DVD boot option. Please select other boot option in Boot Manager Menu.★
- [toggle] **System encounters memory errors**

##  bytes of system memory tested OK  (2 settings)

- [select] **Which USB boot option do you want to select?** — Which network boot option do you want to select?★ / The timeout value is %d seconds and it is larger than maximum timeout value %d. Restore timeout variable to %d!!!
    - _Which CD/DVD boot option do you want to select?_
- [select] **Esc is pressed. Go to boot options.** — Which network boot option do you want to select?★

## SATA Port 0     (3 settings)

- [select] **HDD Security count expired bit is acted** — HDD2          ★ / HDD3          
    - _Please shutdown the system_
- [select] **Please input password for ** — HDD2          ★ / HDD3          
- [select] **Press any key** — HDD2          ★ / HDD3          
    - _HDD           _

## Error Status  (2 settings)

- [toggle] **Please restart system**
    - _Press Esc for boot options_
- [toggle] **Esc is pressed. Go to boot options.**

## Legacy Boot Protocol  (28 settings)

- [select] **Select boot strap type.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$
    - _Link Speed_
- [select] **Link Speed** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$
    - _Configure link speed._
- [select] **Configure Multiple Boot Agent (MBA) parameters.** — NIC Configuration★
    - _NIC Configuration_
- [select] **Virtual LAN Mode** — VLAN ID (1..4094)★ / Virtual LAN ID
    - _Configure virtual LAN mode._
- [select] **10 Mbps Full** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$
    - _100 Mbps Half_
- [select] **100 Mbps Full** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _Disabled_
- [select] **Enabled** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$
    - _One Time Disabled_
- [select] **IPv4** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$
    - _IPv6_
- [select] **Configure virtual LAN ID (1..4094).** — 10Mbps Half★ / 10Mbps Full
    - _AutoNeg_
- [select] **100Mbps Half** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _100Mbps Full_
- [select] **Auto Negotiated** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$
    - _10 Mbps Half_
- [select] **Pre-boot Wake On LAN** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _Configure Pre-boot Wake on LAN (WOL)._
- [select] **iSCSI First Target Parameters** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
- [select] **Configure iSCSI first target parameters.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _iSCSI Second Target Parameters_
- [select] **PCI Device ID** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$
- [select] **iSCSI Second Target Parameters** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
- [select] **Configure iSCSI second target parameters.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _Secondary Device_
- [select] **Boot to Target** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _Enable/Disable booting to iSCSI target after logon._
- [select] **ASF** — MAC Address / Permanent MAC Address★
    - _NC-SI_
- [select] **Subnet Mask Prefix** — Permanent MAC Address / Configure CHAP Secret (12 to 16 characters in length).★
    - _Configure IP subnet mask prefix length._
- [select] **Default Gateway** — MAC Address / Permanent MAC Address★ / Configure primary DNS IP address.
    - _Configure default gateway IP address._
- [select] **Subnet Mask** — MAC Address / Permanent MAC Address★
    - _Configure IP subnet mask._
- [select] **CCM** — MAC Address / Permanent MAC Address★
    - _UMP_
- [select] **EFI** — MAC Address / Permanent MAC Address★
- [select] **Fcode** — MAC Address / Permanent MAC Address★
- [select] **Controller BIOS Version** — MAC Address / Permanent MAC Address★
- [select] **MBA** — MAC Address / Permanent MAC Address★
- [select] **iSCSI Boot** — MAC Address / Permanent MAC Address★

## Other Device      (1 settings)

- [toggle] **Esc is pressed. Go to boot options.**

## % de la mémoire de système essayée D'ACCORD  (1 settings)

- [number] **System doesn't have any CD/DVD boot option. Please select other boot option in Boot Manager Menu.**
    - _System doesn't have any Network boot option. Please select other boot option in Boot Manager Menu or Enable PXE Boot Option in SCU._

## Press YES   (12 settings)

- [toggle] **disable**
- [select] **clear** — deactivate and disable★ / allow a user to take ownership of / disallow a user to take ownership of
    - _enable and activate_
- [select] **enable, activate, and allow a user to take ownership of** — disallow a user to take ownership of / allow a user to take ownership of / deactivate and disable★
    - _deactivate, disable, and disallow a user to take ownership of_
- [select] **clear, enable, and activate** — enable, activate, clear, enable, and activate / allow field upgrade / deactivate and disable★
    - _enable, activate and clear_
- [select] **provision** — to approve future Operating System requests  / deactivate and disable★ / WARNING: Clearing erases infomation stored on the TPM. You will lose all created keys and access to data encrypted by these keys.  / Press Esc for boot options
    - _maintain_
- [select] **change the configuration of** — clear and change identity of / maintain★
    - _provision_
- [select] **turn on** — clear and change identity of★ / enable
    - _turn off_
- [select] **to approve future Operating System requests ** — clear and change identity of★ / enable
    - _change the format of boot measurement log_
- [number] **Press YES **
- [number] **issue a Block SID authentication command**
    - _disable issuing a Block SID authentication command_
- [number] **enable blocking SID authentication**
    - _disable blocking SID authentication_
- [select] **Press Esc for boot options**
    - _Esc is pressed. Go to boot options._

## maintain  (1 settings)

- [select] **Press Esc for boot options**
    - _Esc is pressed. Go to boot options._

## EFI USB Device  (6 settings)

- [select] **V1.12** — 05.32.42★ / BIOS Version / BIOS Build Date
    - _FH50P_
- [select] **Processor Type** — BIOS Build Date / BIOS Version / 05.32.42★
    - _System Memory Speed_
- [select] **Do you want to recovery ROM part? (Caution: Not every OS is bootable in Recovery Mode.)** — YES,this choice will flash Rom part. / NO, abort Recovery mode and restart system. / 05.32.42★
    - _Flash Status_
- [select] **Rebooting !** — Boot Succeeded -  / 05.32.42★
    - _% of the system memory tested OK_
- [select] ** has been blocked by the current security policy.** — Boot Succeeded -  /  boot failed. / 05.32.42★
    - _Execution of the selected file has been blocked by the current security policy._
- [select] **Execution of the selected file boot failed.** — Esc is pressed. Go to boot options.★
    - _Press Esc for boot options_

## Perform memory test (DEL to skip)  (1 settings)

- [select] **Esc is pressed. Go to boot options.**

## Etes-vous sûr? (Y/N)  (1 settings)

- [toggle] **Des changements ont été sauvegardés**

## Configure Device Parameters.  (66 settings)

- [select] **Energy Efficient Ethernet (EEE)** — Permanent MAC Address★
    - _VLAN Mode_
- [select] **Version:** — Permanent MAC Address
    - _^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$_
- [select] **PCI Address** — Primary DNS / Configure primary DNS IP address.★
- [select] **Link Status** — Permanent MAC Address
    - _Connected_
- [select] **Disconnected** — Permanent MAC Address★
    - _Blink LEDs_
- [select] **PCI Bus:Device:Function number of this device.** — Permanent MAC Address
    - _Link Status_
- [select] **Blink LEDs for a duration up to 15 seconds.** — Legacy Boot Protocol★ / Select non-UEFI Boot Protocol: Preboot Execution Environment (PXE)/iSCSI.
    - _Legacy Boot Protocol_
- [select] **PXE** — NONE
    - _iSCSI_
- [select] **None** — Permanent MAC Address
    - _Boot Strap Type_
- [number] **Boot Strap Type**
    - _Select boot strap type._
- [number] **Link Speed**
- [number] **Configure link speed.**
    - _Pre-boot Wake On LAN_
- [number] **Configure Pre-boot Wake on LAN (WOL).**
    - _Wake On LAN_
- [select] **Configure Wake on LAN (WOL).** — Configure Energy Efficient Ethernet operation.★ / Maximum Power Savings
    - _Energy Efficient Ethernet_
- [select] **Invalid TCP Port** — Disable HP Shared Memory features / Disable usage of reserved memory regions to allow direct assignment of device to guest virtual machines. / The new image is not supported by this device. / Insufficient space to store image. / The new image version is the same or older than the current image. / Processing error.★ / Port Enablement / Enable all ports / Disable port 3 / Disable ports 2 & 3 / Disable ports 1, 2, & 3 / 2107-Slot X Error- The firmware update did not complete successfully. Action: Ensure the proper firmware image is being used and attempt to update the firmware again. / Image:
    - _Invalid VLAN ID_
- [select] **iSCSI First Target Parameters** — Permanent MAC Address
- [select] **Configure iSCSI first target parameters.** — Permanent MAC Address
    - _iSCSI Second Target Parameters_
- [select] **iSCSI Second Target Parameters** — Permanent MAC Address
- [select] **iSCSI Name** — CHAP ID / Configure CHAP ID (up to 32 characters in length). / Configure CHAP ID (up to 128 characters in length). / Permanent MAC Address
    - _Configure iSCSI name._
- [select] **CHAP ID** — CHAP ID / Configure CHAP ID (up to 32 characters in length). / Configure CHAP ID (up to 128 characters in length).
- [select] **Configure CHAP ID (up to 32 characters in length).** — CHAP ID / Configure CHAP ID (up to 32 characters in length). / Configure CHAP ID (up to 128 characters in length).
    - _Configure CHAP ID (up to 128 characters in length)._
- [select] **CHAP Secret** — CHAP Secret★ / Configure CHAP Secret (12 to 16 characters in length). / Permanent MAC Address
- [select] **Configure CHAP Secret (12 to 16 characters in length).** — CHAP Secret★ / Configure CHAP Secret (12 to 16 characters in length).
    - _CHAP Secret_
- [select] **Configure link up delay time in seconds (0..255).** — Permanent MAC Address★ / CHAP Secret
    - _Use TCP Timestamp_
- [select] **TCP Timestamp** — Permanent MAC Address★
    - _Enable/Disable TCP timestamp._
- [select] **Target as First HDD** — Permanent MAC Address★
    - _Enable/Disable target appears as first hard disk drive (HDD) in the system._
- [select] **LUN Busy Retry Count** — IP Version★ / IP version support.  Modifying this parameter will reset all IP-related fields.
    - _Configure number of retries in 2 second intervals when LUN is busy (0..60)._
- [select] **iSCSI Secondary Device Parameters** — Permanent MAC Address
- [select] **Subnet Mask Prefix** — Permanent MAC Address
    - _Configure IP subnet mask prefix length._
- [select] **Default Gateway** — Primary DNS / Configure primary DNS IP address.★
    - _Configure default gateway IP address._
- [select] **Secondary DNS** — Virtual MAC Address
    - _Configure secondary DNS IP address._
- [select] **IP Address** — Permanent MAC Address★ / MAC Address
    - _Configure target IP address._
- [select] **IP Auto-Configuration** — Permanent MAC Address★
    - _Acquire TCP/IP configuration via Stateful or Stateless Autoconfiguration._
- [select] **Boot to iSCSI Target** — Permanent MAC Address★
    - _Boot to Target_
- [select] **Enable/Disable booting to iSCSI target after logon.** — Permanent MAC Address
    - _DHCP Vendor ID_
- [select] **Subnet Mask** — Permanent MAC Address★ / MAC Address
    - _Configure IP subnet mask._
- [select] **Virtual LAN Mode** — Permanent MAC Address★
    - _Configure virtual LAN mode._
- [select] **VLAN ID (1..4094)** — Configure virtual LAN ID (1..4094).★ / AutoNeg
    - _Virtual LAN ID_
- [select] **10Mbps Half** — 100Mbps Half★ / 100Mbps Full
    - _10Mbps Full_
- [select] **Auto Negotiated** — 10 Mbps Full / 100 Mbps Half★ / 100 Mbps Full
    - _10 Mbps Half_
- [select] **Disabled** — Permanent MAC Address
    - _Enabled_
- [select] **IPv6** — Permanent MAC Address
    - _MBA Configuration Menu_
- [select] **One Time Disabled** — Permanent MAC Address★ / Chip Type
    - _IPv4_
- [select] **MBA Configuration Menu** — Permanent MAC Address★
    - _Configure Multiple Boot Agent (MBA) parameters._
- [select] **NIC Configuration** — Permanent MAC Address
- [select] **iSCSI Parameters via DHCP** — Acquire iSCSI parameters via DHCP. / CHAP Authentication / Enable/Disable CHAP authentication.★
- [select] **iSCSI Boot Configuration Menu** — Permanent MAC Address★
- [select] **Configure iSCSI boot parameters.** — Permanent MAC Address★
    - _iSCSI Configuration_
- [select] **iSCSI Configuration** — Permanent MAC Address★
    - _Firmware Image Menu_
- [select] **Firmware Image Menu** — Permanent MAC Address★
    - _Firmware image information._
- [select] **Listing of firmware image components (and their corresponding versions) currently programmed on the NVRAM.  N/A indicates the image is not present.** — Permanent MAC Address★
- [select] **Firmware Image Properties** — Permanent MAC Address★
    - _TCP/IP Parameters via DHCP_
- [select] **Acquire TCP/IP configuration via DHCP.** — Permanent MAC Address
    - _IP Autoconfiguration_
- [select] **Configure DHCP vendor ID (up to 32 bytes long).** — Permanent MAC Address★
    - _Link Up Delay Time_
- [number] **Enable/Disable target establishment.** — Configure target TCP port number (1..65535).★ / TCP Port
    - _Connect_
- [select] **Configure target TCP port number (1..65535).** — Configure target boot LUN number (0..255).★ / Boot LUN / Secondary Device / Input secondary device MAC address. Use XX:XX:XX:XX:XX:XX format. / Secondary Device MAC Address / Use Independent Target Portal / Use independent target portal when multipath I/O is enabled. / Use Independent Target Name / Use independent target name when multipath I/O is enabled. / Family Firmware Version / Bootcode / MBA / iSCSI Boot / ASF / NC-SI / SMASH / CCM
    - _Boot LUN_
- [select] **UMP** — Fcode★ / Controller BIOS Version / MBA / iSCSI Boot / ASF / NC-SI / SMASH / CCM / UMP / EFI Version / Firmware Package / Bootcode / Multiple Boot Agent / UEFI Option ROM / Fcode Option ROM / Management FW
    - _EFI_
- [select] **Configuration ROM** — iSCSI General Parameters★
    - _Main Configuration Page_
- [select] **Configure iSCSI general boot parameters.** — iSCSI Initiator Parameters / Chip Type★
    - _iSCSI Initiator Parameters_
- [select] **Configure iSCSI initiator parameters.** — Permanent MAC Address
    - _iSCSI First Target Parameters_
- [select] **Configure iSCSI second target parameters.** — Permanent MAC Address★ / Secondary Device / Configure Secondary device parameters.
    - _Secondary Device_
- [select] **FlexAddressing** — Permanent MAC Address
    - _TX Bandwidth Control Maximum_
- [select] **^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$** — Permanent MAC Address
    - _^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}|[A-Fa-f0-9]{0,4}\:([A-Fa-f0-9]{0,4}\:?){5}[A-Fa-f0-9]{0,4}\:[A-Fa-f0..._
- [number] **Legacy Boot Protocol**
- [select] **Select non-UEFI Boot Protocol: Preboot Execution Environment (PXE)/iSCSI.** — iSCSI★ / NONE
    - _PXE_
- [toggle] **MAC Address**
    - _Permanent MAC Address_

## Boot Maintenance Manager  (44 settings)

- [toggle] **Modify system boot options**
    - _Driver Options_
- [toggle] **Modify boot driver options**
- [select] **Change Boot Order** — Delete Boot Option / Add .EFI Driver as Driver Option★
    - _Add Driver Option_
- [select] **Range: 0 to 65535 seconds, 0 means no wait, 65535 means waiting for key** — Delete Boot Option / Driver Options★
    - _Boot Next Value_
- [select] **Delete Driver Option**
    - _Change Driver Order_
- [select] **Modify next boot behavior** — Delete Boot Option★ / Driver Options
    - _Set Time Out Value_
- [select] **Modify automatic boot time-out value** — Delete Boot Option / Driver Options★
    - _Console Options_
- [select] **Will be valid on next boot** — Delete Boot Option★ / Driver Options
    - _Set Boot Next Value_
- [select] **Modify system console options** — Enable console device as ConIn★ / Set Legacy Floppy Drive Order
    - _Console Input Device Select_
- [select] **Set Legacy HardDisk Drive Order** — Delete Boot Option★ / Set Legacy NET Drive Order
    - _Set Legacy CD-ROM Drive Order_
- [select] **Set Legacy BEV Drive Order** — Delete Boot Option★ / Driver Options
    - _Console Output Device Select_
- [number] **Enable console device as ConOut**
    - _Console Standard Error Device Select_
- [number] **Enable console device as StdErr**
    - _Console Output Mode Select_
- [number] **Select Console Output Mode: 80x25, 100x31, etc.**
    - _COM Attribute Setup Page_
- [number] **Setup ComPort BaudRate, DataBits, StopBits, Parity and TerminalType**
    - _Add Driver Option Using File_
- [select] **Add Driver Option Using Handle** — Modify Driver Option Description★ / Auto Boot Time-out
    - _Modify Boot Option Description_
- [select] **Change the order** — Delete Boot Option / Driver Options★
    - _Disabled_
- [select] **File Explorer** — Delete Boot Option / Driver Options★
    - _Hardware_
- [select] **None** — Delete Boot Option / Driver Options★
- [select] **One** — Delete Boot Option / Driver Options★
    - _One And A Half_
- [select] **VT_UTF8** — Delete Boot Option / Driver Options★
    - _Reset System_
- [select] **Go Back To Main Page** — Delete Boot Option★ / Driver Options
    - _Boot From File_
- [select] **Next boot use this boot option** — Delete Boot Option / Driver Options★
    - _Input the description_
- [select] **Load Option Reconnect** — Discard Changes and Exit★ / Set Console Output Mode
    - _Commit Changes and Exit_
- [select] **Set COM Attributes** — Set COM Flow Control★ / Set COM Baud Rate
    - _Set COM Terminal Type_
- [select] **Set COM Data Bits** — Set COM Stop Bits / 115200★ / 57600
    - _Set COM Parity_
- [select] **38400** — Delete Boot Option★ / Driver Options
    - _19200_
- [select] **4800** — Delete Boot Option★ / Driver Options
    - _3600_
- [select] **9600** — Delete Boot Option / Driver Options★ / Will be valid immediately
    - _7200_
- [select] **2400** — Delete Boot Option / Driver Options★
    - _2000_
- [select] **1800** — Delete Boot Option★ / Driver Options
    - _1200_
- [select] **Two** — PC_ANSI / VT_100 / VT_100_PLUS★
- [select] **600** — Delete Boot Option / Driver Options★
    - _300_
- [select] **150** — Delete Boot Option / Driver Options★
    - _134_
- [select] **110** — Delete Boot Option / Driver Options★
    - _75_
- [select] **50** — Delete Boot Option / Driver Options★
    - _5_
- [select] **6** — Delete Boot Option / Driver Options★
    - _7_
- [select] **8** — Delete Boot Option★ / Driver Options
    - _None_
- [select] **Even** — Delete Boot Option / Driver Options★
    - _Odd_
- [select] **Mark** — Delete Boot Option★ / Driver Options
    - _Space_
- [select] **Boot system from a file or device** — Delete Boot Option / Driver Options★
    - _Input Optional Data_
- [number] **Console Input Device Select**
    - _Enable console device as ConIn_
- [select] **Set Legacy Floppy Drive Order** — Set Legacy CD-ROM Drive Order★ / Set Legacy NET Drive Order
    - _Set Legacy HardDisk Drive Order_
- [select] **Esc is pressed. Go to boot options.** — Delete Boot Option

## Boot Options  (8 settings)

- [select] **Change Boot Order** — Add .EFI Driver as Driver Option★ / Delete Driver Option / Change Driver Order
    - _Add Driver Option_
- [select] **Will be valid on next boot** — Change Driver Order / Delete Driver Option / Add .EFI Driver as Driver Option★
    - _Set Boot Next Value_
- [select] **Modify next boot behavior** — Modify automatic boot time-out value / Console Options / Add .EFI Driver as Driver Option★
    - _Set Time Out Value_
- [select] **Modify system console options** — Enable console device as ConIn / Add .EFI Driver as Driver Option★
    - _Console Input Device Select_
- [select] **Set Legacy Floppy Drive Order** — Enable console device as ConIn / Set Legacy CD-ROM Drive Order / Add .EFI Driver as Driver Option★
    - _Set Legacy HardDisk Drive Order_
- [select] **Set Legacy NET Drive Order** — Console Output Device Select★ / Enable console device as ConOut / Console Standard Error Device Select
    - _Set Legacy BEV Drive Order_
- [select] **Select Console Output Mode: 80x25, 100x31, etc.** — Enable console device as ConIn / Set Legacy CD-ROM Drive Order / Add .EFI Driver as Driver Option★
    - _COM Attribute Setup Page_
- [select] **Setup ComPort BaudRate, DataBits, StopBits, Parity and TerminalType** — Enable console device as ConIn / Set Legacy CD-ROM Drive Order / Add .EFI Driver as Driver Option★
    - _Add Driver Option Using File_

## Modify Driver Option Description  (1 settings)

- [toggle] **Load Option Reconnect**

## Console Input Device Select  (13 settings)

- [select] **Console Standard Error Device Select**
    - _Enable console device as StdErr_
- [select] **Console Output Mode Select**
    - _Select Console Output Mode: 80x25, 100x31, etc._
- [select] **2000** — 1200★
    - _1800_
- [select] **Next boot use this boot option** — Load Option Reconnect★ / Commit Changes and Exit
    - _Input the description_
- [select] **Set COM Stop Bits**
    - _115200_
- [select] **57600**
    - _38400_
- [select] **19200**
    - _9600_
- [select] **7200**
    - _4800_
- [select] **Discard Changes and Exit** — Set COM Attributes★ / Set COM Terminal Type
    - _Set Console Output Mode_
- [select] **Set COM Flow Control**
    - _Set COM Baud Rate_
- [select] **Set COM Data Bits**
    - _Set COM Parity_
- [select] **COM Attribute Setup Page**
    - _Setup ComPort BaudRate, DataBits, StopBits, Parity and TerminalType_
- [select] **Reset System**
    - _Go Back To Main Page_

## Set Legacy HardDisk Drive Order  (1 settings)

- [toggle] **Console Output Device Select**
    - _Enable console device as ConOut_

## Geräteparameter konfigurieren.  (64 settings)

- [number] **Bootprotokolle älterer Geräte**
- [select] **Nicht-UEFI Boot-Protokoll auswählen: Preboot Execution Environment (PXE)/iSCSI.** — iSCSI★ / NONE
    - _PXE_
- [select] **Version:** — Permanente MAC-Adresse
    - _^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$_
- [select] **PCI-Adresse** — Primäre DNS
- [select] **Verbindungsstatus** — Permanente MAC-Adresse
    - _Verbunden_
- [select] **Verbindung getrennt** — Permanente MAC-Adresse★
    - _Blinkende LEDs_
- [select] **PCI-Bus:Gerät:Funktionsnummer für dieses Gerät.** — Permanente MAC-Adresse
    - _Verbindungsstatus_
- [select] **Blinkende LEDs für bis zu 15 Sekunden** — Bootprotokolle älterer Geräte★ / Nicht-UEFI Boot-Protokoll auswählen: Preboot Execution Environment (PXE)/iSCSI.
    - _Bootprotokolle älterer Geräte_
- [select] **PXE** — NONE
    - _iSCSI_
- [select] **None** — Permanente MAC-Adresse
    - _Boot-Strap-Typ_
- [number] **Boot-Strap-Typ**
    - _Boot-Strap-Typ auswählen._
- [number] **Übertragungsrate**
- [number] **Übertragungsrate konfigurieren.**
    - _Pre-boot Wake On LAN_
- [number] **Pre-boot Wake On LAN (WOL) konfigurieren**
    - _Wake On LAN_
- [select] **Wake on LAN (WOL) konfigurieren**
- [select] **Ungültiger TCP-Port** — HP Shared-Memory-Funktion deaktivieren / Deaktivieren Sie die Verwendung des reservierten Speichers Regionen zu ermöglichen direkte Zuordnung von Gerät zu virtuellen Gastcomputer. / Das neue Bild wird von diesem Gerät nicht unterstützt. / Nicht genügend Speicherplatz, um das Bild zu speichern. / Die neue Bildversion ist die gleiche wie oder älter als das aktuelle Bild. / Verarbeitungsfehler.★ / Bild:
    - _Ungültige VLAN-ID_
- [select] **Erste iSCSI-Zielparameter** — Permanente MAC-Adresse
- [select] **Erste iSCSI-Zielparameter konfigurieren.** — Permanente MAC-Adresse
    - _Zweite iSCSI-Zielparameter_
- [select] **Zweite iSCSI-Zielparameter** — Permanente MAC-Adresse
- [select] **iSCSI-Name** — CHAP-ID / CHAP-ID konfigurieren (bis zu 32 Zeichen lang) / CHAP-ID konfigurieren (bis zu 128 Zeichen lang) / Permanente MAC-Adresse
    - _iSCSI-Name konfigurieren._
- [select] **CHAP-ID** — CHAP-ID / CHAP-ID konfigurieren (bis zu 32 Zeichen lang) / CHAP-ID konfigurieren (bis zu 128 Zeichen lang)
- [select] **CHAP-ID konfigurieren (bis zu 32 Zeichen lang)** — CHAP-ID / CHAP-ID konfigurieren (bis zu 32 Zeichen lang) / CHAP-ID konfigurieren (bis zu 128 Zeichen lang)
    - _CHAP-ID konfigurieren (bis zu 128 Zeichen lang)_
- [select] **CHAP-Kennwort** — CHAP-Kennwort★ / CHAP-Geheimnis konfigurieren (12 – 16 Zeichen lang) / Permanente MAC-Adresse
- [select] **CHAP-Geheimnis konfigurieren (12 – 16 Zeichen lang)** — CHAP-Kennwort★ / CHAP-Geheimnis konfigurieren (12 – 16 Zeichen lang)
    - _CHAP-Kennwort_
- [select] **Verzögerung nach Verbindungsaufbau in Sekunden (0..255) konfigurieren.** — Permanente MAC-Adresse★ / CHAP-Kennwort
    - _TCP-Zeitstempel verwenden_
- [select] **TCP-Zeitstempel** — Permanente MAC-Adresse★
    - _TCP-Zeitstempel aktivieren/deaktivieren_
- [select] **Ziel als erstes HDD** — Permanente MAC-Adresse★
    - _Ziel erscheint als erstes Festplattenlaufwerk (HDD) im System._
- [select] **Anzahl Wiederholungen bei 'LUN besetzt'** — IP-Version★ / IP-Version-Support. Eine Änderung dieses Parameters setzt alle IP-bezogenen Felder zurück.
    - _Konfiguration der Anzahl der Wiederholungen auf 2 Sekunden wenn LUN besetzt ist (0..60)._
- [select] **iSCSI-Parameter des sekundären Geräts** — Permanente MAC-Adresse
- [select] **Präfix für Subnetzmaske** — Permanente MAC-Adresse
    - _Länge des IP-Präfixes für Subnetzmaske konfigurieren._
- [select] **Standard-Gateway** — Primäre DNS
    - _IP-Adresse des Standard-Gateways konfigurieren_
- [select] **Sekundäre DNS** — Virtuelle MAC-Adresse
    - _Sekundäre DNS-IP-Adresse konfigurieren._
- [select] **IP-Adresse** — Permanente MAC-Adresse★ / MAC-Adresse
    - _Ziel-IP-Adresse konfigurieren._
- [select] **Automatische IP-Konfiguration** — Permanente MAC-Adresse★
    - _TCP/IP-Konfigurationseinstellungen über zustandbehaftete oder zustandslose Autokonfiguration erhalten._
- [select] **Booten von iSCSI-Ziel** — Permanente MAC-Adresse★
    - _Booten von Ziel_
- [select] **Booten von iSCSI-Ziel nach dem Einloggen aktivieren/deaktivieren** — Permanente MAC-Adresse
    - _DHCP Vendor ID_
- [select] **Subnetzmaske** — Permanente MAC-Adresse★ / MAC-Adresse
    - _Subnetzmaske konfigurieren._
- [select] **Virtuellen LAN-Modus** — Permanente MAC-Adresse★
    - _Virtuellen LAN-Modus konfigurieren._
- [select] **VLAN-ID (1..4094)** — Virtuelle LAN-ID (1..4094) konfigurieren.★ / Auto Neg
    - _Virtuelle LAN-ID_
- [select] **10 Mbps Halb** — 100 Mbps Halb★ / 100 Mbps Voll
    - _10 Mbps Voll_
- [select] **Automatische Aushandlung** — 10 Mbps Voll / 100 Mbps Halb★ / 100 Mbps Voll
    - _10 Mbps Halb_
- [select] **Deaktiviert** — Permanente MAC-Adresse
    - _Aktiviert_
- [select] **IPv6** — Permanente MAC-Adresse
    - _MBA-Konfigurationsmenü_
- [select] **Einmalige Deaktivierung** — Permanente MAC-Adresse★ / Chip-Typ
    - _IPv4_
- [select] **MBA-Konfigurationsmenü** — Permanente MAC-Adresse★
    - _Multiple-Boot-Agent-Parameter (MBA) konfigurieren._
- [select] **NIC-Konfiguration** — Permanente MAC-Adresse
- [select] **iSCSI-Parameter über DHCP** — iSCSI-Parameter über DHCP erhalten. / CHAP-Authentifizierung / CHAP-Authentifizierung aktivieren/deaktivieren★
- [select] **iSCSI-Boot-Konfigurationsmenü** — Permanente MAC-Adresse★
- [select] **iSCSI-Bootparameter konfigurieren.** — Permanente MAC-Adresse★
    - _iSCSI-Konfiguration_
- [select] **iSCSI-Konfiguration** — Permanente MAC-Adresse★
    - _Menü Firmware Image_
- [select] **Menü Firmware Image** — Permanente MAC-Adresse★
    - _Firmware-Image-Information_
- [select] **Liste mit Firmware-Image-Komponenten (und den entsprechenden Versionen), die momentan auf dem NVRAM gespeichert sind. Ein Gedankenstrich bedeutet, dass das Image nicht vorhanden ist.** — Permanente MAC-Adresse★
- [select] **Firmware-Image-Eigenschaften** — Permanente MAC-Adresse★
    - _TCP/IP-Parameter über DHCP_
- [select] **TCP/IP-Konfigurationseinstellungen über DHCP erhalten.** — Permanente MAC-Adresse
    - _IP-Autokonfiguration_
- [select] **DHCP Vendor ID konfigurieren (bis zu 32 Bytes lang).** — Permanente MAC-Adresse★
    - _Verzögerung nach Verbindungsaufbau_
- [number] **Zielherstellung aktivieren/deaktivieren.** — Ziel-TCP.Port-Nummer (1..65535) konfigurieren.★ / TCP-Port
    - _Verbinden_
- [select] **Ziel-TCP.Port-Nummer (1..65535) konfigurieren.** — Ziel-Boot-LUN-Nummer (0..255) konfigurieren.★ / Boot-LUN / Sekundäres Gerät / Eingabe der MAC-Adresse des sekundären Geräts. XX:XX:XX:XX:XX:XX-Format verwenden. / MAC-Adresse des sekundären Geräts / Unabhängiges Zielportal verwenden / Unabhängiges Zielportal verwenden wenn Multipath I/O aktiviert ist. / Unabhängigen Zielnamen verwenden / Unabhängigen Zielnamen verwenden wenn Multipath I/O aktiviert ist. / Firmware-Version der Familie / Bootcode / MBA / iSCSI Boot / ASF / NC-SI / SMASH / CCM
    - _Boot-LUN_
- [select] **UMP** — Fcode★ / BIOS-Version des Controllers / MBA / iSCSI Boot / ASF / NC-SI / SMASH / CCM / UMP / EFI-Version / BootCode / Multiple Boot Agent / UEFI – optionales ROM / Fcode – optionales ROM / Management FW
    - _EFI_
- [select] **Configuration ROM** — Allgemeine iSCSI-Parameter★
    - _Hauptkonfigurationsseite_
- [select] **Allgemeine iSCSI-Bootparameter konfigurieren.** — Initiator-iSCSI-Parameter / Chip-Typ★
    - _Initiator-iSCSI-Parameter_
- [select] **Initiator-iSCSI-Parameter konfigurieren.** — Permanente MAC-Adresse
    - _Erste iSCSI-Zielparameter_
- [select] **Zweite iSCSI-Zielparameter konfigurieren.** — Permanente MAC-Adresse★ / Sekundäres Gerät / Parameter des sekundären Geräts konfigurieren.
    - _Sekundäres Gerät_
- [select] **FlexAddressing** — Permanente MAC-Adresse
    - _TX-Bandbreitensteuerung – Maximum_
- [toggle] **MAC-Adresse**
    - _Permanente MAC-Adresse_

## None  (14 settings)

- [select] **RAID** — VGA BIOS Version:★ / System BIOS Version:
    - _ _
- [select] **I2C** — CPU Speed:★ / [Not Detected]
    - _PS2_
- [select] **Touchpad** — CPU Speed:★ / [Not Detected]
    - _Please make sure I2C driver is installed before select to I2C mode. Otherwise, touchpad will be no function._
- [select] **Camera Switch.** — CPU Speed: / 30% / This is Intel VTD function switch★
    - _Fingerprint:_
- [select] **Intel VTX:** — This is Intel VTX function switch / Intel VTD:★
- [select] **Fingerprint Switch.** — CPU Speed: / [Not Detected]★
    - _Type C_
- [select] **Lid Open Resume** — CPU Speed: / EMMC Model Name:★
    - _System will resume from S3 state by Lid open._
- [select] **Exit Saving Changes** — CPU Speed: / EMMC Model Name:★
    - _Exit System Setup and save your changes._
- [select] **USB Wake from S4 Support** — Support USB wake S4
    - _USB Boot:_
- [select] **TBT Wake:** — TBT Wake from S4 Support★ / Support TBT wake from S4 / CPU Speed: / [Not Detected]
    - _Enable/Disable S3 wake capability of TBT_
- [select] **ASF Support** — CPU Speed: / [Not Detected]★
    - _ASF Configuration_
- [select] **ASF Configuration** — CPU Speed: / [Not Detected]★
    - _System Diagnose_
- [select] **Wired Lan Switch.** — CPU Speed: / [Not Detected]★
    - _Optical Drive:_
- [select] **Enable/Disable Optical Drive** — Audio Switch. / Speaker & Headphone:★
    - _Audio:_

## Numéro Bus PCI:Périphérique:Numéro de fonction de ce périphérique.  (2 settings)

- [select] **ID de VLAN (1 à 4094)** — Adresse MAC★ / Adresse MAC permanente
    - _ID de VLAN_
- [select] **Mode VLAN** — Adresse MAC★ / Adresse MAC permanente
    - _Configurer le mode VLAN._

## Mode VLAN  (41 settings)

- [select] **Mode VLAN** — ID de VLAN (1 à 4094) / Bus:Périphérique:Fonction★
    - _Configurer le mode VLAN._
- [number] **ID de VLAN** — Autonégociation / 10 Mbit/s, semi / 10 Mbit/s, intégral★
    - _Configurer l'ID de VLAN (1 à 4094)._
- [number] **Autonégociation**
    - _10 Mbit/s, semi_
- [number] **10 Mbit/s, intégral**
    - _100 Mbit/s, semi_
- [number] **100 Mbit/s, intégral**
    - _Négociation automatique_
- [number] **10 Mbit/s, semi**
    - _10 Mbit/s, intégral_
- [select] **100 Mbit/s, semi** — Protocole de démarrage hérité / ID de VLAN (1 à 4094) / Bus:Périphérique:Fonction★ / Type d'amorçage / None
    - _100 Mbit/s, intégral_
- [number] **Désactivé**
    - _Activé_
- [number] **Désactivé une fois**
    - _IPv4_
- [number] **IPv6**
    - _Menu de configuration MBA_
- [select] **Menu de configuration MBA** — Protocole de démarrage hérité / ID de VLAN (1 à 4094) / Bus:Périphérique:Fonction★
    - _Configurer les paramètres MBA._
- [number] **Configuration de la carte réseau** — Menu de configuration du démarrage iSCSI★ / Configuration iSCSI / Configurer les paramètres de démarrage iSCSI.
- [number] **Menu de configuration du démarrage iSCSI**
- [number] **Configurer les paramètres de démarrage iSCSI.**
    - _Configuration iSCSI_
- [select] **Configuration iSCSI** — Protocole de démarrage hérité / ID de VLAN (1 à 4094) / Bus:Périphérique:Fonction★
    - _Menu Image de micrologiciel_
- [number] **Menu Image de micrologiciel**
    - _Informations sur l'image du microprogramme ._
- [number] **Liste des composants de l'image du micrologiciel (et des versions correspondantes) actuellement programmés sur la mémoire NVRAM. N/A indique qu'il n'y a pas d'image.**
- [select] **Propriétés de l'image du microprogramme** — Protocole de démarrage hérité / ID de VLAN (1 à 4094) / Bus:Périphérique:Fonction★
    - _Paramètres TCP/IP via DHCP_
- [number] **Acquérir la configuration TCP/IP via DHCP.**
    - _Configuration IP automatique_
- [number] **Configuration automatique de l'IP**
    - _Acquérir la configuration TCP/IP via la configuration automatique avec état ou sans état._
- [number] **Paramètres iSCSI via DHCP**
    - _Acquérir les paramètres iSCSI via DHCP._
- [select] **Authentification CHAP** — Protocole de démarrage hérité / ID de VLAN (1 à 4094) / Bus:Périphérique:Fonction★
    - _Activer/Désactiver l'authentification CHAP._
- [number] **Démarrer depuis la cible iSCSI**
    - _Démarrer depuis la cible_
- [number] **Activer/Désactiver le démarrage depuis la cible iSCSI après l'ouverture de la session.**
    - _Réf. fournisseur DHCP_
- [number] **Configurer la référence fournisseur DHCP (jusqu'à 32 octets).**
    - _Durée d'établissement de la liaison_
- [select] **Configurer la durée d'établissement de la liaison en secondes (0 à 255).** — Protocole de démarrage hérité / ID de VLAN (1 à 4094) / Bus:Périphérique:Fonction★
    - _Utiliser l'horodatage TCP_
- [number] **Horodatage TCP**
    - _Activer/Désactiver l'horodatage TCP._
- [number] **Cibler comme premier disque dur**
    - _Activer/Désactiver l'apparition de la cible comme premier disque dur dans le système._
- [number] **Nombre d'essais de connexion à une unité logique occupée**
    - _Configurer le nombre d'essais à 2 secondes d'intervalle lorsque l'unité logique est occupée (0 à 60)._
- [select] **IP Version** — Protocole de démarrage hérité / ID de VLAN (1 à 4094) / Bus:Périphérique:Fonction★
    - _Prise en charge d'IP Version. La modification de ce paramètre réinitialisera tous les champs relatifs à l'adresse IP._
- [number] **Adresse IP**
    - _Configurer l'adresse IP de l'initiateur._
- [select] **Masque de sous-réseau** — Protocole de démarrage hérité / iSCSI / Bus:Périphérique:Fonction★
    - _Configurer le masque du sous-réseau de l'adresse IP._
- [select] **Utiliser le portail cible indépendant lorsque les E/S multivoies sont activées.** — Utiliser le portail cible indépendant / Adresse MAC du périphérique secondaire d'entrée. Utiliser le format XX:XX:XX:XX:XX:XX.★
    - _Utiliser le nom de cible indépendante_
- [select] **EFI** — Version du BIOS du contrôleur★ / MBA
    - _Fcode_
- [select] **00:00:00:00:00:00** — ID du périphérique PCI★
- [toggle] **Configurer la séquence de touches**
    - _Configurer la séquence de touches permettant d'appeler le menu de configuration._
- [toggle] **Ctrl-S**
    - _Ctrl-B_
- [toggle] **Délai d'inactivité du message de bannière**
- [toggle] **Sélectionner une valeur pour le délai d'inactivité. (0 : par défaut, 4 secondes ; 15 : aucun délai ; 1-14 : valeur du délai d'inactivité en secondes)**
    - _BRCM ISAN_
- [toggle] **0.0.0.0**
    - _iqn.1995-05.com.broadcom.iscsiboot_
- [toggle] **Adresse MAC** — Adresse MAC★

## 10 Mbit/s, intégral  (2 settings)

- [select] **IPv4** — Bus:Périphérique:Fonction★ / Type de puce/Révision.
    - _IPv6_
- [select] **Configuration iSCSI** — Bus:Périphérique:Fonction★ / Type de puce/Révision.

## SATA Port 1     (2 settings)

- [number] **  Fermer   **
    - _  Unfermer  _
- [number] **  Lock    **
    - _  Unlock  _

## SATA Port 3     (7 settings)

- [select] **Press [ESC] Abort Harddisk Security** — Enter incorrect password 3 times★ / Please press Enter to continue / [ENTER]
    - _Harddisk Security_
- [select] **Error Status** — [ENTER] / Please press Enter to continue / Enter incorrect password 3 times★
    - _Enter incorrect password too many times_
- [select] **HDD Security count expired bit is acted** — Please input password for  / Enter incorrect password 3 times★ / Password check Fail!!
    - _Please shutdown the system_
- [select] **Press any key** — HDD0           / Enter incorrect password 3 times★
    - _HDD           _
- [select] **HDD1          ** — HDD0           / HDD3           / Enter incorrect password 3 times★
    - _HDD2          _
- [select] **HDD4          ** — HDD0(OPAL)    ★ / HDD1(OPAL)     / HDD2(OPAL)    
    - _HDD(OPAL)     _
- [select] **Press Esc for boot options** — HDD0           / HDD3           / Enter incorrect password 3 times★
    - _Esc is pressed. Go to boot options._

## PID for PSK  (2 settings)

- [select] **Hash2 Value**
    - _Set or change DASH second PKI hash value_
- [select] **Set or change DASH sixth PKI hash value** — FQDN★ / Set or change DASH PKI FQDN / PKI DNS Suffix
    - _Please Input Password_

## Configurer les paramètres du périphérique.  (64 settings)

- [number] **Protocole de démarrage hérité**
- [select] **Sélectionner un protocole de démarrage non UEFI : environnement d'exécution pré-démarrage (PXE)/iSCSI.** — iSCSI★ / NONE
    - _PXE_
- [select] **Version :** — Adresse MAC permanente
    - _^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$_
- [select] **Adresse PCI** — Serveur DNS principal
- [select] **Etat de la liaison** — Adresse MAC permanente
    - _Connecté_
- [select] **Déconnecté** — Adresse MAC permanente★
    - _Clignotement des voyants_
- [select] **Numéro Bus PCI:Périphérique:Numéro de fonction de ce périphérique.** — Adresse MAC permanente
    - _Etat de la liaison_
- [select] **Fait clignoter les voyants pendant une durée de 15 secondes.** — Protocole de démarrage hérité★ / Sélectionner un protocole de démarrage non UEFI : environnement d'exécution pré-démarrage (PXE)/iSCSI.
    - _Protocole de démarrage hérité_
- [select] **PXE** — NONE
    - _iSCSI_
- [select] **None** — Adresse MAC permanente
    - _Type d'amorçage_
- [number] **Type d'amorçage**
    - _Sélectionner le type d'amorçage._
- [number] **Vitesse de liaison**
- [number] **Configurer la vitesse de liaison.**
    - _Réveil sur LAN au pré-démarrage_
- [number] **Configurer le réveil sur LAN au pré-démarrage.**
    - _Réveil sur LAN_
- [select] **Configurer le réseau local de réveil.**
- [select] **Port TCP non valide** — Désactiver la fonction de mémoire partagée HP / Désactiver l'utilisation de régions de mémoire réservée pour permettre l'affectation directe de périphérique pour les ordinateurs virtuels invités. / La nouvelle image n'est pas prise en charge par le périphérique. / Espace insuffisant pour stocker l'image. / La nouvelle version de l'image est identique ou plus ancienne que l'image en cours. / Erreur de traitement★ / Image :
    - _ID de VLAN non valide_
- [select] **Paramètres de la première cible iSCSI** — Adresse MAC permanente
- [select] **Configurer les paramètres de la première cible iSCSI.** — Adresse MAC permanente
    - _Paramètres de la deuxième cible iSCSI_
- [select] **Paramètres de la deuxième cible iSCSI** — Adresse MAC permanente
- [select] **Nom iSCSI** — Réf. CHAP / Configurer la réf. CHAP (jusqu'à 32 caractères). / Configurer la réf. CHAP (jusqu'à 128 caractères). / Adresse MAC permanente
    - _Configurer le nom iSCSI._
- [select] **Réf. CHAP** — Réf. CHAP / Configurer la réf. CHAP (jusqu'à 32 caractères). / Configurer la réf. CHAP (jusqu'à 128 caractères).
- [select] **Configurer la réf. CHAP (jusqu'à 32 caractères).** — Réf. CHAP / Configurer la réf. CHAP (jusqu'à 32 caractères). / Configurer la réf. CHAP (jusqu'à 128 caractères).
    - _Configurer la réf. CHAP (jusqu'à 128 caractères)._
- [select] **Clé secrète CHAP** — Clé secrète CHAP★ / Configurer la clé secrète CHAP (12 à 16 caractères). / Adresse MAC permanente
- [select] **Configurer la clé secrète CHAP (12 à 16 caractères).** — Clé secrète CHAP★ / Configurer la clé secrète CHAP (12 à 16 caractères).
    - _Clé secrète CHAP_
- [select] **Configurer la durée d'établissement de la liaison en secondes (0 à 255).** — Adresse MAC permanente★ / Clé secrète CHAP
    - _Utiliser l'horodatage TCP_
- [select] **Horodatage TCP** — Adresse MAC permanente★
    - _Activer/Désactiver l'horodatage TCP._
- [select] **Cibler comme premier disque dur** — Adresse MAC permanente★
    - _Activer/Désactiver l'apparition de la cible comme premier disque dur dans le système._
- [select] **Nombre d'essais de connexion à une unité logique occupée** — IP Version★ / Prise en charge d'IP Version. La modification de ce paramètre réinitialisera tous les champs relatifs à l'adresse IP.
    - _Configurer le nombre d'essais à 2 secondes d'intervalle lorsque l'unité logique est occupée (0 à 60)._
- [select] **Paramètres iSCSI du périphérique secondaire** — Adresse MAC permanente
- [select] **Préfixe du masque de sous-réseau** — Adresse MAC permanente
    - _Configurer la longueur du préfixe du masque de sous-réseau de l'adresse IP._
- [select] **Passerelle par défaut** — Serveur DNS principal
    - _Configurer l'adresse IP de la passerelle par défaut._
- [select] **Serveur DNS secondaire** — Adresse MAC virtuelle
    - _Configurer l'adresse IP du serveur DNS secondaire._
- [select] **Adresse IP** — Adresse MAC permanente★ / Adresse MAC
    - _Configurer l'adresse IP de la cible._
- [select] **Configuration automatique de l'IP** — Adresse MAC permanente★
    - _Acquérir la configuration TCP/IP via la configuration automatique avec état ou sans état._
- [select] **Démarrer depuis la cible iSCSI** — Adresse MAC permanente★
    - _Démarrer depuis la cible_
- [select] **Activer/Désactiver le démarrage depuis la cible iSCSI après l'ouverture de la session.** — Adresse MAC permanente
    - _Réf. fournisseur DHCP_
- [select] **Masque de sous-réseau** — Adresse MAC permanente★ / Adresse MAC
    - _Configurer le masque du sous-réseau de l'adresse IP._
- [select] **Mode VLAN** — Adresse MAC permanente★
    - _Configurer le mode VLAN._
- [select] **ID de VLAN (1 à 4094)** — Configurer l'ID de VLAN (1 à 4094).★ / Autonégociation
    - _ID de VLAN_
- [select] **10 Mbit/s, semi** — 100 Mbit/s, semi★ / 100 Mbit/s, intégral
    - _10 Mbit/s, intégral_
- [select] **Négociation automatique** — 10 Mbit/s, intégral / 100 Mbit/s, semi★ / 100 Mbit/s, intégral
    - _10 Mbit/s, semi_
- [select] **Désactivé** — Adresse MAC permanente
    - _Activé_
- [select] **IPv6** — Adresse MAC permanente
    - _Menu de configuration MBA_
- [select] **Désactivé une fois** — Adresse MAC permanente★ / Type de puce
    - _IPv4_
- [select] **Menu de configuration MBA** — Adresse MAC permanente★
    - _Configurer les paramètres MBA._
- [select] **Configuration de la carte réseau** — Adresse MAC permanente
- [select] **Paramètres iSCSI via DHCP** — Acquérir les paramètres iSCSI via DHCP. / Authentification CHAP / Activer/Désactiver l'authentification CHAP.★
- [select] **Menu de configuration du démarrage iSCSI** — Adresse MAC permanente★
- [select] **Configurer les paramètres de démarrage iSCSI.** — Adresse MAC permanente★
    - _Configuration iSCSI_
- [select] **Configuration iSCSI** — Adresse MAC permanente★
    - _Menu Image de micrologiciel_
- [select] **Menu Image de micrologiciel** — Adresse MAC permanente★
    - _Informations sur l'image du microprogramme ._
- [select] **Liste des composants de l'image du micrologiciel (et des versions correspondantes) actuellement programmés sur la mémoire NVRAM. N/A indique qu'il n'y a pas d'image.** — Adresse MAC permanente★
- [select] **Propriétés de l'image du microprogramme** — Adresse MAC permanente★
    - _Paramètres TCP/IP via DHCP_
- [select] **Acquérir la configuration TCP/IP via DHCP.** — Adresse MAC permanente
    - _Configuration IP automatique_
- [select] **Configurer la référence fournisseur DHCP (jusqu'à 32 octets).** — Adresse MAC permanente★
    - _Durée d'établissement de la liaison_
- [number] **Activer/Désactiver l'établissement de la cible.** — Configurer le numéro du port TCP de la cible (1 à 65 535).★ / Port TCP
    - _Connecter_
- [select] **Configurer le numéro du port TCP de la cible (1 à 65 535).** — Configurer le numéro d'unité logique de démarrage cible (0 à 255).★ / Unité logique de démarrage / Périphérique secondaire / Adresse MAC du périphérique secondaire d'entrée. Utiliser le format XX:XX:XX:XX:XX:XX. / Adresse MAC du périphérique secondaire / Utiliser le portail cible indépendant / Utiliser le portail cible indépendant lorsque les E/S multivoies sont activées. / Utiliser le nom de cible indépendante / Utiliser le nom de cible indépendante lorsque les E/S multivoies sont activées. / Version du microprogramme famille / Code de démarrage / MBA / Initialisation iSCSI / ASF / NC-SI / SMASH / CCM
    - _Unité logique de démarrage_
- [select] **UMP** — Fcode★ / Version du BIOS du contrôleur / MBA / Initialisation iSCSI / ASF / NC-SI / SMASH / CCM / UMP / Version EFI / Code d'initialisation / Multiple Boot Agent / ROM en option UEFI / ROM en option Fcode / Micrologiciel de gestion
    - _EFI_
- [select] **ROM de configuration** — Paramètres généraux iSCSI★
    - _Page de configuration principale_
- [select] **Configurer les paramètres généraux iSCSI de démarrage.** — Paramètres de l'initiateur iSCSI / Type de puce★
    - _Paramètres de l'initiateur iSCSI_
- [select] **Configurer les paramètres de l'initiateur iSCSI.** — Adresse MAC permanente
    - _Paramètres de la première cible iSCSI_
- [select] **Configurer les paramètres de la deuxième cible iSCSI.** — Adresse MAC permanente★ / Périphérique secondaire / Configurer les paramètres du périphérique secondaire.
    - _Périphérique secondaire_
- [select] **AdressageFlex** — Adresse MAC permanente
    - _Maximale pour contrôle de la bande passante TX_
- [toggle] **Adresse MAC**
    - _Adresse MAC permanente_

## F9=￱デフォルト設定へ戻す￰  (3 settings)

- [select] **N**
    - _￱文字数が足りません￰_
- [select] **￱変更を保存しました￰**
    - _[￱継続￰]_
- [select] **Setup Warning**
    - _￱設定注意事項￰_

## ￱よろしいですか￰? (Y/N)  (1 settings)

- [toggle] **￱変更を保存しました￰**

## On  (3 settings)

- [select] **<Enter>=Select Entry** — =Move Highlight★ /  =Select From Choices
    - _<Enter>=Complete Entry_
- [select] **Esc=Exit Entry** — =Move Highlight★ /  =Select From Choices
    - _Esc=Discard Changes_
- [select] **Failed to Save** — =Move Highlight★ /  =Select From Choices
    - _+/- =Adjust Value_

## F9=Reset to Defaults  (3 settings)

- [select] **N** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>★ / <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='20'><VerticalLayout width='160' childpadding='4'><Button name='month_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='month' text='1' fontsize='38' align='center' readonly='true' /><Button name='month_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><VerticalLayout width='160' childpadding='4'><Button name='day_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='day' fontsize='38' align='center' readonly='true'/><Button name='day_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><VerticalLayout width='234' childpadding='4'><Button name='year_up' width='234' height='38' normalimage='@TimeDate2UpNormal' hotimage='@TimeDate2UpNormal' pushimage='@TimeDate2UpPush' /><UiEdit name='year' fontsize='38' align='center' readonly='true'/><Button name='year_down' width='234'  height='38' normalimage='@TimeDate2DownNormal' hotimage='@TimeDate2DownNormal' pushimage='@TimeDate2DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='cancel' fontsize='24' /></HorizontalLayout></VerticalLayout>
    - _Please enter enough characters_
- [select] **Changes have been saved.** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='16,28,16,28' ><Label name='title' height='60' align='center' fontsize='40' textcolor='0xFFFFFF' /><VerticalLayout vscrollbar='true' ><Label name='showstring' fontsize='20' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout  name='content' height='30' /></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _[continue]_
- [select] **Setup Warning** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='16,28,16,28' ><Label name='title' height='60' align='center' fontsize='40' textcolor='0xFFFFFF' /><VerticalLayout vscrollbar='true' ><Label name='showstring' fontsize='20' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout  name='content' height='30' /></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _Setup Notice_

## Are you sure? (Y/N)  (1 settings)

- [toggle] **Changes have been saved.**

##                                                                                     (1 settings)

- [toggle] **Esc is pressed. Go to boot options.**

## Configurar parámetros de dispositivo.  (64 settings)

- [number] **Protocolo de arranque heredado**
- [select] **Seleccionar protocolo de arranque no UEFI: Entorno de ejecución de arranque previo (PXE)/iSCSI.** — iSCSI★ / NADA
    - _PXE_
- [toggle] **Dirección MAC**
    - _Dirección MAC permanente_
- [select] **Versión:** — Dirección MAC permanente
    - _^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$_
- [select] **Dirección PCI** — DNS primario
- [select] **Estado del enlace** — Dirección MAC permanente
    - _Conectado_
- [select] **Desconectado** — Dirección MAC permanente★
    - _LED intermitentes_
- [select] **PCI Bus:Dispositivo:Número de función de este dispositivo.** — Dirección MAC permanente
    - _Estado del enlace_
- [select] **LED intermitentes con una duración de hasta 15 segundos.** — Protocolo de arranque heredado★ / Seleccionar protocolo de arranque no UEFI: Entorno de ejecución de arranque previo (PXE)/iSCSI.
    - _Protocolo de arranque heredado_
- [select] **PXE** — NADA
    - _iSCSI_
- [select] **Nada** — Dirección MAC permanente
    - _Tipo de autocarga_
- [number] **Tipo de autocarga**
    - _Seleccionar tipo de autocarga._
- [number] **Velocidad de enlace**
- [number] **Configurar velocidad de enlace.**
    - _Wake on LAN (WOL) (LAN de reactivación) previa al inicio del sistema_
- [number] **Configurar Wake on LAN (WOL) (LAN de reactivación) previa al inicio del sistema.**
    - _Wake on LAN (WOL) (LAN de reactivación)_
- [select] **Configurar Wake on LAN (WOL, LAN de reactivación))**
- [select] **Puerto TCP no válido** — Desactivar función de memoria compartida de HP / Desactivar el uso de regiones de memoria reservada para permitir la asignación directa de dispositivo para las máquinas virtuales invitadas. / La nueva imagen no se admite en este dispositivo. / Espacio insuficiente para almacenar la imagen. / La versión de la nueva imagen es la misma o anterior que la de la imagen actual. / Error de procesamiento.★ / Imagen:
    - _ID de VLAN no válido_
- [select] **Parámetros de primer destino de iSCSI** — Dirección MAC permanente
- [select] **Configurar parámetros de primer destino de iSCSI.** — Dirección MAC permanente
    - _Parámetros de segundo destino de iSCSI_
- [select] **Parámetros de segundo destino de iSCSI** — Dirección MAC permanente
- [select] **Nombre de iSCSI** — ID CHAP / Configurar identificación CHAP (hasta 32 caracteres de longitud). / Configurar identificación CHAP (hasta 128 caracteres de longitud). / Dirección MAC permanente
    - _Configurar nombre de iSCSI._
- [select] **ID CHAP** — ID CHAP / Configurar identificación CHAP (hasta 32 caracteres de longitud). / Configurar identificación CHAP (hasta 128 caracteres de longitud).
- [select] **Configurar identificación CHAP (hasta 32 caracteres de longitud).** — ID CHAP / Configurar identificación CHAP (hasta 32 caracteres de longitud). / Configurar identificación CHAP (hasta 128 caracteres de longitud).
    - _Configurar identificación CHAP (hasta 128 caracteres de longitud)._
- [select] **Secreto CHAP** — Secreto CHAP★ / Configurar secreto CHAP (entre 12 y 16 caracteres de longitud). / Dirección MAC permanente
- [select] **Configurar secreto CHAP (entre 12 y 16 caracteres de longitud).** — Secreto CHAP★ / Configurar secreto CHAP (entre 12 y 16 caracteres de longitud).
    - _Secreto CHAP_
- [select] **Configurar el tiempo de retraso de conexión en segundos (0..255).** — Dirección MAC permanente★ / Secreto CHAP
    - _Utilizar marca de hora TCP_
- [select] **Sello de tiempo TCP** — Dirección MAC permanente★
    - _Habilitar/Deshabilitar marca de hora TCP._
- [select] **Destino como primera HDD** — Dirección MAC permanente★
    - _Habilitar/Deshabilitar la aparición del destino como primera unidad de disco duro (HDD) en el sistema._
- [select] **Conteo de reintentos con LUN ocupado** — Versión de IP★ / Compatibilidad con la versión de IP. Al modificar este parámetro se restablecerán todos los campos relacionados con la IP.
    - _Configurar el número de reintentos en intervalos de 2 segundos cuando el número de unidad lógica (LUN) está ocupado (0..60)._
- [select] **Parámetros de dispositivo secundario iSCSI** — Dirección MAC permanente
- [select] **Prefijo de máscara de subred** — Dirección MAC permanente
    - _Configurar longitud de prefijo de máscara de subred de IP._
- [select] **Puerta de enlace predeterminada** — DNS primario
    - _Configurar dirección IP de puerta de enlace predeterminada._
- [select] **DNS secundario** — Dirección MAC virtual
    - _Configurar dirección IP del DNS secundario._
- [select] **Dirección IP** — Dirección MAC permanente★ / Dirección MAC
    - _Configurar dirección IP de destino._
- [select] **Configuración auto. de IP** — Dirección MAC permanente★
    - _Adquirir configuración de TCP/IP a través de configuración automática con estado o sin estado._
- [select] **Arranque en destino iSCSI** — Dirección MAC permanente★
    - _Arranque en destino_
- [select] **Habilitar/Deshabilitar arranque en destino iSCSI tras el inicio de sesión.** — Dirección MAC permanente
    - _ID de proveedor DHCP_
- [select] **Máscara de subred** — Dirección MAC permanente★ / Dirección MAC
    - _Configurar máscara de subred de IP._
- [select] **Modo LAN virtual** — Dirección MAC permanente★
    - _Configurar modo LAN virtual._
- [select] **ID de VLAN (1..4094)** — Configurar ID de LAN virtual (1..4094).★ / AutoNeg
    - _ID de LAN virtual_
- [select] **10 Mbps media** — 100 Mbps media★ / 100 Mbps llena
    - _10 Mbps llena_
- [select] **Negociación auto.** — 10 Mbps llena / 100 Mbps media★ / 100 Mbps llena
    - _10 Mbps media_
- [select] **Deshabilitado** — Dirección MAC permanente
    - _Habilitado_
- [select] **IPv6** — Dirección MAC permanente
    - _Menú de configuración MBA_
- [select] **Un solo uso desactivado** — Dirección MAC permanente★ / Tipo de chip
    - _IPv4_
- [select] **Menú de configuración MBA** — Dirección MAC permanente★
    - _Configurar parámetros de Multiple Boot Agent (MBA)._
- [select] **Configuración NIC** — Dirección MAC permanente
- [select] **Parámetros de iSCSI a través de DHCP** — Adquirir parámetros de iSCSI a través de DHCP. / Autenticación CHAP / Habilitar/Deshabilitar autenticación CHAP.★
- [select] **Menú de configuración de arranque iSCSI** — Dirección MAC permanente★
- [select] **Configurar parámetros de arranque iSCSI.** — Dirección MAC permanente★
    - _Configuración iSCSI_
- [select] **Configuración iSCSI** — Dirección MAC permanente★
    - _Menú de imagen de firmware_
- [select] **Menú de imagen de firmware** — Dirección MAC permanente★
    - _Información de imagen del firmware._
- [select] **Listado de componentes de imagen de firmware (y sus versiones correspondientes) programados actualmente en NVRAM. N/A indica que la imagen no está presente.** — Dirección MAC permanente★
- [select] **Propiedades de imagen del firmware** — Dirección MAC permanente★
    - _Parámetros de TCP/IP a través de DHCP_
- [select] **Adquirir configuración de TCP/IP a través de DHCP.** — Dirección MAC permanente
    - _Configuración automática de IP_
- [select] **Configurar ID de proveedor DHCP (hasta 32 bytes de longitud).** — Dirección MAC permanente★
    - _Tiempo de retraso de conexión_
- [number] **Habilitar/Deshabilitar establecimiento de destino.** — Configurar número de puerto TCP de destino (1..65535).★ / Puerto TCP
    - _Conectar_
- [select] **Configurar número de puerto TCP de destino (1..65535).** — Configurar número LUN de arranque de destino (0..255).★ / LUN de arranque / Dispositivo secundario / Introducir dirección MAC de dispositivo secundario. Utilizar formato XX:XX:XX:XX:XX:XX. / Dirección MAC de dispositivo secundario / Utilizar portal de destino independiente / Utilizar portal de destino independiente cuando esté habilitada la E/S de múltiples rutas. / Utilizar nombre de destino independiente / Utilizar nombre de destino independiente cuando esté habilitada la E/S de múltiples rutas. / Versión del firmware de familia / Código de arranque / MBA / Arranque iSCSI / ASF / NC-SI / SMASH / CCM
    - _LUN de arranque_
- [select] **UMP** — Fcode★ / Versión BIOS del controlador / MBA / Arranque iSCSI / ASF / NC-SI / SMASH / CCM / UMP / Versión EFI / Bootcode / Multiple Boot Agent / Opción UEFI ROM / Opción Fcode ROM / Administración FW
    - _EFI_
- [select] **Configuración ROM** — Parámetros generales de iSCSI★
    - _Página de configuración principal_
- [select] **Configurar parámetros generales de arranque iSCSI.** — Parámetros de iniciador de iSCSI / Tipo de chip★
    - _Parámetros de iniciador de iSCSI_
- [select] **Configurar parámetros de iniciador de iSCSI.** — Dirección MAC permanente
    - _Parámetros de primer destino de iSCSI_
- [select] **Configurar parámetros de segundo destino iSCSI.** — Dirección MAC permanente★ / Dispositivo secundario / Configurar parámetros de dispositivo secundario.
    - _Dispositivo secundario_
- [select] **Dirección flexible** — Dirección MAC permanente
    - _Control de banda ancha TX máximo_

## Realtek Ethernet Controller  (3 settings)

- [select] **Configuration Menu** — Driver Version:★ / %s
    - _Advanced Settings_
- [select] **Configure Realtek ethernet controller parameter** — Driver Version:★ / %s
- [select] **Driver Information** — Driver Version:★ / %s
    - _Realtek UEFI UNDI driver information_

## AMD CBS Setup Page  (75 settings)

- [select] **RedirectForReturnDis** — Combo CBS / Auto★
    - _From a workaround for GCC/C000005 issue for XV Core on CZ A0, setting MSRC001_1029 Decode Configuration (DE_CFG) bit 14 [DecfgNoRdrctForReturns] to 1_
- [select] **Decline** — Combo CBS / UMC Common Options★
    - _Accept_
- [select] **32h Clk** — Combo CBS★ / UMC Common Options
    - _33h Clk_
- [select] **1** — Downcore control
    - _0_
- [select] **Platform First Error Handling** — Combo CBS★ / UMC Common Options
    - _Enable/disable PFEH, cloak individual banks, and mask deferred error interrupts from each bank._
- [select] **Enable** — Combo CBS / UMC Common Options★
    - _Disable_
- [select] **L2 TLB Associativity** — Combo CBS★ / UMC Common Options
    - _0 - L2 TLB ways [11:8] are fully associative.  1 - =L2 TLB ways [11:8] are 4K-only._
- [select] **Core Performance Boost** — Disabled★ / Global C-state Control
    - _Disable CPB_
- [select] **Controls IO based C-state generation and DF C-states.** — Combo CBS★ / OC Mode
    - _Enabled_
- [select] **No help string** — Combo CBS★ / UMC Common Options
    - _Normal Operation_
- [number] **OC1**
    - _Customized_
- [number] **Custom Pstates / Throttling**
    - _Core/Thread Enablement_
- [number] **Streaming Stores Control**
    - _Enables or disables the streaming stores functionality_
- [number] **Enable IBS**
    - _When IBS is enabled, SpecLockMap and Stack Engine are disabled._
- [select] **WARNING - DAMAGE CAUSED BY USE OF YOUR AMD PROCESSOR OUTSIDE OF SPECIFICATION OR IN EXCESS OF FACTORY SETTINGS ARE NOT COVERED UNDER YOUR AMD PRODUCT WARRANTY AND MAY NOT BE COVERED BY YOUR SYSTEM MANUFACTURER'S WARRANTY.** — Operating your AMD processor outside of specification or in excess of factory settings, including but not limited to overclocking, may damage or shorten the life of your processor or other system components, create system instabilities (e.g., data loss and corrupted images) and in extreme cases may result in total system failure. AMD does not provide support or service for issues or damages related to use of an AMD processor outside of processor specifications or in excess of factory settings.★ / Legal Disclaimer
    - _Legal Disclaimer_
- [select] **22h Clk** — 24h Clk / 25h Clk / 26h Clk / 27h Clk / 28h Clk / 29h Clk★ / 2Ah Clk / 2Bh Clk / 2Ch Clk / 2Dh Clk / 2Eh Clk / 2Fh Clk / 30h Clk / 31h Clk
    - _23h Clk_
- [select] **1900MHz** — Combo CBS★ / UMC Common Options
    - _1933MHz_
- [select] **1967MHz** — Combo CBS★ / UMC Common Options
    - _2000MHz_
- [select] **333MHz** — Combo CBS★ / UMC Common Options / 48 hours / Redirect scrubber control / Control DF::RedirScrubCtrl[EnRedirScrub] / Disable DF sync flood propagation / Control DF::PIEConfig[DisSyncFloodProp] / Sync flood disabled / Sync flood enabled / GMI encryption control
    - _400MHz_
- [select] **Provide a value that is the number of hours to scrub memory.** — Combo CBS★ / 48 hours / Redirect scrubber control / Control DF::RedirScrubCtrl[EnRedirScrub] / Disable DF sync flood propagation
    - _1 hour_
- [select] **4 hours** — Combo CBS★ / 48 hours / Redirect scrubber control / Control DF::RedirScrubCtrl[EnRedirScrub] / Disable DF sync flood propagation
    - _8 hours_
- [select] **16 hours** — Combo CBS★ / 48 hours / Redirect scrubber control / Control DF::RedirScrubCtrl[EnRedirScrub] / Disable DF sync flood propagation
    - _24 hours_
- [select] **xGMI encryption control** — Control whether or not the CC6 save/restore memory is encrypted★ / Location of private memory regions
    - _CC6 memory region encryption_
- [select] **Control xGMI link encryption** — Control whether or not the CC6 save/restore memory is encrypted★ / Location of private memory regions
    - _CC6 memory region encryption_
- [select] **Custom Pstate6** — Combo CBS / UMC Common Options★ / Control GMI link encryption
- [select] **Pstate6 FID** — Combo CBS / UMC Common Options★
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [select] **Pstate6 DID** — Combo CBS / UMC Common Options★
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [select] **Pstate6 VID** — Combo CBS / Custom Pstate7★
    - _Specifies the core voltage._
- [select] **2067MHz** — Combo CBS★ / UMC Common Options
    - _2100MHz_
- [select] **WARNING - S3 is NOT SUPPORTED on systems where cores/threads have been removed/disabled.** — Combo CBS★ / UMC Common Options
    - _Legal Disclaimer_
- [select] **Disagree** — Downcore control
    - _Agree_
- [select] **ONE** — Combo CBS★ / NBIO Common Options / FCH Common Options / Promontory Common Options
    - _TWO_
- [select] **Pstate7 VID** — Combo CBS / UMC Common Options★ / DF Common Options
    - _Specifies the core voltage._
- [select] **Pstate4 DID** — Combo CBS / UMC Common Options★
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [select] **Pstate5 FID** — Combo CBS / UMC Common Options★
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [select] **Pstate5 DID** — Combo CBS★ / UMC Common Options
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [select] **Relaxed EDC throttling** — Combo CBS / UMC Common Options★ / DF Common Options
- [select] **THREE** — Combo CBS★ / UMC Common Options
    - _SMTEN_
- [select] **Pstate7 FID** — Combo CBS / UMC Common Options★
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [select] **Pstate7 DID** — Combo CBS / UMC Common Options★
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [select] **Custom Pstate0** — Combo CBS / UMC Common Options★
- [select] **Custom** — Current core frequency in MHz★ / Voltage (uV)
    - _Frequency (MHz)_
- [select] **Voltage in uV (1V = 1000 * 1000 uV)** — Specifies the core frequency multiplier. COF = 200MHz * FID / DID★ / Pstate0 DID
    - _Pstate0 FID_
- [select] **Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah).** — Specifies the core voltage. / Custom Pstate1★
    - _Pstate0 VID_
- [select] **Pstate1 FID** — Combo CBS★ / UMC Common Options
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [select] **Pstate1 VID** — Combo CBS★ / UMC Common Options
    - _Specifies the core voltage._
- [select] **Pstate1 DID** — Combo CBS / UMC Common Options★ / No help string
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [select] **Custom Pstate2** — Combo CBS / UMC Common Options★
- [select] **Pstate2 FID** — Combo CBS★ / UMC Common Options
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [select] **Pstate4 VID** — Specifies the core voltage. / Custom Pstate5
- [select] **Pstate2 DID** — Combo CBS / UMC Common Options★
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [select] **Pstate2 VID** — Combo CBS / UMC Common Options★
    - _Specifies the core voltage._
- [select] **Custom Pstate3** — Combo CBS / UMC Common Options★
- [select] **Pstate3 FID** — Combo CBS / UMC Common Options★
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [select] **Pstate3 DID** — Combo CBS / UMC Common Options★
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [select] **Pstate3 VID** — Combo CBS★ / UMC Common Options
    - _Specifies the core voltage._
- [select] **Custom Pstate4** — Combo CBS / UMC Common Options★
- [select] **Pstate4 FID** — Combo CBS★ / UMC Common Options
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [select] **Pstate5 VID** — Combo CBS / UMC Common Options★
    - _Specifies the core voltage._
- [select] **Controls whether or not the private memory regions (PSP, SMU and CC6) are at the top of DRAM or distributed. Note that distributed requires memory on all dies. Note that it will always be at the top of DRAM if some dies don't have memory regardless of this option's setting.** — Combo CBS★ / UMC Common Options
    - _Distributed_
- [number] **Consolidated**
    - _System probe filter_
- [number] **Controls whether or not the probe filter is enabled. Has no effect on parts where the probe filter is fuse disabled.**
    - _Memory interleaving_
- [select] **Controls fabric level memory interleaving (AUTO, none, channel, die, socket). Note that channel, die, and socket has requirements on memory populations and it will be ignored if the memory doesn't support the selected option.** — Channel★ / Die
    - _None_
- [select] **Socket** — Controls the memory interleaving size. The valid values are AUTO, 256 bytes, 512 bytes, 1 Kbytes or 2Kbytes. This determines the starting address of the interleave (bit 8, 9, 10 or 11).★ / 256 Bytes / 512 Bytes / 1 KB / 2 KB / Channel interleaving hash / Controls whether or not the address bits are hashed during channel interleave mode. This field should not be used unless the interleaving is set to channel and the interleaving size is 256 or 512 bytes. / DF C-state control / Enable / disable DF C-states (DF::CstateControl[DfCstateDisable]) / xGMI DLWM control / Controls xGMI dynamic link width management feature. / Freeze DF module queues on error / DDR4 Common Options / DRAM Memory Mapping / NVDIMM / Memory MBIST / DRAM Timing Configuration / DRAM Controller Configuration / CAD Bus Configuration / Data Bus Configuration
    - _Memory interleaving size_
- [select] **Common RAS** — WARNING - DAMAGE CAUSED BY USE OF YOUR AMD PROCESSOR OUTSIDE OF SPECIFICATION OR IN EXCESS OF FACTORY SETTINGS ARE NOT COVERED UNDER YOUR AMD PRODUCT WARRANTY AND MAY NOT BE COVERED BY YOUR SYSTEM MANUFACTURER'S WARRANTY.★ / No help string / Operating your AMD processor outside of specification or in excess of factory settings, including but not limited to overclocking, may damage or shorten the life of your processor or other system components, create system instabilities (e.g., data loss and corrupted images) and in extreme cases may result in total system failure. AMD does not provide support or service for issues or damages related to use of an AMD processor outside of processor specifications or in excess of factory settings. / I Decline / I Accept / Overclock / Memory Overclock Settings / Memory Clock Speed / Set the memory clock frequency. / 667MHz / 800MHz / 933MHz / 1067MHz / 1200MHz / 1333MHz / 1367MHz / 1400MHz / 1433MHz / 1467MHz / 1500MHz
    - _Security_
- [select] **1533MHz** — 1600MHz★ / 1633MHz / 1667MHz
    - _1567MHz_
- [select] **1700MHz** — 1767MHz / 1800MHz / No help string★
    - _1733MHz_
- [select] **1833MHz** — Combo CBS★ / UMC Common Options
    - _1867MHz_
- [select] **533MHz** — Combo CBS / UMC Common Options★ / 1066MHz / 2033MHz
    - _1050MHz_
- [select] **Trp** — Combo CBS★ / UMC Common Options
    - _Specify the row precharge time._
- [select] **34h Clk** — Combo CBS★ / UMC Common Options
    - _35h Clk_
- [toggle] **DF Common Options**
    - _UMC Common Options_
- [toggle] **NBIO Common Options**
- [number] **Disable CPB**
    - _Disabled_
- [select] **Global C-state Control** — Enabled★ / OC Mode
    - _Controls IO based C-state generation and DF C-states._

## Pstate0 FID  (2 settings)

- [select] **Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah).** — Auto★ / From a workaround for GCC/C000005 issue for XV Core on CZ A0, setting MSRC001_1029 Decode Configuration (DE_CFG) bit 14 [DecfgNoRdrctForReturns] to 1
    - _Pstate1 VID_
- [select] **Specifies the core voltage.** — Auto★ / From a workaround for GCC/C000005 issue for XV Core on CZ A0, setting MSRC001_1029 Decode Configuration (DE_CFG) bit 14 [DecfgNoRdrctForReturns] to 1
    - _Custom Pstate3_

## Pstate6 FID  (6 settings)

- [select] **Pstate6 DID** — Auto★ / From a workaround for GCC/C000005 issue for XV Core on CZ A0, setting MSRC001_1029 Decode Configuration (DE_CFG) bit 14 [DecfgNoRdrctForReturns] to 1
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [select] **Custom Pstate7** — Auto★ / From a workaround for GCC/C000005 issue for XV Core on CZ A0, setting MSRC001_1029 Decode Configuration (DE_CFG) bit 14 [DecfgNoRdrctForReturns] to 1
- [select] **Pstate7 DID** — Auto★ / From a workaround for GCC/C000005 issue for XV Core on CZ A0, setting MSRC001_1029 Decode Configuration (DE_CFG) bit 14 [DecfgNoRdrctForReturns] to 1
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [select] **Relaxed EDC throttling** — Auto★ / From a workaround for GCC/C000005 issue for XV Core on CZ A0, setting MSRC001_1029 Decode Configuration (DE_CFG) bit 14 [DecfgNoRdrctForReturns] to 1
- [select] **Disagree** — Auto★ / From a workaround for GCC/C000005 issue for XV Core on CZ A0, setting MSRC001_1029 Decode Configuration (DE_CFG) bit 14 [DecfgNoRdrctForReturns] to 1
    - _Agree_
- [select] **ONE** — Auto★ / From a workaround for GCC/C000005 issue for XV Core on CZ A0, setting MSRC001_1029 Decode Configuration (DE_CFG) bit 14 [DecfgNoRdrctForReturns] to 1
    - _TWO_

## Disabled  (10 settings)

- [toggle] **Add this hash image to allowed database (db)**
    - _Exit Discarding Change_
- [select] **I Decline** — DF Common Options / UMC Common Options★
    - _I Accept_
- [select] **WARNING - S3 is NOT SUPPORTED on systems where cores/threads have been removed/disabled.** — UMC Common Options / Control xGMI link encryption★
    - _Legal Disclaimer_
- [select] **Disagree** — DF Common Options / UMC Common Options★
    - _Agree_
- [select] **Relaxed EDC throttling** — DF Common Options / UMC Common Options★
- [select] **Data Bus Configuration** — DF Common Options / UMC Common Options★
    - _Common RAS_
- [select] **Security** — DF Common Options / UMC Common Options★
- [select] **WARNING - DAMAGE CAUSED BY USE OF YOUR AMD PROCESSOR OUTSIDE OF SPECIFICATION OR IN EXCESS OF FACTORY SETTINGS ARE NOT COVERED UNDER YOUR AMD PRODUCT WARRANTY AND MAY NOT BE COVERED BY YOUR SYSTEM MANUFACTURER'S WARRANTY.** — DF Common Options / UMC Common Options★
- [select] **No help string** — DF Common Options / UMC Common Options★
- [select] **Operating your AMD processor outside of specification or in excess of factory settings, including but not limited to overclocking, may damage or shorten the life of your processor or other system components, create system instabilities (e.g., data loss and corrupted images) and in extreme cases may result in total system failure. AMD does not provide support or service for issues or damages related to use of an AMD processor outside of processor specifications or in excess of factory settings.** — DF Common Options / UMC Common Options★

## Exit RealManage Setup  (3 settings)

- [select] **%s** — 100 Mpbs Half Duplex★ / 100 Mpbs Full Duplex
    - _RealManage Setup_
- [select] **Host Configuration** — Link Speed & Duplex★ / Change link speed and duplex for current adapter.
    - _Configure DASH host settings_
- [select] **Configure DASH(Desktop and Mobile Architecture for System Hardware) setting. DASH is a web services-based standard that can support both in-band and out-of-band management.** — Link Speed & Duplex★ / Change link speed and duplex for current adapter.
    - _Realtek RealManage Setup_

## Configuration Menu  (1 settings)

- [select] **Provisioning Model** — Link Speed & Duplex / Auto Negotiation★
    - _Configure DASH provision settings_

## Configure Realtek ethernet controller parameter  (5 settings)

- [select] **DHCPv4** — Enable or Disble DASH DHCP service / Set or change DASH IP★
    - _DNS_
- [select] **Host Name** — Domain Name★ / Set or change DASH domain name
    - _Set or change DASH host name_
- [select] **Set or change DASH DNS** — Link Speed & Duplex★ / Change link speed and duplex for current adapter.
    - _Echoservice_
- [select] **Enable or Disble DASH Echoservice** — Link Speed & Duplex / Change link speed and duplex for current adapter.★
    - _Provision Mode_
- [select] **Change DASH provision mode. Provision mode support Enterprise/Small business** — Link Speed & Duplex / Change link speed and duplex for current adapter.★
    - _Provision State_

## Driver Name:  (3 settings)

- [select] **Hash4 Value** — Change link speed and duplex for current adapter.
    - _Set or change DASH forth PKI hash value_
- [select] **Certificate Hash5 for PKI** — Link Speed & Duplex / Change link speed and duplex for current adapter.★ / Set or change DASH fifth PKI hash value
    - _Affirmative or negative DASH fifth PKI hash value_
- [select] **Certificate Hash4 for PKI** — Link Speed & Duplex / Change link speed and duplex for current adapter.★
    - _Affirmative or negative DASH forth PKI hash value_

## Driver Version:  (2 settings)

- [select] **Certificate Hash6 for PKI** — Hash6 Value / Set or change DASH sixth PKI hash value★ / FQDN / Set or change DASH PKI FQDN / PKI DNS Suffix / Set or change DASH PKI DNS suffix / Please Enter Username & Password / Please Input Password
    - _Affirmative or negative DASH sixth PKI hash value_
- [toggle] **Device Information**
    - _Device Name:_

## Secure Boot Database  (8 settings)

- [select] **Secure Boot Status** — YES★ / NO / Options:
    - _User Customized Security_
- [select] **Select a UEFI file as trusted for execution** — Options: / NO / YES★
    - _Add sepecific EFI image hash to allowed database._
- [select] **Enforce Secure Boot** — Erase all Secure Boot Settings / Enable this option will erase all Secure Boot Settings. This action will clear four variables PK, KEK, db, and dbx. / YES★
    - _Select Disable to Suspend enforcement of Secure Boot Checks._
- [select] **Restore Secure Boot to Factory Settings** — Restore Secure Boot to Backup Settings / YES★
    - _Restore all of the Secure Boot Settings to default factory settings and enable Secure Boot._
- [select] **Restore all of the secure boot Settings to backup factory settings and enable Secure Boot.** — Restore Secure Boot to Backup Settings / Enabled / YES★ / Activer
    - _Disabled_
- [select] **Operation is completed. System will reset!!** — Add this hash image to allowed database (db)★ / Exit Discarding Change / Exit saving changes
    - _This isn't a vaild EFI image. Please select another file!!_
- [select] **File format is incorrect!!** — Restore Secure Boot to Backup Settings / Enabled / YES★ / Activer
    - _Select Secure Mode_
- [select] **Select different secure boot mode. User can select one of 4 different modes (Setup Mode, User Mode, Audit mode and Deployed mode).** — Restore Secure Boot to Backup Settings / Enabled / YES★ / Activer
    - _PK Options_

## Restore all of the Secure Boot Settings to default factory settings and enable Secure Boot.  (12 settings)

- [select] **Exit saving changes**
    - _Cannot find file!!_
- [select] **File size is too large!!**
    - _File format is incorrect!!_
- [select] **X509_SHA384_GUID** — Select Signature Format★
    - _X509_SHA512_GUID_
- [select] **KEK Options** — KEK Signature List:★ / Enroll KEK
    - _Enroll/Delete KEK_
- [select] **DBX Signature List:**
    - _Enroll Signature_
- [select] **Delete Signature**
    - _Unknown_
- [select] **RSA2048_SHA256**
    - _PKCS7_
- [select] **SHA1**
    - _SHA256_
- [select] **Enroll KEK Using File** — Enter into Delete KEK Form★ / DB Options
    - _Delete KEK_
- [select] **Enroll/Delete Signature**
    - _DB Signature List:_
- [select] **DBX Options**
    - _Enroll/Delete DBX_
- [select] **Select Secure Mode**
    - _Select different secure boot mode. User can select one of 4 different modes (Setup Mode, User Mode, Audit mode and Deployed mode)._

## Désactiver  (1 settings)

- [toggle] **Add this hash image to allowed database (db)**
    - _Exit Discarding Change_

## IPv6 Network Configuration  (3 settings)

- [select] **Current gateway IPv6 addresses.** — automatic or manual★ / automatic
    - _DNS addresses     :_
- [select] **Current DNS server list.** — automatic or manual★ / automatic
    - _Interface ID_
- [select] **The 64 bit alternative interface ID for the device. The string is colon separated. e.g. ff:dd:88:66:cc:1:2:3** — automatic or manual★ / automatic
    - _DAD Transmit Count_

## Espace insuffisant pour stocker l'image.  (18 settings)

- [select] **Menu de configuration MBA** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
- [select] **Micrologiciel de gestion** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Page de configuration principale** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Paramètres généraux iSCSI_
- [select] **Paramètres généraux iSCSI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurer les paramètres généraux iSCSI de démarrage.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Paramètres de l'initiateur iSCSI_
- [select] **Paramètres de l'initiateur iSCSI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurer les paramètres de l'initiateur iSCSI.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Paramètres de la première cible iSCSI_
- [select] **Périphérique secondaire** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configurer les paramètres du périphérique secondaire._
- [select] **Paramètres iSCSI du périphérique secondaire** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurer les paramètres du périphérique secondaire.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **ROM en option** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Activer/Désactiver la ROM en option d'initialisation** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Détecter automatiquement_
- [select] **BBS** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Int 18h_
- [select] **Int 19h** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Masquer l'invite de configuration_
- [select] **Masquer l'invite de configuration** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configurer l'affichage de l'invite de configuration pendant l'initialisation de la ROM._
- [select] **Configurer la séquence de touches** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurer la séquence de touches permettant d'appeler le menu de configuration.** — Ctrl-B / Délai d'inactivité du message de bannière★
    - _Ctrl-S_
- [select] **Menu de configuration du démarrage iSCSI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configurer les paramètres de démarrage iSCSI._

## Enter into Delete PK Form  (19 settings)

- [select] **Select Signature Format** — [Error] PK already exists.★ / [Error] Invalid GUID string. GUID string should be in 12345678-1234-1234-1234-1234567890ab format. / [Error] There is already an identical signature in signature list.
    - _Delete this signature_
- [toggle] **Input Owner_GUID in 12345678-1234-1234-1234-1234567890ab format.** — Restore Secure Boot to Backup Settings / KEK Signature List: / YES★
    - _The operation is only allowed before booting any boot device!!! Please reset system and enter this menu directly if need use this operation._
- [toggle] **Secure Boot Mode** — Secure Boot Mode★
- [select] **Enroll/Delete Signature** — Add this hash image to allowed database (db) / This isn't a vaild EFI image. Please select another file!!★
    - _DB Signature List:_
- [select] **Enroll KEK** — Delete KEK / Enter into Delete KEK Form / DB Options★
    - _Enroll KEK Using File_
- [select] **KEK Options** — KEK Signature List: / YES★
    - _Enroll/Delete KEK_
- [number] **Delete KEK**
    - _Enter into Delete KEK Form_
- [number] **DB Options**
    - _Enroll/Delete Signature_
- [number] **DB Signature List:**
    - _DBX Options_
- [number] **Enroll/Delete DBX**
    - _DBX Signature List:_
- [select] **Enroll Signature** — Restore Secure Boot to Backup Settings / KEK Signature List: / YES★
    - _Delete Signature_
- [number] **Unknown**
    - _RSA2048_SHA256_
- [number] **PKCS7**
    - _SHA1_
- [number] **SHA256**
    - _SHA512_
- [select] **X509_SHA256** — Restore Secure Boot to Backup Settings / KEK Signature List: / YES★
    - _X509_SHA384_GUID_
- [number] **X509_SHA512_GUID**
    - _Select Signature Format_
- [number] **Delete this signature**
    - _[Error] PK already exists._
- [number] **[Error] There is already an identical signature in signature list.**
    - _[Error] Invalid GUID string. GUID string should be in 12345678-1234-1234-1234-1234567890ab format._
- [number] **Press Esc for boot options**
    - _Esc is pressed. Go to boot options._

## 容量が不足しているために画像を保存できません。  (18 settings)

- [select] **MBA コンフィギュレーション メニュー** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
- [select] **管理ファームウェア** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **メイン コンフィギュレーション ページ** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _iSCSI 全般パラメタ_
- [select] **iSCSI 全般パラメタ** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **iSCSI の全般的なブート パラメタを設定する。** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _iSCSI イニシエータ パラメタ_
- [select] **iSCSI イニシエータ パラメタ** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **iSCSI イニシエータ パラメタを設定する。** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _iSCSI ファースト ターゲット パラメタ_
- [select] **セカンダリ デバイス** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _セカンダリ デバイスのパラメタを設定する。_
- [select] **iSCSI セカンダリ デバイス パラメタ** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **セカンダリ デバイスのパラメタを設定する。** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **オプション ROM** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **ブート オプション ROM をイネーブル/ディスネーブルする** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _自動検出_
- [select] **BBS** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Int 18h_
- [select] **Int 19h** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _セットアップ プロンプトを隠す_
- [select] **セットアップ プロンプトを隠す** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _ROM の初期化中にセットアップ プロンプトを表示するかどうかを設定する。_
- [select] **キー操作のセットアップ** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **コンフィギュレーション メニューを呼び出すキー操作を設定する。** — Ctrl-B / バナー メッセージのタイムアウト★
    - _Ctrl-S_
- [select] **iSCSI ブート コンフィギュレーション メニュー** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _iSCSI ブート パラメタを設定する。_

## HDD2            (1 settings)

- [toggle] **HDD0(OPAL)    **
    - _HDD1(OPAL)    _

## VDD18 voltage (ANPEC:+80mv/TI:+75mv)  (7 settings)

- [select] **VDD18 voltage (ANPEC:+90mv/TI:+87.5mv)** — HybridGraphics★ / Disable Discrete GPU's Audio or keep its ROM strap setting
    - _VDD18 voltage (ANPEC:+100mv/TI:+100mv)_
- [select] **VDD18 voltage (ANPEC:+110mv/TI:+112.5mv)** — HybridGraphics★ / VDD18 voltage (ANPEC:+130mv/TI:+137.5mv) / VDD18 voltage (ANPEC:-40mv/TI:-25mv) / VDD18 voltage (ANPEC:-50mv/TI:-37.5mv) / VDD18 voltage (ANPEC:-60mv/TI:-50mv) / VDD18 voltage (ANPEC:-70mv/TI:-62.5mv) / VDD18 voltage (ANPEC:-80mv/TI:-75mv) / VDD18 voltage (ANPEC:-90mv/TI:-87.5mv) / VDD18 voltage (ANPEC:-100mv/TI:-100mv) / VDD18 voltage (ANPEC:-110mv/TI:-112.5mv) / VDD18 voltage (ANPEC:-120mv/TI:-125mv) / VDD18 voltage (ANPEC:-130mv/TI:-137.5mv) / 5V_S5 voltage. / 5V_S5 voltage setting for ANPEC PSA / 5v_ALW(default) / 5v_ALW +60mv / 5v_ALW +100mv / AMD KVM Mouse Protocol / Swtich KVM Mouse Protocol between Absolut/Simple / Absolute / Simple / AMD DPTC interface / Dynamic Power and Thermal Control Interface Enable/Disable / StallForUnlock / StallForUnlock Enable/Disable / HDT BreakPoint for Boot / HDT BreakPoint for Boot Enable/Disable / SW BreakPoint for S3 / SW BreakPoint for S3 Enable/Disable / BLINK LED / Enable/Disable BLINK LED to identify S3/S4 state / GPIO 11 Output Low / GPIO 11 Output High / Serial Debug Message Under OS / Enable Serial Debug Message Under OS
    - _VDD18 voltage (ANPEC:+120mv/TI:+125mv)_
- [select] **AMD Firmware Version** — AGESA Version / 0 / PSP BootLoader Version / PSP SecureOS Version / ABL Version / APCB Version / APOB Version / HybridGraphics★ / Ucode Patch Version / SMU FW Version / SMU RV2 FW Version / DXIO FW Version / MP2 FW Version / MP2 RV2 FW Version / XHCI FW Version
    - _Show all of AMD Firmware Version_
- [select] **VBIOS FW Version** — AGESA Version / 0 / PSP BootLoader Version / PSP SecureOS Version / ABL Version / APCB Version / Ucode Patch Version / SMU FW Version / SMU RV2 FW Version / DXIO FW Version / APOB Version / HybridGraphics★
    - _0_
- [select] **GOP Driver Version** — HybridGraphics★ / AGESA Version / 0 / EC FW Version / USB PD Section 1 FW Version / USB PD Section 2 FW Version / APCB Version / APOB Version / Ucode Patch Version / SMU FW Version / SMU RV2 FW Version / DXIO FW Version
    - _0_
- [select] **iLA TraceMemoryEn** — AGESA Version / 0 / PSP BootLoader Version / PSP SecureOS Version / ABL Version / APCB Version / APOB Version / HybridGraphics★ / Ucode Patch Version / SMU FW Version / SMU RV2 FW Version / DXIO FW Version
    - _Reserved 1M bytes MMIO space on 1M boundary when iLA TraceMemoryEn enabled_
- [select] **iLA TraceMemoryEn reserved MMIO** — 0 / SMU FW Version / SMU RV2 FW Version / DXIO FW Version / MP2 FW Version / MP2 RV2 FW Version / XHCI FW Version / Above 4GB MMIO Limit / Select Above 4GB MMIO Limit to 35~48bits limit. / 35bit (32GB) / 36bit (64GB) / 37bit (128GB) / 38bit (256GB) / 39bit (512GB) / 40bit (1TB) / 41bit (2TB) / HybridGraphics★ / 42bit (4TB) / 43bit (8TB) / 44bit (16TB) / 45bit (32TB) / 46bit (64TB) / 47bit (128TB) / 48bit (256TB) / NVIDIA DGPU Power Enable / For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround / For NRT3663 VRM only. Enable PSI0 Workaround To Save Power. / Press Esc for boot options / Esc is pressed. Go to boot options.
    - _0_

## Réf. fournisseur DHCP  (2 settings)

- [select] **Adresse IP** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Configurer l'adresse IP de l'initiateur._
- [select] **Configurer le nom iSCSI.** — Nom iSCSI★ / Configurer le nom iSCSI. / Réf. CHAP
    - _Réf. CHAP_

## AMD PBS Setup Page  (4 settings)

- [number] **Disabled**
    - _Auto_
- [select] **0** — 0★ / USB PD Section 2 FW Version / For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround
    - _USB PD Section 1 FW Version_
- [number] **Reserved 1M bytes MMIO space on 1M boundary when iLA TraceMemoryEn enabled**
    - _iLA TraceMemoryEn reserved MMIO_
- [number] **Select Above 4GB MMIO Limit to 35~48bits limit.**
    - _35bit (32GB)_

## Enable/Disable PCIe x8 Slot D3Cold  (41 settings)

- [select] **UCSI Support** — UCSI tunnel location / HybridGraphics★
    - _Enable/Disable UCSI (USB Type-C Connector System Software Interface)_
- [number] **UCSI tunnel can be put on ECRAM or MMIO space, this option specify which one is selected.** — UCSI tunnel at MMIO 0xFEEC2000 / S3/Modern Standby Support / Switch S3/Modern Standby★
    - _UCSI tunnel at EC RAM_
- [number] **UCSI tunnel at MMIO 0xFEEC2000**
    - _S3/Modern Standby Support_
- [number] **Switch S3/Modern Standby**
    - _S3 Enable_
- [number] **Modern Standby Enable**
    - _Modern Standby Type_
- [number] **Select S0I2 or S0I3 type for Modern Standby.**
    - _Modern Standby + S0i2_
- [select] **Modern Standby + S0i3** — OR Circuitry / UCSI tunnel location / HybridGraphics★
    - _Modern Standby + S0i2 + S0i3_
- [number] **SATA D3cold Enable**
    - _Enable/Disable SATA devies D3-COLD support._
- [number] **MS Resource**
    - _Auto: USB interrupt resource is controlled automatically; Enable: Enable USB current resource for MS; Disable: Disable USB current resource for MS._
- [number] **Reduce Hardware Support**
    - _Enable/Disable Reduce Hardware Support. Please disable PME wakeup, when Reduce Hardware enabled._
- [select] **Wake on PME** — OR Circuitry / UCSI tunnel location / HybridGraphics★
    - _Determines the action taken when the system power is off and a PCI Power Management Enable wake up event occurs._
- [number] **Sensor Fusion User Mode Driver**
    - _Enable/Disable Sensor Fusion User Mode Driver_
- [number] **Unused GPP Clocks Off**
    - _Turn Unused GPP Clocks Off_
- [number] **Clock PM: CLK_REQ0**
    - _Enable or disable CLK_REQ0# for M.2 WLAN Slot J3711_
- [select] **Clock PM: CLK_REQ1** — OR Circuitry / UCSI tunnel location / HybridGraphics★
    - _Enable or disable CLK_REQ1# for Onboard LAN U1301_
- [number] **Clock PM: CLK_REQ2**
    - _Enable or disable CLK_REQ2# for M.2 WWAN Slot J3712_
- [number] **Clock PM: CLK_REQ3**
    - _Enable or disable CLK_REQ3# for M.2 WIFI Slot J3709_
- [number] **Clock PM: CLK_REQ4**
    - _Enable or disable CLK_REQ4# for DT x4 Slot J3606_
- [select] **Clock PM: CLK_REQ5** — OR Circuitry / UCSI tunnel location / HybridGraphics★
    - _Enable or disable CLK_REQ5# for M.2 SSD Slot J3704_
- [number] **Clock PM: CLK_REQ6**
    - _Enable or disable CLK_REQ6# for MXM x8 Slot J3604_
- [number] **Wireless LAN Recovery**
    - _Wireless LAN Recovery suppport Enable/Disable_
- [number] **MITT/WITT Selection**
    - _MITT Only_
- [select] **WITT Only** — OR Circuitry / UCSI tunnel location / HybridGraphics★
    - _Both disable_
- [number] **LAN Power Enable**
    - _Enable or disable LAN Power_
- [number] **LAN Low Power Mode**
    - _Enable or disable LAN Low Power Mode_
- [number] **KBC Support**
    - _Enable/Disable KBC Support under OS_
- [select] **HDD Power Enable** — OR Circuitry / UCSI tunnel location / HybridGraphics★
    - _Enable or disable the power of HDD_
- [number] **ODD Power Enable**
    - _Enable or disable the power of ODD_
- [number] **Zero-Power ODD**
    - _Enable/Disable Zero-Power ODD Feature_
- [number] **SSD Power Enable**
    - _Enable or disable the power of SSD_
- [select] **SSD x2** — OR Circuitry / UCSI tunnel location / HybridGraphics★
    - _SSD x4_
- [number] **Camera 0 Enable**
    - _Enable or disable the power of REAR CAMERA_
- [number] **Camera 1 Enable**
    - _Enable or disable the power of FRONT CAMERA_
- [number] **WLAN/WIFI Power Enable**
    - _Enable or disable the power of WLAN/WIFI_
- [select] **WWAN Power Enable** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _Enable or disable the power of WWAN_
- [select] **VDDP voltage (+80mv)** — Select Internal/External Graphics / VDDP voltage (+70mv) / VDDP voltage (+40mv)★
    - _VDDP voltage (+90mv)_
- [select] **VDD18 voltage  Setting.** — VDD18 voltage (ANPEC:+40mv/TI:+25mv)★ / VDD18 voltage (ANPEC:+50mv/TI:+37.5mv)
    - _VDD18 voltage (1.8V)_
- [select] **Enable/Disable Sensor Fusion User Mode Driver** — Turn Unused GPP Clocks Off★ / Enable or disable CLK_REQ0# for M.2 WLAN Slot J3711 / Clock PM: CLK_REQ0
    - _Unused GPP Clocks Off_
- [select] **0** — 0 / XHCI FW Version★
    - _MP2 RV2 FW Version_
- [toggle] **Manual** — Manual★
- [select] **S3 Enable** — Enable/Disable Discrete GPU BOMACO Support / Discrete GPU BOMACO Support★
    - _Modern Standby Enable_

## Select DT Hotplug Mode - DxioHotplugEnhanced or DxioHotplugBasic  (2 settings)

- [select] **Basic Mode** — DT Slot Power Enable / Enable or disable the power of DT SLOT / Eval Auto Detection / HybridGraphics★
    - _Enhanced Mode_
- [select] **Disable or enable EVAL card auto detection** — Enable to support sending PME_Turn_Off message to Discrete GPU when going to D3Cold / HybridGraphics★
    - _Touch Panel Support_

## Manual  (14 settings)

- [select] **Enable/Disable exposing of _HID(PNP0C50) in ACPI ASL code to OS** — OR Circuitry / Enable/Disable exposing of _HID(PNP0C50) in ACPI ASL code to OS / Nfc Support / Enable/Disable exposing of _HID(BCM2F25) in ACPI ASL code to OS / ALS Support / Enable/Disable exposing of _HID(CPLM3218) in ACPI ASL code to OS / Under I2C 0 Bus / HybridGraphics★
    - _Touch Pad Support_
- [select] **Under I2C 1 Bus** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _Under I2C 2 Bus_
- [select] **Under I2C 3 Bus** — ELAN TSP Under I2C 1 Bus / ELAN TSP Under I2C 2 Bus / HybridGraphics★
    - _ELAN TSP Under I2C 0 Bus_
- [select] **ELAN TSP Under I2C 3 Bus** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _Manual by jumper_
- [select] **HDMI over USB-C0** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _HDMI over USB-C1_
- [select] **Force HDMI signals route over USB Type C port** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _Native USB Type-C_
- [select] **HDMI over USB Type-C** — Enable/disable AcDcSwitch. / AmdDcTimer / HybridGraphics★
    - _AcDcSwitch_
- [select] **AmdDcTimer Setting.** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _AmdAcTimer_
- [select] **AmdAcTimer Setting.** — SATA/ SATA express selection  Setting. / SATA / SATA express / VDDP voltage / HybridGraphics★
    - _SATA/ SATA express selection_
- [select] **VDDP voltage  Setting.** — VDDP voltage (+10mv) / VDDP voltage (+20mv) / VDDP voltage (+30mv) / VDDP voltage (+40mv) / HybridGraphics★
    - _VDDP voltage (0.9V)_
- [select] **VDDP voltage (+50mv)** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _VDDP voltage (+60mv)_
- [select] **VDDP voltage (+70mv)** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _VDDP voltage (+80mv)_
- [select] **VDDP voltage (+90mv)** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _VDDP voltage (+100mv)_
- [select] **VDDP voltage (-10mv)** — OR Circuitry / Disable Discrete GPU's Audio or keep its ROM strap setting / HybridGraphics★
    - _VDDP voltage (-20mv)_

## Set COM Terminal Type  (2 settings)

- [select] **7200** — Add .EFI Driver as Driver Option★ / Add Driver Option
    - _4800_
- [select] **134** — Add .EFI Driver as Driver Option★ / Add Driver Option
    - _110_

## File Explorer  (1 settings)

- [select] **None** — Add .EFI Driver as Driver Option★ / Add Driver Option

## VDDP voltage (+10mv)  (2 settings)

- [select] **VDDP voltage (+20mv)** — VDDP voltage (+40mv)★ / VDDP voltage (+50mv)
    - _VDDP voltage (+30mv)_
- [select] **Under I2C 2 Bus** — RT3663 VRM PSI0 Workaround★ / For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state.
    - _Under I2C 3 Bus_

## 10Mbps Full  (2 settings)

- [select] **IPv4** — Bus:Device:Function★ / Chip Type/Revision.
    - _IPv6_
- [select] **iSCSI Configuration** — Bus:Device:Function★ / Chip Type/Revision.

## TCP Timestamp  (6 settings)

- [select] **Target as First HDD** — Bus:Device:Function★ / Chip Type/Revision.
    - _Enable/Disable target appears as first hard disk drive (HDD) in the system._
- [select] **IP Version** — Bus:Device:Function★ / Chip Type/Revision.
    - _IP version support.  Modifying this parameter will reset all IP-related fields._
- [select] **IP Address** — Bus:Device:Function★ / Chip Type/Revision.
    - _Configure target IP address._
- [select] **Subnet Mask** — Bus:Device:Function★ / Chip Type/Revision.
    - _Configure IP subnet mask._
- [select] **Default Gateway** — Bus:Device:Function★ / Chip Type/Revision.
    - _Configure default gateway IP address._
- [select] **Secondary DNS** — Bus:Device:Function★ / Chip Type/Revision.
    - _Configure secondary DNS IP address._

## Permanent MAC Address  (7 settings)

- [select] **PCI Bus:Device:Function number of this device.** — PCI Address / Bus:Device:Function★
    - _Link Status_
- [select] **Link Status** — Disconnected / Blink LEDs / Bus:Device:Function★
    - _Connected_
- [select] **Blink LEDs for a duration up to 15 seconds.** — Legacy Boot Protocol / Bus:Device:Function★
    - _Legacy Boot Protocol_
- [select] **Select non-UEFI Boot Protocol: Preboot Execution Environment (PXE)/iSCSI.** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★
    - _PXE_
- [select] **NONE** — Boot Strap Type★ / Select boot strap type.
    - _None_
- [select] **Configure link speed.** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★
    - _Pre-boot Wake On LAN_
- [select] **Configure Pre-boot Wake on LAN (WOL).** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★
    - _Wake On LAN_

## Link Status  (4 settings)

- [select] **Int 18h** — MAC Address / Banner Message Timeout / iqn.1995-05.com.broadcom.iscsiboot★
    - _Int 19h_
- [select] **Select timeout value. (0 defaults to 4 seconds, 15 is no delay, 1-14 is timeout value in seconds)** — BRCM ISAN / 0.0.0.0★
- [select] **Hide Setup Prompt** — MAC Address / Permanent MAC Address★
- [select] **100Mbps Half** — MAC Address
    - _100Mbps Full_

## Configure Energy Efficient Ethernet operation.  (1 settings)

- [toggle] **VLAN ID (1..4094)**

## バス：デバイス：機能  (1 settings)

- [select] **iSCSI オフロード サポート** — MAC アドレス / 固定 MAC アドレス★
    - _iSCSI ブート サポート_

## 管理ファームウェア  (1 settings)

- [select] **iSCSI ファースト ターゲット パラメタ** — MAC アドレス / 固定 MAC アドレス★

## メイン コンフィギュレーション ページ  (5 settings)

- [select] **iSCSI ファースト ターゲット パラメタ** — MAC アドレス / 固定 MAC アドレス★
- [select] **HP共有メモリ機能を無効にします** — 無効 / 有効★
    - _予約されたメモリ領域の使用状況のデバイス割り当てを直接ゲスト仮想マシンに許可をディセーブルにします。_
- [number] **LED を点滅させる**
    - _LED を最大 15 秒点滅させる。_
- [select] **プリブート Wake On LAN** — 無効 / 有効
    - _プリブート Wake on LAN (WOL) を設定する。_
- [select] **リンク ステータス** — 切断完了 / 接続完了

## iSCSI 全般パラメタ  (13 settings)

- [select] **iSCSI ファースト ターゲット パラメタ** — MAC アドレス / 固定 MAC アドレス★
- [select] **DHCP 経由の TCP/IP パラメタ** — 無効 / 有効★
    - _DHCP 経由で TCP/IP コンフィギュレーションを取得する。_
- [select] **IP 自動コンフィギュレーション** — 無効 / 有効★
    - _ステートフルまたはステートレスな自動コンフィギュレーションで TCP/IP コンフィギュレーションを取得する。_
- [select] **DHCP 経由の iSCSI パラメタ** — 無効 / 有効★
    - _DHCP 経由で iSCSI パラメタを取得する。_
- [select] **CHAP 認証** — 無効★ / 有効
    - _CHAP 認証をイネーブル/ディスエーブルする。_
- [select] **iSCSI ターゲットでのブート** — 無効 / 有効★ / 一時的に無効
    - _ログオン後の iSCSI ターゲットでのブートをイネーブル/ディスエーブルする。_
- [select] **ターゲットでのブート** — 無効 / 有効★ / 一時的に無効
    - _ログオン後の iSCSI ターゲットでのブートをイネーブル/ディスエーブルする。_
- [number] **リンク アップ遅延時間**
    - _リンク アップの遅延時間を秒単位で設定する (0 ～ 255 秒)。_
- [select] **TCP タイムスタンプを使用** — 無効★ / 有効
    - _TCP タイムスタンプをイネーブル/ディスエーブルする。_
- [select] **TCP タイムスタンプ** — 無効★ / 有効
    - _TCP タイムスタンプをイネーブル/ディスエーブルする。_
- [select] **ターゲットをファースト HDD として表示** — 無効★ / 有効
    - _ターゲットをシステムのファースト ハード ディスク ドライブ (HDD) として表示することをイネーブル/ディスエーブルする。_
- [number] **LUN ビジー再試行カウント**
    - _LUN がビジーな場合に、2 秒置きに何回再試行するか設定する (0 ～ 60 回)。_
- [select] **IP バージョン** — IPv4★ / IPv6
    - _IP バージョンのサポート。このパラメタを変更するとすべての IP 関連のフィールドがリセットされます。_

## iSCSI の全般的なブート パラメタを設定する。  (1 settings)

- [select] **iSCSI ファースト ターゲット パラメタ** — MAC アドレス / 固定 MAC アドレス★

## iSCSI イニシエータ パラメタ  (1 settings)

- [select] **iSCSI ファースト ターゲット パラメタ** — MAC アドレス / 固定 MAC アドレス★

## iSCSI イニシエータ パラメタを設定する。  (1 settings)

- [select] **iSCSI ファースト ターゲット パラメタ** — MAC アドレス / 固定 MAC アドレス★

## PCIバス：デバイス：機能。  (2 settings)

- [select] **VLAN ID (1..4094)** — MAC アドレス★ / 固定 MAC アドレス
    - _バーチャル LAN ID_
- [select] **仮想 LAN** — MAC アドレス★ / 固定 MAC アドレス
    - _仮想 LAN モードを設定する。_

## リンク ステータス  (4 settings)

- [select] **Int 18h** — MAC アドレス / バナー メッセージのタイムアウト / iqn.1995-05.com.broadcom.iscsiboot★
    - _Int 19h_
- [select] **タイムアウト値を選択する。(0 はデフォルトの 4 秒、15 は遅延なし、1 ～ 14 は秒単位のタイムアウト値)** — BRCM ISAN / 0.0.0.0★
- [select] **セットアップ プロンプトを隠す** — MAC アドレス / 固定 MAC アドレス★
- [select] **100 Mbps 半二重** — MAC アドレス
    - _100 Mbps 全二重_

## 切断完了  (6 settings)

- [select] **SMASH** — MAC アドレス
    - _CCM_
- [select] **IPv4** — IPv6 / MBA コンフィギュレーション メニュー★
    - _iSCSI ブート コンフィギュレーション メニュー_
- [select] **100 Mbps 全二重** — 有効★ / 一時的に無効
    - _無効_
- [select] **iSCSI ブート パラメタを設定する。** — MAC アドレス★ / 固定 MAC アドレス
    - _iSCSI の設定_
- [select] **iSCSI の設定** — MAC アドレス / 固定 MAC アドレス★
    - _ファームウェア イメージ メニュー_
- [select] **ファームウェア イメージ メニュー** — MAC アドレス / 固定 MAC アドレス★
    - _ファームウェア イメージの情報。_

## LED を最大 15 秒点滅させる。  (2 settings)

- [select] **セカンダリ デバイスのパラメタを設定する。** — MAC アドレス / 固定 MAC アドレス★
    - _iSCSI セカンダリ デバイス パラメタ_
- [select] **iSCSI セカンダリ デバイス パラメタ** — オプション ROM★
    - _セカンダリ デバイスのパラメタを設定する。_

## 旧式ブート プロトコル  (28 settings)

- [select] **ASF** — MAC アドレス / 固定 MAC アドレス★
    - _NC-SI_
- [select] **サブネット マスク プリフィックス** — 固定 MAC アドレス / CHAP 秘密情報を設定する (12 ～ 16 文字)。★
    - _IP サブネット マスク プリフィックス長を設定する。_
- [select] **デフォルト ゲートウェイ** — MAC アドレス / 固定 MAC アドレス★
    - _デフォルト ゲートウェイの IP アドレスを設定する。_
- [select] **サブネット マスク** — MAC アドレス / 固定 MAC アドレス★
    - _IP サブネットマスクを設定する。_
- [select] **CCM** — MAC アドレス / 固定 MAC アドレス★
    - _UMP_
- [select] **EFI** — MAC アドレス / 固定 MAC アドレス★
- [select] **Fcode** — MAC アドレス / 固定 MAC アドレス★
- [select] **コントローラのBIOSバージョン** — MAC アドレス / 固定 MAC アドレス★
- [select] **MBA** — MAC アドレス / 固定 MAC アドレス★
- [select] **iSCSI ブート** — MAC アドレス / 固定 MAC アドレス★
- [select] **ブート ストラップのタイプを選択する。** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _リンク速度_
- [select] **リンク速度** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _リンク速度を設定する。_
- [select] **MBA (Multiple Boot Agent) パラメタを設定する。** — NICの設定★
    - _NICの設定_
- [select] **仮想 LAN** — VLAN ID (1..4094)★ / バーチャル LAN ID
    - _仮想 LAN モードを設定する。_
- [select] **10 Mbps 全二重** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _100 Mbps 半二重_
- [select] **100 Mbps 全二重** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _無効_
- [select] **有効** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _一時的に無効_
- [select] **IPv4** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _IPv6_
- [select] **バーチャル LAN ID (1..4094) を構成します。** — 10 Mbps 半二重★ / 10 Mbps 全二重
    - _自動ネゴシエーション_
- [select] **100 Mbps 半二重** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _100 Mbps 全二重_
- [select] **自動ネゴシエート済み** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _10 Mbps 半二重_
- [select] **プリブート Wake On LAN** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _プリブート Wake on LAN (WOL) を設定する。_
- [select] **iSCSI ファースト ターゲット パラメタ** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **iSCSI ファースト ターゲット パラメタを設定する。** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _iSCSI セカンド ターゲット パラメタ_
- [select] **PCI デバイス ID** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
- [select] **iSCSI セカンド ターゲット パラメタ** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **iSCSI セカンド ターゲット パラメタを設定する。** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _セカンダリ デバイス_
- [select] **ターゲットでのブート** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _ログオン後の iSCSI ターゲットでのブートをイネーブル/ディスエーブルする。_

## ナシ  (4 settings)

- [select] **CHAP ID** — MAC アドレス / 固定 MAC アドレス★
- [select] **CHAP ID を設定する (32 文字まで)。** — MAC アドレス / 固定 MAC アドレス★
    - _CHAP ID を設定する (128 文字まで)。_
- [select] **CHAP 秘密情報** — MAC アドレス / 固定 MAC アドレス★
- [select] **iSCSI セカンド ターゲット パラメタ** — MAC アドレス / 固定 MAC アドレス★
    - _iSCSI セカンド ターゲット パラメタを設定する。_

## Clé secrète CHAP  (6 settings)

- [select] **Clé secrète CHAP** — Adresse MAC★ / Adresse MAC permanente
    - _Configurer la clé secrète CHAP (12 à 16 caractères)._
- [select] **Périphérique secondaire** — Adresse MAC★
- [select] **Connecter** — Adresse MAC / Adresse MAC permanente★
    - _Activer/Désactiver l'établissement de la cible._
- [select] **Port TCP** — Adresse MAC★ / Configurer le numéro du port TCP de la cible (1 à 65 535). / Port TCP
    - _Configurer le numéro du port TCP de la cible (1 à 65 535)._
- [number] **Configurer le numéro d'unité logique de démarrage cible (0 à 255).**
    - _Type de puce/Révision._
- [select] **Unité logique de démarrage** — Adresse MAC / Adresse MAC permanente★
    - _Configurer le numéro d'unité logique de démarrage cible (0 à 255)._

## AMD PBS  (3 settings)

- [select] **Discrete GPU D3Cold HPD Support** — Discrete GPU's Audio★ / Disable Discrete GPU's Audio or keep its ROM strap setting
    - _Enable/Disable Discrete GPU D3Cold HPD function_
- [select] **PME Turn Off Support** — Discrete GPU's Audio★ / Disable Discrete GPU's Audio or keep its ROM strap setting
    - _Enable to support sending PME_Turn_Off message to Discrete GPU when going to D3Cold_
- [select] **Discrete GPU HPD Circuitry** — Discrete GPU's Audio★ / Disable Discrete GPU's Audio or keep its ROM strap setting
    - _Enable/Disable Discrete GPU Display HPD Circuitry_

## Int Graphics (IGD)  (1 settings)

- [toggle] **UCSI tunnel location**

## Switch S3/Modern Standby  (2 settings)

- [select] **Auto: USB interrupt resource is controlled automatically; Enable: Enable USB current resource for MS; Disable: Disable USB current resource for MS.** — HybridGraphics★ / Enable/Disable HybridGraphics
    - _Reduce Hardware Support_
- [select] **Enable or disable CLK_REQ0# for M.2 WLAN Slot J3711** — HybridGraphics★ / Enable/Disable HybridGraphics
    - _Clock PM: CLK_REQ1_

## System Status:  (1 settings)

- [number] **Unlocked**
    - _Installed and Locked_

## Secreto CHAP  (6 settings)

- [select] **Secreto CHAP** — Dirección MAC★ / Dirección MAC permanente
    - _Configurar secreto CHAP (entre 12 y 16 caracteres de longitud)._
- [select] **Dispositivo secundario** — Dirección MAC★
- [select] **Conectar** — Dirección MAC / Dirección MAC permanente★
    - _Habilitar/Deshabilitar establecimiento de destino._
- [select] **Puerto TCP** — Dirección MAC★ / Configurar número de puerto TCP de destino (1..65535). / Puerto TCP
    - _Configurar número de puerto TCP de destino (1..65535)._
- [number] **Configurar número LUN de arranque de destino (0..255).**
    - _Revisión/tipo de chip._
- [select] **LUN de arranque** — Dirección MAC / Dirección MAC permanente★
    - _Configurar número LUN de arranque de destino (0..255)._

## Boot-LUN  (2 settings)

- [select] **Ziel-Boot-LUN-Nummer (0..255) konfigurieren.** — Eingabe der MAC-Adresse des sekundären Geräts. XX:XX:XX:XX:XX:XX-Format verwenden.★ / MAC-Adresse des sekundären Geräts
    - _Sekundäres Gerät_
- [select] **CHAP-ID konfigurieren (bis zu 32 Zeichen lang)** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _CHAP-ID konfigurieren (bis zu 128 Zeichen lang)_

## L2 TLB Associativity  (3 settings)

- [select] **Decline** — Combo CBS★ / Promontory Common Options
    - _Accept_
- [select] **Custom** — DF Common Options★ / UMC Common Options
    - _Frequency (MHz)_
- [select] **Custom Pstate0** — DF Common Options★ / UMC Common Options

## Operating your AMD processor outside of specification or in excess of factory settings, including but not limited to overclocking, may damage or shorten the life of your processor or other system components, create system instabilities (e.g., data loss and corrupted images) and in extreme cases may result in total system failure. AMD does not provide support or service for issues or damages related to use of an AMD processor outside of processor specifications or in excess of factory settings.  (1 settings)

- [toggle] **Custom**

## Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah).  (2 settings)

- [select] **Pstate7 FID** — 34h Clk / 33h Clk★
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [select] **SMTEN** — DRAM scrub time / Provide a value that is the number of hours to scrub memory. / 48 hours★ / Redirect scrubber control
    - _8 hours_

## Administer Secure Boot  (3 settings)

- [select] **Enforce Secure Boot** — Disabled★ / Enabled / Désactiver / Activer
    - _Select Disable to Suspend enforcement of Secure Boot Checks._
- [select] **Erase all Secure Boot Settings** — Disabled★ / Enabled / Désactiver / Activer
    - _Enable this option will erase all Secure Boot Settings. This action will clear four variables PK, KEK, db, and dbx._
- [select] **Restore Secure Boot to Factory Settings** — Disabled★ / Enabled / Désactiver / Activer
    - _Restore all of the Secure Boot Settings to default factory settings and enable Secure Boot._

## The route table of the IPv6 network stack runs on this interface.  (1 settings)

- [select] **Press ENTER to enter configuration menu for IPv6 configuration.** — The interface type of the network interface, defined in RFC1700.

## automatic or manual  (1 settings)

- [toggle] **Configure the interface manually. IP address, gateway address, and DNS server address can be configured.**
    - _New IPv6 address_

## +/- =rejette des Changements  (11 settings)

- [select] **S'il vous plait tape votre nouveau mot de passe**
    - _S'il vous plait confirmer votre nouveau mot de passe_
- [select] **Les mots de passe ne sont pas pareils**
    - _Mauvais mot de passe_
- [select] **Appuyer sur Entrée/Echappe  - Quitter** — Appuyer sur Page Suivante   - la Page Suivante★
    - _Appuyer sur Page Précédente - Précédent_
- [select] **Setup Warning** — Des changements ont été sauvegardés★ / [continuer]
    - _Avis de Configuration_
- [select] **Esc=Exit Menu**
    - _F10=Save and Exit_
- [select] **Mot de Passe Invalide! Enter nouvelle chaîneou configurez le mot de passe.**
    - _Quitter en Sauvegardant les Modifications_
- [select] **Ok**
    - _Annuler_
- [select] **Oui**
    - _Non_
- [select] **Changes have been saved after press ** — Question valeur décalage avec l'option valeur!★ / Changes have not saved. Save Changes or not?
    - _Enregistrer les modifications et quitter?_
- [select] **Press 'Y' to save and exit, 'N' to discard and exit.**
    - _Logiciel de Configuration d'InsydeH2O_
- [select] **La presse ENTRE continuer**
    - _S'il vous plaît tape vos données_

## =Essentiel de mouvement  (1 settings)

- [toggle] **<Spacebar>Bascule la Case de pointage**
    - _S'il vous plait tape votre mot de passe_

## Appuie sur DEL sauter examen de mémoire  (3 settings)

- [toggle] **le Système rencontre les erreurs de mémoire**
- [select] **Which USB boot option do you want to select?** — System doesn't have any CD/DVD boot option. Please select other boot option in Boot Manager Menu. / Which network boot option do you want to select?★
    - _Which CD/DVD boot option do you want to select?_
- [select] **The timeout value is %d seconds and it is larger than maximum timeout value %d. Restore timeout variable to %d!!!**

## ￱請輸入足夠字元￰  (21 settings)

- [select] **￱按下￰PageDown  ￱下一頁￰** — ￱說明￰★ / ￱選擇項目￰ / ↑↓
    - _F1_
- [toggle] **F5/F6** — + =￱上移選擇項￰ / ￱變更已儲存￰
    - _￱調整數值￰_
- [select] **Press 'Y' to save and exit, 'N' to discard and exit.** — <￱空白鍵￰>￱勾選查核方塊￰ / 0-9 a-f￱為有效輸入￰★
    - _￱系微設置工具￰_
- [select] **[￱繼續￰]** — ￱更改尚未儲存。儲存更改並離開？￰ / ￱問題值與可選值不符￰ / Changes have not saved. Save Changes or not?★
- [select] **Setup Warning** — ￱變更已儲存￰
    - _￱設定通知￰_
- [number] **￱更改尚未儲存。儲存更改並離開？￰**
    - _￱問題值與可選值不符￰_
- [number] **Changes have not saved. Save Changes or not?**
    - _Press 'Y' to save and exit, 'N' to discard and exit._
- [number] **￱系微設置工具￰**
- [number] **Rev. 5.0**
    - _Esc=Exit Menu_
- [select] **F10=Save and Exit** — + =￱上移選擇項￰ / ￱變更已儲存￰
    - _￱無效的密碼￰!￱請重輸設定密碼￰_
- [number] **￱離開並儲存設定￰**
    - _￱確定￰_
- [number] **￱取消￰**
    - _￱是￰_
- [number] **￱否￰** — + =￱上移選擇項￰ / ￱變更已儲存￰
    - _￱一般幫助訊息￰_
- [number] **￱按下￰PageUp    ￱上一頁￰**
    - _￱按下￰PageDown  ￱下一頁￰_
- [number] **F1**
    - _￱說明￰_
- [number] **↑↓**
    - _￱選擇項目￰_
- [number] **F9**
    - _￱預設值￰_
- [number] **Esc**
    - _￱離開￰_
- [number] **←→**
    - _￱選擇功能表￰_
- [select] **Enter** — + =￱上移選擇項￰ / ￱變更已儲存￰
    - _￱選取￰ ► ￱子功能表￰_
- [number] **F10**
    - _￱儲存並離開￰_

## Dirección MAC permanente  (7 settings)

- [select] **PCI Bus:Dispositivo:Número de función de este dispositivo.** — Dirección PCI / Bus:Dispositivo:Función★
    - _Estado del enlace_
- [select] **Estado del enlace** — Desconectado / LED intermitentes / Bus:Dispositivo:Función★
    - _Conectado_
- [select] **LED intermitentes con una duración de hasta 15 segundos.** — Protocolo de arranque heredado / Bus:Dispositivo:Función★
    - _Protocolo de arranque heredado_
- [select] **Seleccionar protocolo de arranque no UEFI: Entorno de ejecución de arranque previo (PXE)/iSCSI.** — Protocolo de arranque heredado / iSCSI / Bus:Dispositivo:Función★
    - _PXE_
- [select] **NADA** — Tipo de autocarga★ / Seleccionar tipo de autocarga.
    - _Nada_
- [select] **Configurar velocidad de enlace.** — Protocolo de arranque heredado / iSCSI / Bus:Dispositivo:Función★
    - _Wake on LAN (WOL) (LAN de reactivación) previa al inicio del sistema_
- [select] **Configurar Wake on LAN (WOL) (LAN de reactivación) previa al inicio del sistema.** — Protocolo de arranque heredado / iSCSI / Bus:Dispositivo:Función★
    - _Wake on LAN (WOL) (LAN de reactivación)_

## Estado del enlace  (4 settings)

- [select] **Int 18 h** — Dirección MAC / Tiempo de espera de mensaje de banner / iqn.1995-05.com.broadcom.iscsiboot★
    - _Int 19 h_
- [select] **Seleccionar valor para el tiempo de espera. (0 establece de forma predeterminada 4 segundos, 15 es sin retraso, 1-14 es el valor de tiempo de espera en segundos)** — BRCM ISAN / 0.0.0.0★
- [select] **Ocultar solicitud de configuración** — Dirección MAC / Dirección MAC permanente★
- [select] **100 Mbps media** — Dirección MAC
    - _100 Mbps llena_

## Protocolo de arranque heredado  (28 settings)

- [select] **Seleccionar tipo de autocarga.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Velocidad de enlace_
- [select] **Velocidad de enlace** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Configurar velocidad de enlace._
- [select] **Configurar parámetros de Multiple Boot Agent (MBA).** — Configuración NIC★
    - _Configuración NIC_
- [select] **Modo LAN virtual** — ID de VLAN (1..4094)★ / ID de LAN virtual
    - _Configurar modo LAN virtual._
- [select] **10 Mbps llena** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _100 Mbps media_
- [select] **100 Mbps llena** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Deshabilitado_
- [select] **Habilitado** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Un solo uso desactivado_
- [select] **IPv4** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _IPv6_
- [select] **Configurar ID de LAN virtual (1..4094).** — 10 Mbps media★ / 10 Mbps llena
    - _AutoNeg_
- [select] **100 Mbps media** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _100 Mbps llena_
- [select] **Negociación auto.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _10 Mbps media_
- [select] **Wake on LAN (WOL) (LAN de reactivación) previa al inicio del sistema** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configurar Wake on LAN (WOL) (LAN de reactivación) previa al inicio del sistema._
- [select] **Parámetros de primer destino de iSCSI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurar parámetros de primer destino de iSCSI.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Parámetros de segundo destino de iSCSI_
- [select] **ID de dispositivo PCI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
- [select] **Parámetros de segundo destino de iSCSI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurar parámetros de segundo destino iSCSI.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Dispositivo secundario_
- [select] **Arranque en destino** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Habilitar/Deshabilitar arranque en destino iSCSI tras el inicio de sesión._
- [select] **ASF** — Dirección MAC / Dirección MAC permanente★
    - _NC-SI_
- [select] **Prefijo de máscara de subred** — Dirección MAC permanente / Configurar secreto CHAP (entre 12 y 16 caracteres de longitud).★
    - _Configurar longitud de prefijo de máscara de subred de IP._
- [select] **Puerta de enlace predeterminada** — Dirección MAC / Dirección MAC permanente★
    - _Configurar dirección IP de puerta de enlace predeterminada._
- [select] **Máscara de subred** — Dirección MAC / Dirección MAC permanente★
    - _Configurar máscara de subred de IP._
- [select] **CCM** — Dirección MAC / Dirección MAC permanente★
    - _UMP_
- [select] **EFI** — Dirección MAC / Dirección MAC permanente★
- [select] **Fcode** — Dirección MAC / Dirección MAC permanente★
- [select] **Versión BIOS del controlador** — Dirección MAC / Dirección MAC permanente★
- [select] **MBA** — Dirección MAC / Dirección MAC permanente★
- [select] **Arranque iSCSI** — Dirección MAC / Dirección MAC permanente★

## NADA  (4 settings)

- [select] **ID CHAP** — Dirección MAC / Dirección MAC permanente★
- [select] **Configurar identificación CHAP (hasta 32 caracteres de longitud).** — Dirección MAC / Dirección MAC permanente★
    - _Configurar identificación CHAP (hasta 128 caracteres de longitud)._
- [select] **Secreto CHAP** — Dirección MAC / Dirección MAC permanente★
- [select] **Parámetros de segundo destino de iSCSI** — Dirección MAC / Dirección MAC permanente★
    - _Configurar parámetros de segundo destino iSCSI._

## Erste iSCSI-Zielparameter  (3 settings)

- [select] **Verbinden** — Deaktiviert★ / Aktiviert
    - _Zielherstellung aktivieren/deaktivieren._
- [number] **TCP-Port**
    - _Ziel-TCP.Port-Nummer (1..65535) konfigurieren._
- [number] **Boot-LUN**
    - _Ziel-Boot-LUN-Nummer (0..255) konfigurieren._

## Zweite iSCSI-Zielparameter  (3 settings)

- [select] **Verbinden** — Deaktiviert★ / Aktiviert
    - _Zielherstellung aktivieren/deaktivieren._
- [number] **TCP-Port**
    - _Ziel-TCP.Port-Nummer (1..65535) konfigurieren._
- [number] **Boot-LUN**
    - _Ziel-Boot-LUN-Nummer (0..255) konfigurieren._

## MBA-Konfigurationsmenü  (10 settings)

- [select] **Option ROM** — Deaktiviert / Aktiviert★
    - _Boot Option ROM aktivieren/deaktivieren_
- [select] **Bootprotokolle älterer Geräte** — PXE / iSCSI / NONE
    - _Nicht-UEFI Boot-Protokoll auswählen: Preboot Execution Environment (PXE)/iSCSI._
- [select] **Boot-Strap-Typ** — Auto Erkennung★ / BBS / Int. 18 Std. / Int. 19 Std.
    - _Boot-Strap-Typ auswählen._
- [select] **Eingabeaufforderung ausblenden** — Deaktiviert★ / Aktiviert
    - _Konfigurieren, ob die Eingabeaufforderung während der ROM-Initialisierung angezeigt wird._
- [select] **Tastenanschlag eingeben** — Strg-S★ / Strg-B
    - _Tastenanschläge konfigurieren, um das Konfigurationsmenü aufzurufen._
- [number] **Banner-Nachricht Zeitüberschreitung**
    - _Wert für Zeitüberschreitung auswählen. (0 ist standardmäßig auf 4 Sekunden eingestellt, 15 bedeutet keine Zeitüberschreitung, 1-14 ist der Wert der Zeitübers..._
- [select] **Übertragungsrate** — Auto Neg★ / 10 Mbps Halb / 10 Mbps Voll / 100 Mbps Halb / 100 Mbps Voll
    - _Übertragungsrate konfigurieren._
- [select] **Pre-boot Wake On LAN** — Deaktiviert / Aktiviert
    - _Pre-boot Wake On LAN (WOL) konfigurieren_
- [select] **VLAN-Modus** — Deaktiviert★ / Aktiviert
    - _Virtuellen LAN-Modus konfigurieren._
- [number] **VLAN-ID (1..4094)**
    - _Virtuelle LAN-ID (1..4094) konfigurieren._

## Sekundäres Gerät  (2 settings)

- [select] **Unabhängiges Zielportal verwenden** — Deaktiviert★ / Aktiviert
    - _Unabhängiges Zielportal verwenden wenn Multipath I/O aktiviert ist._
- [select] **Unabhängigen Zielnamen verwenden** — Deaktiviert★ / Aktiviert
    - _Unabhängigen Zielnamen verwenden wenn Multipath I/O aktiviert ist._

## iSCSI-Parameter des sekundären Geräts  (2 settings)

- [select] **Unabhängiges Zielportal verwenden** — Deaktiviert★ / Aktiviert
    - _Unabhängiges Zielportal verwenden wenn Multipath I/O aktiviert ist._
- [select] **Unabhängigen Zielnamen verwenden** — Deaktiviert★ / Aktiviert
    - _Unabhängigen Zielnamen verwenden wenn Multipath I/O aktiviert ist._

## NIC-Konfiguration  (10 settings)

- [select] **Option ROM** — Deaktiviert / Aktiviert
    - _Boot Option ROM aktivieren/deaktivieren_
- [select] **Bootprotokolle älterer Geräte** — PXE / iSCSI / None
    - _Nicht-UEFI Boot-Protokoll auswählen: Preboot Execution Environment (PXE)/iSCSI._
- [select] **Boot-Strap-Typ** — Auto Erkennung★ / BBS / Int. 18 Std. / Int. 19 Std.
    - _Boot-Strap-Typ auswählen._
- [select] **Eingabeaufforderung ausblenden** — Deaktiviert★ / Aktiviert
    - _Konfigurieren, ob die Eingabeaufforderung während der ROM-Initialisierung angezeigt wird._
- [select] **Tastenanschlag eingeben** — Strg-S★ / Strg-B
    - _Tastenanschläge konfigurieren, um das Konfigurationsmenü aufzurufen._
- [number] **Banner-Nachricht Zeitüberschreitung**
    - _Wert für Zeitüberschreitung auswählen. (0 ist standardmäßig auf 4 Sekunden eingestellt, 15 bedeutet keine Zeitüberschreitung, 1-14 ist der Wert der Zeitübers..._
- [select] **Übertragungsrate** — Automatische Aushandlung★ / 10 Mbps Halb / 10 Mbps Voll / 100 Mbps Halb / 100 Mbps Voll
    - _Übertragungsrate konfigurieren._
- [select] **Wake On LAN** — Deaktiviert / Aktiviert
    - _Wake on LAN (WOL) konfigurieren_
- [select] **Virtuellen LAN-Modus** — Deaktiviert★ / Aktiviert
    - _Virtuellen LAN-Modus konfigurieren._
- [number] **Virtuelle LAN-ID**
    - _Virtuelle LAN-ID (1..4094) konfigurieren._

## Patent Information  (1 settings)

- [toggle] **Host Configuration**

## Get driver information and configure Realtek ethernet controller parameter  (1 settings)

- [number] **100 Mpbs Half Duplex**
    - _10 Mpbs Full Duplex_

## Main Configuration Page  (6 settings)

- [select] **Disable HP Shared Memory features** — Disabled / Enabled★
    - _Disable usage of reserved memory regions to allow direct assignment of device to guest virtual machines._
- [number] **Blink LEDs**
    - _Blink LEDs for a duration up to 15 seconds._
- [select] **Energy Efficient Ethernet** — Disabled / Maximum Power Savings
    - _Configure Energy Efficient Ethernet operation._
- [select] **Pre-boot Wake On LAN** — Disabled / Enabled
    - _Configure Pre-boot Wake on LAN (WOL)._
- [select] **Link Status** — Disconnected / Connected
- [select] **iSCSI First Target Parameters** — MAC Address / Permanent MAC Address★

## iSCSI General Parameters  (14 settings)

- [select] **TCP/IP Parameters via DHCP** — Disabled / Enabled★
    - _Acquire TCP/IP configuration via DHCP._
- [select] **IP Autoconfiguration** — Disabled / Enabled★
    - _Acquire TCP/IP configuration via Stateful or Stateless Autoconfiguration._
- [select] **IP Auto-Configuration** — Disabled / Enabled★
    - _Acquire TCP/IP configuration via Stateful or Stateless Autoconfiguration._
- [select] **iSCSI Parameters via DHCP** — Disabled / Enabled★
    - _Acquire iSCSI parameters via DHCP._
- [select] **CHAP Authentication** — Disabled★ / Enabled
    - _Enable/Disable CHAP authentication._
- [select] **Boot to iSCSI Target** — Disabled / Enabled★ / One Time Disabled
    - _Enable/Disable booting to iSCSI target after logon._
- [select] **Boot to Target** — Disabled / Enabled★ / One Time Disabled
    - _Enable/Disable booting to iSCSI target after logon._
- [number] **Link Up Delay Time**
    - _Configure link up delay time in seconds (0..255)._
- [select] **Use TCP Timestamp** — Disabled★ / Enabled
    - _Enable/Disable TCP timestamp._
- [select] **TCP Timestamp** — Disabled★ / Enabled
    - _Enable/Disable TCP timestamp._
- [select] **Target as First HDD** — Disabled★ / Enabled
    - _Enable/Disable target appears as first hard disk drive (HDD) in the system._
- [number] **LUN Busy Retry Count**
    - _Configure number of retries in 2 second intervals when LUN is busy (0..60)._
- [select] **IP Version** — IPv4★ / IPv6
    - _IP version support.  Modifying this parameter will reset all IP-related fields._
- [select] **iSCSI First Target Parameters** — MAC Address / Permanent MAC Address★

## iSCSI Initiator Parameters  (1 settings)

- [select] **iSCSI First Target Parameters** — MAC Address / Permanent MAC Address★

## iSCSI First Target Parameters  (3 settings)

- [select] **Connect** — Disabled★ / Enabled
    - _Enable/Disable target establishment._
- [number] **TCP Port**
    - _Configure target TCP port number (1..65535)._
- [number] **Boot LUN**
    - _Configure target boot LUN number (0..255)._

## iSCSI Second Target Parameters  (3 settings)

- [select] **Connect** — Disabled★ / Enabled
    - _Enable/Disable target establishment._
- [number] **TCP Port**
    - _Configure target TCP port number (1..65535)._
- [number] **Boot LUN**
    - _Configure target boot LUN number (0..255)._

## MBA Configuration Menu  (10 settings)

- [select] **Option ROM** — Disabled / Enabled★
    - _Enable/Disable Boot Option ROM_
- [select] **Legacy Boot Protocol** — PXE / iSCSI / NONE
    - _Select non-UEFI Boot Protocol: Preboot Execution Environment (PXE)/iSCSI._
- [select] **Boot Strap Type** — Auto Detect★ / BBS / Int 18h / Int 19h
    - _Select boot strap type._
- [select] **Hide Setup Prompt** — Disabled★ / Enabled
    - _Configure whether Setup Prompt is displayed during ROM initialization._
- [select] **Setup Key Stroke** — Ctrl-S★ / Ctrl-B
    - _Configure key strokes to invoke configuration menu._
- [number] **Banner Message Timeout**
    - _Select timeout value. (0 defaults to 4 seconds, 15 is no delay, 1-14 is timeout value in seconds)_
- [select] **Link Speed** — AutoNeg★ / 10Mbps Half / 10Mbps Full / 100Mbps Half / 100Mbps Full
    - _Configure link speed._
- [select] **Pre-boot Wake On LAN** — Disabled / Enabled
    - _Configure Pre-boot Wake on LAN (WOL)._
- [select] **VLAN Mode** — Disabled★ / Enabled
    - _Configure virtual LAN mode._
- [number] **VLAN ID (1..4094)**
    - _Configure virtual LAN ID (1..4094)._

## Secondary Device  (2 settings)

- [select] **Use Independent Target Portal** — Disabled★ / Enabled
    - _Use independent target portal when multipath I/O is enabled._
- [select] **Use Independent Target Name** — Disabled★ / Enabled
    - _Use independent target name when multipath I/O is enabled._

## iSCSI Secondary Device Parameters  (2 settings)

- [select] **Use Independent Target Portal** — Disabled★ / Enabled
    - _Use independent target portal when multipath I/O is enabled._
- [select] **Use Independent Target Name** — Disabled★ / Enabled
    - _Use independent target name when multipath I/O is enabled._

## NIC Configuration  (10 settings)

- [select] **Option ROM** — Disabled / Enabled
    - _Enable/Disable Boot Option ROM_
- [select] **Legacy Boot Protocol** — PXE / iSCSI / None
    - _Select non-UEFI Boot Protocol: Preboot Execution Environment (PXE)/iSCSI._
- [select] **Boot Strap Type** — Auto Detect★ / BBS / Int 18h / Int 19h
    - _Select boot strap type._
- [select] **Hide Setup Prompt** — Disabled★ / Enabled
    - _Configure whether Setup Prompt is displayed during ROM initialization._
- [select] **Setup Key Stroke** — Ctrl-S★ / Ctrl-B
    - _Configure key strokes to invoke configuration menu._
- [number] **Banner Message Timeout**
    - _Select timeout value. (0 defaults to 4 seconds, 15 is no delay, 1-14 is timeout value in seconds)_
- [select] **Link Speed** — Auto Negotiated★ / 10 Mbps Half / 10 Mbps Full / 100 Mbps Half / 100 Mbps Full
    - _Configure link speed._
- [select] **Wake On LAN** — Disabled / Enabled
    - _Configure Wake on LAN (WOL)._
- [select] **Virtual LAN Mode** — Disabled★ / Enabled
    - _Configure virtual LAN mode._
- [number] **Virtual LAN ID**
    - _Configure virtual LAN ID (1..4094)._

## Select a UEFI file as trusted for execution  (3 settings)

- [select] **Delete PK** — Unlocked★ / Deployed Mode
    - _Enter into Delete PK Form_
- [select] **KEK Signature List:** — Secure Boot Mode★ / Setup Mode
    - _Enroll KEK_
- [select] **KEK Options** — Secure Boot Mode★ / Setup Mode
    - _Enroll/Delete KEK_

## Enforce Secure Boot  (1 settings)

- [select] **Enroll/Delete Signature** — Secure Boot Mode / User Mode★
    - _DB Signature List:_

## Erase all Secure Boot Settings  (5 settings)

- [select] **SHA1** — SHA256 / X509_SHA256★
    - _[Error] PK already exists._
- [select] **Delete Signature** — RSA2048_SHA256★ / PKCS7
    - _Unknown_
- [select] **[Error] There is already an identical signature in signature list.** — Secure Boot Mode★ / Setup Mode
    - _[Error] Invalid GUID string. GUID string should be in 12345678-1234-1234-1234-1234567890ab format._
- [select] **Input Owner_GUID in 12345678-1234-1234-1234-1234567890ab format.** — Secure Boot Mode / Setup Mode★
    - _The operation is only allowed before booting any boot device!!! Please reset system and enter this menu directly if need use this operation._
- [select] **Press Esc for boot options** — Secure Boot Mode / Setup Mode★
    - _Esc is pressed. Go to boot options._

## 2400  (6 settings)

- [select] **Console Input Device Select** — Set Legacy HardDisk Drive Order / Set Legacy CD-ROM Drive Order / Set Legacy NET Drive Order
    - _Set Legacy Floppy Drive Order_
- [select] **Console Output Device Select**
    - _Console Standard Error Device Select_
- [select] **Enable console device as StdErr** — Set Console Output Mode★ / Set COM Attributes / Set COM Terminal Type / Set COM Flow Control / Set COM Baud Rate
    - _Select Console Output Mode: 80x25, 100x31, etc._
- [select] **COM Attribute Setup Page** — 38400 / 19200
    - _Setup ComPort BaudRate, DataBits, StopBits, Parity and TerminalType_
- [select] **Boot Next Value** — 38400★ / 19200
    - _Input the description_
- [number] **Load Option Reconnect**
    - _Discard Changes and Exit_

## 1200  (6 settings)

- [select] **Enable console device as ConIn** — Set Legacy HardDisk Drive Order / Set Legacy CD-ROM Drive Order / Set Legacy BEV Drive Order
    - _Set Legacy Floppy Drive Order_
- [select] **Enable console device as ConOut**
    - _Console Standard Error Device Select_
- [select] **Console Output Mode Select** — Set COM Data Bits★ / Set COM Parity / Set COM Stop Bits / 115200 / 57600
    - _Select Console Output Mode: 80x25, 100x31, etc._
- [select] **Add Driver Option Using File** — 38400 / 19200
    - _Add Driver Option Using Handle_
- [select] **Next boot use this boot option** — 38400★ / 19200
    - _Input the description_
- [number] **Commit Changes and Exit**
    - _Discard Changes and Exit_

## VLAN モード  (41 settings)

- [select] **multipath I/O がイネーブルな場合、独立したターゲット ポータルを使用する。** — 独立したターゲット ポータルを使用 / セカンダリ デバイスの MAC アドレスを入力する。XX:XX:XX:XX:XX:XX 形式を使用する。★
    - _独立したターゲット名を使用_
- [select] **EFI** — コントローラのBIOSバージョン★ / MBA
    - _Fcode_
- [select] **NICの設定** — iSCSI ブート コンフィギュレーション メニュー★ / iSCSI の設定 / iSCSI ブート パラメタを設定する。
    - _iSCSI ブート コンフィギュレーション メニュー_
- [toggle] **iSCSI の設定** — 旧式ブート プロトコル / VLAN ID (1..4094) / バス：デバイス：機能★
    - _ファームウェア イメージ メニュー_
- [select] **00:00:00:00:00:00** — PCI デバイス ID★
- [toggle] **キー操作のセットアップ**
    - _コンフィギュレーション メニューを呼び出すキー操作を設定する。_
- [toggle] **Ctrl-S**
    - _Ctrl-B_
- [toggle] **バナー メッセージのタイムアウト**
- [toggle] **タイムアウト値を選択する。(0 はデフォルトの 4 秒、15 は遅延なし、1 ～ 14 は秒単位のタイムアウト値)**
    - _BRCM ISAN_
- [toggle] **0.0.0.0**
    - _iqn.1995-05.com.broadcom.iscsiboot_
- [toggle] **MAC アドレス** — MAC アドレス★
- [select] **100 Mbps 半二重** — ブート ストラップのタイプ / ナシ★ / 旧式ブート プロトコル / VLAN ID (1..4094) / バス：デバイス：機能
    - _100 Mbps 全二重_
- [select] **バーチャル LAN ID** — 自動ネゴシエーション / 10 Mbps 半二重 / 10 Mbps 全二重★
    - _バーチャル LAN ID (1..4094) を構成します。_
- [select] **仮想 LAN** — VLAN ID (1..4094) / バス：デバイス：機能★
    - _仮想 LAN モードを設定する。_
- [number] **自動ネゴシエーション**
    - _10 Mbps 半二重_
- [number] **10 Mbps 全二重**
    - _100 Mbps 半二重_
- [number] **100 Mbps 全二重**
    - _自動ネゴシエート済み_
- [number] **10 Mbps 半二重**
    - _10 Mbps 全二重_
- [number] **無効**
    - _有効_
- [number] **一時的に無効**
    - _IPv4_
- [number] **IPv6**
    - _MBA コンフィギュレーション メニュー_
- [select] **MBA コンフィギュレーション メニュー** — 旧式ブート プロトコル / VLAN ID (1..4094) / バス：デバイス：機能★
    - _MBA (Multiple Boot Agent) パラメタを設定する。_
- [number] **iSCSI ブート コンフィギュレーション メニュー**
- [number] **iSCSI ブート パラメタを設定する。**
    - _iSCSI の設定_
- [number] **ファームウェア イメージ メニュー**
    - _ファームウェア イメージの情報。_
- [number] **現在 NVRAM 上にプログラムされているファームウェア イメージ コンポーネント (およびそれらに対応するバージョン) のリスト。[該当なし] はイメージが存在しないことを示します。**
- [select] **ファームウェア イメージのプロパティ** — 旧式ブート プロトコル / VLAN ID (1..4094) / バス：デバイス：機能★
    - _DHCP 経由の TCP/IP パラメタ_
- [number] **DHCP 経由で TCP/IP コンフィギュレーションを取得する。**
    - _IP 自動コンフィギュレーション_
- [number] **IP 自動コンフィギュレーション**
    - _ステートフルまたはステートレスな自動コンフィギュレーションで TCP/IP コンフィギュレーションを取得する。_
- [number] **DHCP 経由の iSCSI パラメタ**
    - _DHCP 経由で iSCSI パラメタを取得する。_
- [select] **CHAP 認証** — 旧式ブート プロトコル / VLAN ID (1..4094) / バス：デバイス：機能★
    - _CHAP 認証をイネーブル/ディスエーブルする。_
- [number] **iSCSI ターゲットでのブート**
    - _ターゲットでのブート_
- [number] **ログオン後の iSCSI ターゲットでのブートをイネーブル/ディスエーブルする。**
    - _DHCP ベンダ ID_
- [number] **DHCP ベンダ ID を設定する (32 バイトまで)。**
    - _リンク アップ遅延時間_
- [select] **リンク アップの遅延時間を秒単位で設定する (0 ～ 255 秒)。** — 旧式ブート プロトコル / VLAN ID (1..4094) / バス：デバイス：機能★
    - _TCP タイムスタンプを使用_
- [number] **TCP タイムスタンプ**
    - _TCP タイムスタンプをイネーブル/ディスエーブルする。_
- [number] **ターゲットをファースト HDD として表示**
    - _ターゲットをシステムのファースト ハード ディスク ドライブ (HDD) として表示することをイネーブル/ディスエーブルする。_
- [number] **LUN ビジー再試行カウント**
    - _LUN がビジーな場合に、2 秒置きに何回再試行するか設定する (0 ～ 60 回)。_
- [select] **IP バージョン** — 旧式ブート プロトコル / VLAN ID (1..4094) / バス：デバイス：機能★
    - _IP バージョンのサポート。このパラメタを変更するとすべての IP 関連のフィールドがリセットされます。_
- [number] **IP アドレス**
    - _イニシエータ IP アドレスを設定する。_
- [select] **サブネット マスク** — 旧式ブート プロトコル / iSCSI / バス：デバイス：機能★
    - _IP サブネットマスクを設定する。_

## SMASH  (5 settings)

- [select] **Current Work Protocol FCoE/FC** — Bus:Device:Function★ / ISCSISecondTargetParameters_BootLUN
- [number] **Current Work Protocol iSCSI**
- [select] **FCoE Permanent Address** — Bus:Device:Function★ / ISCSISecondTargetParameters_BootLUN / FCoE Network Addresses / Connection Type
- [select] **Connection Type** — Bus:Device:Function★ / FCoE Network Addresses / Connection Type
- [select] **Role** — Bus:Device:Function★ / FCoE Network Addresses / Connection Type

## Force HDMI signals route over USB Type C port  (7 settings)

- [select] **AcDcSwitch** — Manual★ / Enabled 
    - _AmdDcTimer_
- [select] **Enable/disable AcDcSwitch.** — Manual / Enabled ★
    - _AmdDcTimer_
- [select] **Enable/Disable BLINK LED to identify S3/S4 state** — Enabled (x4) / Manual★
    - _GPIO 11 Output Low_
- [select] **AmdDcTimer Setting.** — Manual / Enabled ★
    - _AmdAcTimer_
- [select] **SATA/ SATA express selection  Setting.** — Manual★ / VDDP voltage / SATA express
    - _SATA_
- [number] **VDDP voltage (0.9V)**
    - _Enable/Disable HybridGraphics_
- [select] **AmdAcTimer Setting.** — Manual★ / Enabled 
    - _SATA/ SATA express selection_

## Native USB Type-C  (2 settings)

- [select] **VDDP voltage (+10mv)** — Manual / Enabled ★
    - _VDDP voltage (+20mv)_
- [select] **VDDP voltage (+30mv)** — Manual / Enabled (x4)★
    - _VDDP voltage (+40mv)_

## <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,28,160,28' ><VerticalLayout ><Label name='showstring' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout  name='content' height='30' /></VerticalLayout>  (42 settings)

- [number] **+/- =Adjust Value**
    - _+ =Move Selection Up_
- [select] **- =Move Selection Down** —  =Select From Choices★ / 0123456789 are valid inputs
    - _=Move Highlight_
- [select] **<VerticalLayout bkcolor='0xFFFFFFFF'><HorizontalLayout inset='0,2,0,2' ><Container name='setupmenu_panel' inset='0,55,0,0' width='300' bkcolor='0xFFF4F4F4' ><VerticalLayout name ='setupmenulist' /></Container><VerticalLayout inset='0,0,0,0' ><Label height='55' name='sub_title' fontsize='40' height='55' /><HorizontalLayout><VerticalLayout name ='menuoptionlist' vscrollbar='true' inset2='10' childpadding='5' /><VerticalLayout width='40' inset='4,0,4,0' name='bootorder' ><Control /><Button name='up'   width='32' height='32' normalimage='@BootOrderUpNormal' hotimage='@BootOrderUpFocus' pushimage='@BootOrderUpPush' /><Button name='down' width='32' height='32' normalimage='@BootOrderUpNormal' hotimage='@BootOrderUpFocus' pushimage='@BootOrderUpPush' /><Control /></VerticalLayout></HorizontalLayout></VerticalLayout></HorizontalLayout><HorizontalLayout height='50' ><Control /><Button name='exit' text='Exit' bkcolor='0xFF123456' align='center' width='70' height='30' /></HorizontalLayout></VerticalLayout>** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFFFFFFFF' bkcolor='0' bkcolor2='0' bkcolor3='0' bkimagestyle='' bkimage='@ButtonNormal' scale9g..._
- [select] **N** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Please enter enough characters_
- [select] **textcolor='0x00FFFFFF' gradient_vertical='false' textpadding='5,1,1,5' borderround='0,0' fontsize='23' bordercolor='0x80888888'**
    - _textcolor='0x00FFFFFF' gradient_vertical='false' textpadding='5,1,1,5' borderround='0,0' fontsize='23' bordercolor='0x80888888' bkcolor3='0' align='bottom'_
- [select] **<Enter>=Select Entry** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _<Enter>=Complete Entry_
- [select] **Esc=Exit Entry** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Esc=Discard Changes_
- [select] **F9=Reset to Defaults** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _F10=Save_
- [select] **Failed to Save** — + =Move Selection Up★ / - =Move Selection Down
    - _+/- =Adjust Value_
- [select] **=Move Highlight** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>★ / 0123456789 are valid inputs
    - _ =Select From Choices_
- [select] **0-9 a-f are valid inputs** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _<Spacebar>Toggle Checkbox_
- [number] **Enter current password**
    - _Enter New Password_
- [number] **Confirm New Password** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Password do not match_
- [number] **Invalid password**
    - _Re-enter Password_
- [number] **Please type in your data**
    - _NV_
- [select] **!!** — Are you sure? (Y/N)★ / Y
- [select] **Enter Old password** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Enter New Password_
- [select] **Enter old password incorrect !** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _New password confirm fail !_
- [select] **Enter incorrect password over 3 times, system will halt !!** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / Press Esc for boot options★ / Esc is pressed. Go to boot options.
    - _Copyright (C) Acer Inc._
- [select] **Password check Fail!! ** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Add an new file\Do you wish to add this file to allowable database?_
- [select] **Change Values** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Setup Default_
- [select] **Exit** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _Save and Exit_
- [select] **Setup Warning** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Setup Notice_
- [select] **Changes have been saved.** — Changes have been saved after press ★ / Changes have not saved. Save Changes and exit?
    - _[continue]_
- [select] **Question value mismatch with Option value!** — Press 'Y' to save and exit, 'N' to discard and exit.★ / InsydeH2O Setup Utility
    - _Changes have not saved. Save Changes or not?_
- [select] **InsydeH2O Setup Utility (Manufacture)** — Esc=Exit Menu / F10=Save and Exit★ / Invalid password! Please enter new string for setting password.
    - _Rev. 5.0_
- [select] **Exit Saving Changes** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _Ok_
- [select] **No** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _[General Help]_
- [select] **Cancel** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★ / <VerticalLayout name='background' bkcolor='0xFF000000'><Control /><HorizontalLayout height='530' ><Control /><CellLayout name='menuoptionlist' width='710' inset='0,0,0,0' cellwidth='170' cellheight='170' widthgap='10' heightgap='10' /><Control /></HorizontalLayout><Control /></VerticalLayout>
    - _Yes_
- [select] **Push PageUp    - previous** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _Push PageDown  - Next Page_
- [select] **Help** — Select Item / Select Menu / Select★
- [select] **F1** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Help_
- [select] **↑↓** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Select Item_
- [select] **F5/F6** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Change Values_
- [select] **F9** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Setup Defaults_
- [select] **Esc** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Exit_
- [select] **←→** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _Select Menu_
- [select] **Enter** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Select ► Sub-Menu_
- [select] **F10** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _Save and Exit_
- [select] **Item Specific Help** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _System Halted_
- [toggle] **<VerticalLayout name='background' bkcolor='0xFF004D60' inset='16,28,16,28' ><Label name='title' height='60' align='center' fontsize='40' textcolor='0xFFFFFF' /><VerticalLayout vscrollbar='true' ><Label name='showstring' fontsize='20' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout  name='content' height='30' /></VerticalLayout>**
    - _<VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />_
- [toggle] **<VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,28,160,28' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout height='30'><Label name='oldpasswordtext' fontsize='24' textcolor='0xFFFFFF' textpadding='2,0,2,0' width='400' /><UiEdit name='oldpassword' width='160' fontsize='24' textcolor='0xFF000000' password='true' textpadding='5,0,5,0' /></HorizontalLayout><HorizontalLayout height='30'><Label name='newpasswordtext' fontsize='24' textcolor='0xFFFFFF' textpadding='2,0,2,0' width='400' /><UiEdit name='newpassword' width='160' fontsize='24' textcolor='0xFF000000' password='true' textpadding='5,0,5,0' /></HorizontalLayout><HorizontalLayout height='30'><Label name='confirmpasswordtext' fontsize='24' textcolor='0xFFFFFF' textpadding='2,0,2,0' width='400' /><UiEdit name='confirmpassword' width='160' fontsize='24' textcolor='0xFF000000' password='true' textpadding='5,0,5,0' /></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='cancel' fontsize='24' /></HorizontalLayout></VerticalLayout>**

## Modo VLAN  (41 settings)

- [select] **Utilizar portal de destino independiente cuando esté habilitada la E/S de múltiples rutas.** — Utilizar portal de destino independiente / Introducir dirección MAC de dispositivo secundario. Utilizar formato XX:XX:XX:XX:XX:XX.★
    - _Utilizar nombre de destino independiente_
- [select] **EFI** — Versión BIOS del controlador★ / MBA
    - _Fcode_
- [select] **Configuración NIC** — Menú de configuración de arranque iSCSI★ / Configuración iSCSI / Configurar parámetros de arranque iSCSI.
    - _Menú de configuración de arranque iSCSI_
- [toggle] **Configuración iSCSI** — Protocolo de arranque heredado / ID de VLAN (1..4094) / Bus:Dispositivo:Función★
    - _Menú de imagen de firmware_
- [select] **00:00:00:00:00:00** — ID de dispositivo PCI★
- [toggle] **Configurar pulsación de tecla**
    - _Configurar pulsaciones de teclas para llamar al menú de configuración._
- [toggle] **Ctrl-S**
    - _Ctrl-B_
- [toggle] **Tiempo de espera de mensaje de banner**
- [toggle] **Seleccionar valor para el tiempo de espera. (0 establece de forma predeterminada 4 segundos, 15 es sin retraso, 1-14 es el valor de tiempo de espera en segundos)**
    - _BRCM ISAN_
- [toggle] **0.0.0.0**
    - _iqn.1995-05.com.broadcom.iscsiboot_
- [toggle] **Dirección MAC** — Dirección MAC★
- [select] **100 Mbps media** — Tipo de autocarga / Nada★ / Protocolo de arranque heredado / ID de VLAN (1..4094) / Bus:Dispositivo:Función
    - _100 Mbps llena_
- [select] **ID de LAN virtual** — AutoNeg / 10 Mbps media / 10 Mbps llena★
    - _Configurar ID de LAN virtual (1..4094)._
- [select] **Modo LAN virtual** — ID de VLAN (1..4094) / Bus:Dispositivo:Función★
    - _Configurar modo LAN virtual._
- [number] **AutoNeg**
    - _10 Mbps media_
- [number] **10 Mbps llena**
    - _100 Mbps media_
- [number] **100 Mbps llena**
    - _Negociación auto._
- [number] **10 Mbps media**
    - _10 Mbps llena_
- [number] **Deshabilitado**
    - _Habilitado_
- [number] **Un solo uso desactivado**
    - _IPv4_
- [number] **IPv6**
    - _Menú de configuración MBA_
- [select] **Menú de configuración MBA** — Protocolo de arranque heredado / ID de VLAN (1..4094) / Bus:Dispositivo:Función★
    - _Configurar parámetros de Multiple Boot Agent (MBA)._
- [number] **Menú de configuración de arranque iSCSI**
- [number] **Configurar parámetros de arranque iSCSI.**
    - _Configuración iSCSI_
- [number] **Menú de imagen de firmware**
    - _Información de imagen del firmware._
- [number] **Listado de componentes de imagen de firmware (y sus versiones correspondientes) programados actualmente en NVRAM. N/A indica que la imagen no está presente.**
- [select] **Propiedades de imagen del firmware** — Protocolo de arranque heredado / ID de VLAN (1..4094) / Bus:Dispositivo:Función★
    - _Parámetros de TCP/IP a través de DHCP_
- [number] **Adquirir configuración de TCP/IP a través de DHCP.**
    - _Configuración automática de IP_
- [number] **Configuración auto. de IP**
    - _Adquirir configuración de TCP/IP a través de configuración automática con estado o sin estado._
- [number] **Parámetros de iSCSI a través de DHCP**
    - _Adquirir parámetros de iSCSI a través de DHCP._
- [select] **Autenticación CHAP** — Protocolo de arranque heredado / ID de VLAN (1..4094) / Bus:Dispositivo:Función★
    - _Habilitar/Deshabilitar autenticación CHAP._
- [number] **Arranque en destino iSCSI**
    - _Arranque en destino_
- [number] **Habilitar/Deshabilitar arranque en destino iSCSI tras el inicio de sesión.**
    - _ID de proveedor DHCP_
- [number] **Configurar ID de proveedor DHCP (hasta 32 bytes de longitud).**
    - _Tiempo de retraso de conexión_
- [select] **Configurar el tiempo de retraso de conexión en segundos (0..255).** — Protocolo de arranque heredado / ID de VLAN (1..4094) / Bus:Dispositivo:Función★
    - _Utilizar marca de hora TCP_
- [number] **Sello de tiempo TCP**
    - _Habilitar/Deshabilitar marca de hora TCP._
- [number] **Destino como primera HDD**
    - _Habilitar/Deshabilitar la aparición del destino como primera unidad de disco duro (HDD) en el sistema._
- [number] **Conteo de reintentos con LUN ocupado**
    - _Configurar el número de reintentos en intervalos de 2 segundos cuando el número de unidad lógica (LUN) está ocupado (0..60)._
- [select] **Versión de IP** — Protocolo de arranque heredado / ID de VLAN (1..4094) / Bus:Dispositivo:Función★
    - _Compatibilidad con la versión de IP. Al modificar este parámetro se restablecerán todos los campos relacionados con la IP._
- [number] **Dirección IP**
    - _Configurar dirección IP de iniciador._
- [select] **Máscara de subred** — Protocolo de arranque heredado / iSCSI / Bus:Dispositivo:Función★
    - _Configurar máscara de subred de IP._

## AMD CBS  (6 settings)

- [select] **0xB Clk** — 0xD Clk★ / 0xE Clk
    - _0xC Clk_
- [select] **0xF Clk** — 33h Clk★ / 34h Clk
    - _Trp_
- [number] **Specify the row precharge time.**
    - _Tras_
- [number] **Specify the min RAS# active time.**
    - _22h Clk_
- [number] **23h Clk**
    - _24h Clk_
- [number] **Combo CBS**
    - _No help string_

## 27h Clk  (19 settings)

- [select] **Specifies the core voltage.** — 33h Clk★ / 34h Clk
    - _Custom Pstate2_
- [select] **1433MHz** — 33h Clk / 34h Clk★
    - _1467MHz_
- [select] **1500MHz** — 33h Clk / 34h Clk★
    - _1533MHz_
- [select] **1567MHz** — 33h Clk / 34h Clk★
    - _1600MHz_
- [select] **1633MHz** — 33h Clk / 34h Clk★
    - _1667MHz_
- [select] **1700MHz** — 33h Clk / 34h Clk★
    - _1733MHz_
- [select] **1767MHz** — 33h Clk / 34h Clk★
    - _1800MHz_
- [select] **1833MHz** — 33h Clk / 34h Clk★
    - _1867MHz_
- [select] **1066MHz** — 33h Clk / 34h Clk★
    - _2033MHz_
- [select] **2067MHz** — 33h Clk / 34h Clk★
    - _2100MHz_
- [select] **Tcl** — 33h Clk / 34h Clk★
    - _Sets the tCL time._
- [select] **8 Clk** — 33h Clk / 34h Clk★
    - _9 Clk_
- [select] **0Ah Clk** — 33h Clk / 34h Clk★
    - _0Bh Clk_
- [select] **0Ch Clk** — 33h Clk / 34h Clk★
    - _0Dh Clk_
- [select] **0Eh Clk** — 33h Clk / 34h Clk★
    - _0Fh Clk_
- [select] **10h Clk** — 33h Clk / 34h Clk★
    - _11h Clk_
- [select] **12h Clk** — 33h Clk / 34h Clk★
    - _13h Clk_
- [select] **14h Clk** — 16h Clk / 17h Clk / 18h Clk★
    - _15h Clk_
- [select] **Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah).** — 34h Clk★ / 33h Clk
    - _Pstate2 VID_

## ODD Power Enable  (6 settings)

- [select] **Zero-Power ODD** — HybridGraphics★ / Enable/Disable HybridGraphics
    - _Enable/Disable Zero-Power ODD Feature_
- [select] **SSD x2** — HybridGraphics★ / Enable/Disable HybridGraphics
    - _SSD x4_
- [select] **Camera 1 Enable** — HybridGraphics★ / Enable/Disable HybridGraphics
    - _Enable or disable the power of FRONT CAMERA_
- [select] **WWAN Power Enable** — HybridGraphics★ / Enable/Disable HybridGraphics
    - _Enable or disable the power of WWAN_
- [select] **DT Hotplug Mode** — HybridGraphics★ / Enable/Disable HybridGraphics
    - _Select DT Hotplug Mode - DxioHotplugEnhanced or DxioHotplugBasic_
- [select] **DT Slot Power Enable** — HybridGraphics★ / Enable/Disable HybridGraphics
    - _Enable or disable the power of DT SLOT_

## 10 Mbps Voll  (2 settings)

- [select] **IPv4** — Bus:Gerät:Funktion★ / Chip-Typ/Revision.
    - _IPv6_
- [select] **iSCSI-Konfiguration** — Bus:Gerät:Funktion★ / Chip-Typ/Revision.

## TCP-Zeitstempel  (6 settings)

- [select] **Ziel als erstes HDD** — Bus:Gerät:Funktion★ / Chip-Typ/Revision.
    - _Ziel erscheint als erstes Festplattenlaufwerk (HDD) im System._
- [select] **IP-Version** — Bus:Gerät:Funktion★ / Chip-Typ/Revision.
    - _IP-Version-Support. Eine Änderung dieses Parameters setzt alle IP-bezogenen Felder zurück._
- [select] **IP-Adresse** — Bus:Gerät:Funktion★ / Chip-Typ/Revision.
    - _Ziel-IP-Adresse konfigurieren._
- [select] **Subnetzmaske** — Bus:Gerät:Funktion★ / Chip-Typ/Revision.
    - _Subnetzmaske konfigurieren._
- [select] **Standard-Gateway** — Bus:Gerät:Funktion★ / Chip-Typ/Revision.
    - _IP-Adresse des Standard-Gateways konfigurieren_
- [select] **Sekundäre DNS** — Bus:Gerät:Funktion★ / Chip-Typ/Revision.
    - _Sekundäre DNS-IP-Adresse konfigurieren._

## This selection will take you to the Device Manager  (1 settings)

- [number] **Select the network device according the MAC address**
    - _Network Device List_

## ￱按下￰PageDown  ￱下一頁￰  (6 settings)

- [select] **+ =￱上移選擇項￰** — =￱移動反白項￰ /  =￱由可選項目中選擇￰ / 0-9 a-f￱為有效輸入￰
    - _- =￱下移選擇項￰_
- [select] **￱請輸入密碼￰**
    - _￱請輸入新密碼￰_
- [select] **￱密碼不相同￰** — Rev. 5.0 / Esc=Exit Menu / F10=Save and Exit / ￱無效的密碼￰!￱請重輸設定密碼￰
    - _￱密碼錯誤￰_
- [select] **NV** — ￱離開並儲存設定￰ / ￱確定￰
    - _!!_
- [select] **Setup Warning** — ￱離開並儲存設定￰★ / ￱確定￰
    - _￱設定通知￰_
- [number] **[￱繼續￰]**

## ブート LUN  (2 settings)

- [select] **ターゲット ブート LUN 番号を設定する (0 ～ 255)。** — セカンダリ デバイスの MAC アドレスを入力する。XX:XX:XX:XX:XX:XX 形式を使用する。★ / セカンダリ デバイス MAC アドレス
    - _セカンダリ デバイス_
- [select] **CHAP ID を設定する (32 文字まで)。** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _CHAP ID を設定する (128 文字まで)。_

## <Enter>=Select Entry  (1 settings)

- [select] **Press 'Y' to save and exit, 'N' to discard and exit.** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='16,28,16,28' ><Label name='title' height='60' align='center' fontsize='40' textcolor='0xFFFFFF' /><VerticalLayout vscrollbar='true' ><Label name='showstring' fontsize='20' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout  name='content' height='30' /></VerticalLayout> / <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,28,160,28' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout height='30'><Label name='oldpasswordtext' fontsize='24' textcolor='0xFFFFFF' textpadding='2,0,2,0' width='400' /><UiEdit name='oldpassword' width='160' fontsize='24' textcolor='0xFF000000' password='true' textpadding='5,0,5,0' /></HorizontalLayout><HorizontalLayout height='30'><Label name='newpasswordtext' fontsize='24' textcolor='0xFFFFFF' textpadding='2,0,2,0' width='400' /><UiEdit name='newpassword' width='160' fontsize='24' textcolor='0xFF000000' password='true' textpadding='5,0,5,0' /></HorizontalLayout><HorizontalLayout height='30'><Label name='confirmpasswordtext' fontsize='24' textcolor='0xFFFFFF' textpadding='2,0,2,0' width='400' /><UiEdit name='confirmpassword' width='160' fontsize='24' textcolor='0xFF000000' password='true' textpadding='5,0,5,0' /></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='cancel' fontsize='24' /></HorizontalLayout></VerticalLayout>★
    - _InsydeH2O Setup Utility_

## Esc=Exit Entry  (5 settings)

- [select] **Yes** — No
    - _Help_
- [select] **Invalid password! Please enter new string for setting password.** — Ok★ / Cancel
    - _Exit Saving Changes_
- [select] **↑↓** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='16,28,16,28' ><Label name='title' height='60' align='center' fontsize='40' textcolor='0xFFFFFF' /><VerticalLayout vscrollbar='true' ><Label name='showstring' fontsize='20' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout  name='content' height='30' /></VerticalLayout>★ / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />
    - _Select Item_
- [select] **F5/F6** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='16,28,16,28' ><Label name='title' height='60' align='center' fontsize='40' textcolor='0xFFFFFF' /><VerticalLayout vscrollbar='true' ><Label name='showstring' fontsize='20' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout  name='content' height='30' /></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Change Values_
- [select] **F9** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='16,28,16,28' ><Label name='title' height='60' align='center' fontsize='40' textcolor='0xFFFFFF' /><VerticalLayout vscrollbar='true' ><Label name='showstring' fontsize='20' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout  name='content' height='30' /></VerticalLayout> / <VerticalLayout name='list' childpadding='10' bkcolor='0xFFFFFFFF' inset='2,2,0,0' vscrollbar='true' />★
    - _Setup Defaults_

## =Move Highlight  (1 settings)

- [toggle] **<Spacebar>Toggle Checkbox**
    - _Enter current password_

## Pg Dn￱キー￰     - ￱ページダウン￰  (6 settings)

- [select] **+ =￱上へ移動￰** — =￱ハイライト移動￰ /  =￱項目選択￰  / 0-9 a-f￱は有効なインプットです￰
    - _- =￱下へ移動￰_
- [select] **￱パスワード入力￰**
    - _￱新しいパスワード入力￰_
- [select] **￱パスワードが同一ではありません￰** — Rev. 5.0 / Esc=Exit Menu / F10=Save and Exit / ￱無効なパスワード￰!￱パスワード設定のために新しい文字列を入力してください。￰
    - _￱パスワードに誤りがあります￰_
- [select] **NV** — ￱変更を保存して終了￰ / ￱オーケー￰
    - _!!_
- [select] **Setup Warning** — ￱変更を保存して終了￰★ / ￱オーケー￰
    - _￱設定注意事項￰_
- [number] **[￱継続￰]**

## F9=Reset à Défauts  (3 settings)

- [select] **N**
    - _Veuillez entrer des caractères suffisants_
- [select] **Des changements ont été sauvegardés**
    - _[continuer]_
- [select] **Setup Warning**
    - _Avis de Configuration_

## Enable/Disable Discrete GPU Display HPD Circuitry  (18 settings)

- [select] **MACO-PWR Timing: MACO_EN assert to PWR_EN deassert** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state.★ / RT3663 VRM PSI0 Workaround
    - _PWROFF-RST Timing (ms)_
- [select] **PWROFF-RST Timing: PWR_EN deassert to PERSTb assert** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state.★ / RT3663 VRM PSI0 Workaround
    - _PWRON-RST Timing  (ms)_
- [select] **Determines the action taken when the system power is off and a PCI Power Management Enable wake up event occurs.** — Enable/Disable Sensor Fusion User Mode Driver★
    - _Sensor Fusion User Mode Driver_
- [select] **UCSI Support** — UCSI tunnel location★ / UCSI tunnel can be put on ECRAM or MMIO space, this option specify which one is selected.
    - _Enable/Disable UCSI (USB Type-C Connector System Software Interface)_
- [select] **Modern Standby + S0i2** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state.★ / RT3663 VRM PSI0 Workaround
    - _Modern Standby + S0i3_
- [select] **Modern Standby + S0i2 + S0i3** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _SATA D3cold Enable_
- [select] **Enable/Disable SATA devies D3-COLD support.** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state.★ / RT3663 VRM PSI0 Workaround
    - _MS Resource_
- [select] **Auto: USB interrupt resource is controlled automatically; Enable: Enable USB current resource for MS; Disable: Disable USB current resource for MS.** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state.★ / RT3663 VRM PSI0 Workaround
    - _Reduce Hardware Support_
- [select] **UCSI tunnel at EC RAM** — S3/Modern Standby Support★ / Switch S3/Modern Standby
    - _UCSI tunnel at MMIO 0xFEEC2000_
- [select] **S3 Enable** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _Modern Standby Enable_
- [select] **Modern Standby Type** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state.★ / RT3663 VRM PSI0 Workaround
    - _Select S0I2 or S0I3 type for Modern Standby._
- [select] **PWRON-RST Timing: PWR_EN assert to PERSTb deassert** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _RST-MACO Timing   (ms)_
- [select] **StallForUnlock** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _StallForUnlock Enable/Disable_
- [select] **HDT BreakPoint for Boot** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _HDT BreakPoint for Boot Enable/Disable_
- [select] **0** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state.★ / RT3663 VRM PSI0 Workaround
    - _VBIOS FW Version_
- [select] **SW BreakPoint for S3** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _SW BreakPoint for S3 Enable/Disable_
- [select] **BLINK LED** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _Enable/Disable BLINK LED to identify S3/S4 state_
- [select] **Enable or disable LAN Power** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _LAN Low Power Mode_

## Página de configuración principal  (5 settings)

- [select] **Desactivar función de memoria compartida de HP** — Deshabilitado / Habilitado★
    - _Desactivar el uso de regiones de memoria reservada para permitir la asignación directa de dispositivo para las máquinas virtuales invitadas._
- [number] **LED intermitentes**
    - _LED intermitentes con una duración de hasta 15 segundos._
- [select] **Wake on LAN (WOL) (LAN de reactivación) previa al inicio del sistema** — Deshabilitado / Habilitado
    - _Configurar Wake on LAN (WOL) (LAN de reactivación) previa al inicio del sistema._
- [select] **Estado del enlace** — Desconectado / Conectado
- [select] **Parámetros de primer destino de iSCSI** — Dirección MAC / Dirección MAC permanente★

## Parámetros generales de iSCSI  (14 settings)

- [select] **Parámetros de TCP/IP a través de DHCP** — Deshabilitado / Habilitado★
    - _Adquirir configuración de TCP/IP a través de DHCP._
- [select] **Configuración automática de IP** — Deshabilitado / Habilitado★
    - _Adquirir configuración de TCP/IP a través de configuración automática con estado o sin estado._
- [select] **Configuración auto. de IP** — Deshabilitado / Habilitado★
    - _Adquirir configuración de TCP/IP a través de configuración automática con estado o sin estado._
- [select] **Parámetros de iSCSI a través de DHCP** — Deshabilitado / Habilitado★
    - _Adquirir parámetros de iSCSI a través de DHCP._
- [select] **Autenticación CHAP** — Deshabilitado★ / Habilitado
    - _Habilitar/Deshabilitar autenticación CHAP._
- [select] **Arranque en destino iSCSI** — Deshabilitado / Habilitado★ / Un solo uso desactivado
    - _Habilitar/Deshabilitar arranque en destino iSCSI tras el inicio de sesión._
- [select] **Arranque en destino** — Deshabilitado / Habilitado★ / Un solo uso desactivado
    - _Habilitar/Deshabilitar arranque en destino iSCSI tras el inicio de sesión._
- [number] **Tiempo de retraso de conexión**
    - _Configurar el tiempo de retraso de conexión en segundos (0..255)._
- [select] **Utilizar marca de hora TCP** — Deshabilitado★ / Habilitado
    - _Habilitar/Deshabilitar marca de hora TCP._
- [select] **Sello de tiempo TCP** — Deshabilitado★ / Habilitado
    - _Habilitar/Deshabilitar marca de hora TCP._
- [select] **Destino como primera HDD** — Deshabilitado★ / Habilitado
    - _Habilitar/Deshabilitar la aparición del destino como primera unidad de disco duro (HDD) en el sistema._
- [number] **Conteo de reintentos con LUN ocupado**
    - _Configurar el número de reintentos en intervalos de 2 segundos cuando el número de unidad lógica (LUN) está ocupado (0..60)._
- [select] **Versión de IP** — IPv4★ / IPv6
    - _Compatibilidad con la versión de IP. Al modificar este parámetro se restablecerán todos los campos relacionados con la IP._
- [select] **Parámetros de primer destino de iSCSI** — Dirección MAC / Dirección MAC permanente★

## Parámetros de iniciador de iSCSI  (1 settings)

- [select] **Parámetros de primer destino de iSCSI** — Dirección MAC / Dirección MAC permanente★

## Parámetros de primer destino de iSCSI  (3 settings)

- [select] **Conectar** — Deshabilitado★ / Habilitado
    - _Habilitar/Deshabilitar establecimiento de destino._
- [number] **Puerto TCP**
    - _Configurar número de puerto TCP de destino (1..65535)._
- [number] **LUN de arranque**
    - _Configurar número LUN de arranque de destino (0..255)._

## Parámetros de segundo destino de iSCSI  (3 settings)

- [select] **Conectar** — Deshabilitado★ / Habilitado
    - _Habilitar/Deshabilitar establecimiento de destino._
- [number] **Puerto TCP**
    - _Configurar número de puerto TCP de destino (1..65535)._
- [number] **LUN de arranque**
    - _Configurar número LUN de arranque de destino (0..255)._

## Menú de configuración MBA  (10 settings)

- [select] **Opción ROM** — Deshabilitado / Habilitado★
    - _Habilitar/Deshabilitar opción ROM de arranque_
- [select] **Protocolo de arranque heredado** — PXE / iSCSI / NADA
    - _Seleccionar protocolo de arranque no UEFI: Entorno de ejecución de arranque previo (PXE)/iSCSI._
- [select] **Tipo de autocarga** — Detección automática★ / BBS / Int 18 h / Int 19 h
    - _Seleccionar tipo de autocarga._
- [select] **Ocultar solicitud de configuración** — Deshabilitado★ / Habilitado
    - _Configurar si se muestra la solicitud de configuración durante la inicialización ROM._
- [select] **Configurar pulsación de tecla** — Ctrl-S★ / Ctrl-B
    - _Configurar pulsaciones de teclas para llamar al menú de configuración._
- [number] **Tiempo de espera de mensaje de banner**
    - _Seleccionar valor para el tiempo de espera. (0 establece de forma predeterminada 4 segundos, 15 es sin retraso, 1-14 es el valor de tiempo de espera en segun..._
- [select] **Velocidad de enlace** — AutoNeg★ / 10 Mbps media / 10 Mbps llena / 100 Mbps media / 100 Mbps llena
    - _Configurar velocidad de enlace._
- [select] **Wake on LAN (WOL) (LAN de reactivación) previa al inicio del sistema** — Deshabilitado / Habilitado
    - _Configurar Wake on LAN (WOL) (LAN de reactivación) previa al inicio del sistema._
- [select] **Modo VLAN** — Deshabilitado★ / Habilitado
    - _Configurar modo LAN virtual._
- [number] **ID de VLAN (1..4094)**
    - _Configurar ID de LAN virtual (1..4094)._

## Dispositivo secundario  (2 settings)

- [select] **Utilizar portal de destino independiente** — Deshabilitado★ / Habilitado
    - _Utilizar portal de destino independiente cuando esté habilitada la E/S de múltiples rutas._
- [select] **Utilizar nombre de destino independiente** — Deshabilitado★ / Habilitado
    - _Utilizar nombre de destino independiente cuando esté habilitada la E/S de múltiples rutas._

## Parámetros de dispositivo secundario iSCSI  (2 settings)

- [select] **Utilizar portal de destino independiente** — Deshabilitado★ / Habilitado
    - _Utilizar portal de destino independiente cuando esté habilitada la E/S de múltiples rutas._
- [select] **Utilizar nombre de destino independiente** — Deshabilitado★ / Habilitado
    - _Utilizar nombre de destino independiente cuando esté habilitada la E/S de múltiples rutas._

## Configuración NIC  (10 settings)

- [select] **Opción ROM** — Deshabilitado / Habilitado
    - _Habilitar/Deshabilitar opción ROM de arranque_
- [select] **Protocolo de arranque heredado** — PXE / iSCSI / Nada
    - _Seleccionar protocolo de arranque no UEFI: Entorno de ejecución de arranque previo (PXE)/iSCSI._
- [select] **Tipo de autocarga** — Detección automática★ / BBS / Int 18 h / Int 19 h
    - _Seleccionar tipo de autocarga._
- [select] **Ocultar solicitud de configuración** — Deshabilitado★ / Habilitado
    - _Configurar si se muestra la solicitud de configuración durante la inicialización ROM._
- [select] **Configurar pulsación de tecla** — Ctrl-S★ / Ctrl-B
    - _Configurar pulsaciones de teclas para llamar al menú de configuración._
- [number] **Tiempo de espera de mensaje de banner**
    - _Seleccionar valor para el tiempo de espera. (0 establece de forma predeterminada 4 segundos, 15 es sin retraso, 1-14 es el valor de tiempo de espera en segun..._
- [select] **Velocidad de enlace** — Negociación auto.★ / 10 Mbps media / 10 Mbps llena / 100 Mbps media / 100 Mbps llena
    - _Configurar velocidad de enlace._
- [select] **Wake on LAN (WOL) (LAN de reactivación)** — Deshabilitado / Habilitado
    - _Configurar Wake on LAN (WOL, LAN de reactivación))_
- [select] **Modo LAN virtual** — Deshabilitado★ / Habilitado
    - _Configurar modo LAN virtual._
- [number] **ID de LAN virtual**
    - _Configurar ID de LAN virtual (1..4094)._

## PCI Bus:Device:Function number of this device.  (3 settings)

- [select] **Energy Efficient Ethernet (EEE)** — Virtual MAC Address
    - _VLAN Mode_
- [select] **VLAN ID (1..4094)** — MAC Address★ / Permanent MAC Address
    - _Virtual LAN ID_
- [select] **Virtual LAN Mode** — MAC Address★ / Permanent MAC Address
    - _Configure virtual LAN mode._

## Confirm New Password  (2 settings)

- [select] **Enter old password incorrect !** — textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★ / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFFFFFFFF' bkcolor='0' bkcolor2='0' bkcolor3='0' bkimagestyle='' bkimage='@ButtonNormal' scale9grid='12,12,12,12' 
    - _New password confirm fail !_
- [select] **Press Esc for boot options** — textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★ / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFFFFFFFF' bkcolor='0' bkcolor2='0' bkcolor3='0' bkimagestyle='' bkimage='@ButtonNormal' scale9grid='12,12,12,12' 
    - _Esc is pressed. Go to boot options._

## Boot Next Value  (33 settings)

- [select] **Next boot use this boot option** — Load Option Reconnect / Add .EFI Driver as Driver Option★
    - _Input the description_
- [number] **Commit Changes and Exit** — Set Console Output Mode / Set COM Attributes / Set COM Terminal Type★
    - _Discard Changes and Exit_
- [number] **Set Console Output Mode**
    - _Set COM Attributes_
- [number] **Set COM Terminal Type**
    - _Set COM Flow Control_
- [number] **Set COM Baud Rate**
    - _Set COM Data Bits_
- [number] **Set COM Parity**
    - _Set COM Stop Bits_
- [select] **115200** — Enable console device as ConIn / Load Option Reconnect / Add .EFI Driver as Driver Option★
    - _57600_
- [number] **38400**
    - _19200_
- [number] **9600**
    - _7200_
- [number] **4800**
    - _3600_
- [select] **2400** — Enable console device as ConIn / Load Option Reconnect / Add .EFI Driver as Driver Option★
    - _2000_
- [number] **1800**
    - _1200_
- [number] **600**
    - _300_
- [number] **150**
    - _134_
- [select] **110** — Enable console device as ConIn / Load Option Reconnect / Add .EFI Driver as Driver Option★
    - _75_
- [number] **50**
    - _5_
- [number] **6**
    - _7_
- [number] **8**
    - _None_
- [select] **Even** — Enable console device as ConIn / Load Option Reconnect / Add .EFI Driver as Driver Option★
    - _Odd_
- [number] **Mark**
    - _Space_
- [number] **One**
    - _One And A Half_
- [number] **Two**
    - _PC_ANSI_
- [select] **VT_100** — Enable console device as ConIn / Load Option Reconnect / Add .EFI Driver as Driver Option★
    - _VT_100_PLUS_
- [number] **VT_UTF8**
    - _Reset System_
- [number] **Go Back To Main Page**
    - _Boot From File_
- [number] **Boot system from a file or device**
    - _Input Optional Data_
- [select] **Change the order** — Enable console device as ConIn / Load Option Reconnect / Add .EFI Driver as Driver Option★
    - _Disabled_
- [number] **File Explorer**
    - _Hardware_
- [number] **None**
    - _Press Esc for boot options_
- [number] **Esc is pressed. Go to boot options.**
- [select] **1200** — 300★ / 134 / 150
    - _600_
- [toggle] **Modify system boot options** — Modify system boot options★
- [select] **Set COM Flow Control** — Console Output Device Select / Set Legacy BEV Drive Order★
    - _Set COM Baud Rate_

## CHAP Secret  (6 settings)

- [select] **CHAP Secret** — MAC Address★ / Permanent MAC Address
    - _Configure CHAP Secret (12 to 16 characters in length)._
- [select] **Secondary Device** — MAC Address★
- [select] **Connect** — MAC Address / Permanent MAC Address★
    - _Enable/Disable target establishment._
- [select] **TCP Port** — MAC Address★ / Configure target TCP port number (1..65535). / TCP Port
    - _Configure target TCP port number (1..65535)._
- [number] **Configure target boot LUN number (0..255).**
    - _Chip Type/Revision._
- [select] **Boot LUN** — MAC Address / Permanent MAC Address★
    - _Configure target boot LUN number (0..255)._

## I Accept  (42 settings)

- [select] **Overclock** — Auto★ / Enabled
    - _Memory Overclock Settings_
- [select] **Memory Clock Speed** — Auto★ / 667MHz / 800MHz / 933MHz / 1067MHz / 1200MHz / 1333MHz / 1367MHz / 1400MHz / 1433MHz / 1467MHz / 1500MHz / 1533MHz / 1567MHz / 1600MHz / 1633MHz / 1667MHz / 1700MHz / 1733MHz / 1767MHz / 1800MHz / 1833MHz / 1867MHz / 1900MHz / 1933MHz / 1967MHz / 2000MHz / 333MHz / 400MHz / 533MHz / 1050MHz / 1066MHz / 2033MHz / 2067MHz / 2100MHz
    - _Set the memory clock frequency._
- [select] **Tcl** — 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / 0Ch Clk / 0Dh Clk / 0Eh Clk / 0Fh Clk / 10h Clk / 11h Clk / 12h Clk / 13h Clk / Auto★ / 14h Clk / 15h Clk / 16h Clk / 17h Clk / 18h Clk / 19h Clk / 1Ah Clk / 1Bh Clk / 1Ch Clk / 1Dh Clk / 1Eh Clk / 1Fh Clk / 20h Clk / 21h Clk
    - _Sets the tCL time._
- [select] **Trcdrd** — 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / 0Ch Clk / 0Dh Clk / 0Eh Clk / 0Fh Clk / 10h Clk / 14h Clk / 15h Clk / 16h Clk / 17h Clk / 18h Clk / 19h Clk / 1Ah Clk / 11h Clk / 12h Clk / 13h Clk / Auto★ / 1Bh Clk
    - _This sets the RAS# Active to CAS# read/write delay._
- [select] **Trcdwr** — Auto★ / 8 Clk / 9 Clk / 0xA Clk / 0xB Clk / 0xC Clk / 0xD Clk / 0xE Clk / 0xF Clk / 10h Clk / 11h Clk / 12h Clk / 13h Clk / 14h Clk / 15h Clk / 16h Clk / 17h Clk / 18h Clk / 19h Clk / 1Ah Clk / 1Bh Clk
    - _This sets the RAS# Active to CAS# read/write delay._
- [select] **Trp** — 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / 0Ch Clk / 0Dh Clk / 0Eh Clk / 0Fh Clk / 10h Clk / 11h Clk / 12h Clk / 13h Clk / Auto★ / 14h Clk / 15h Clk / 16h Clk / 17h Clk / 18h Clk / 19h Clk / 1Ah Clk / 1Bh Clk
    - _Specify the row precharge time._
- [select] **Tras** — 15h Clk / 16h Clk / 17h Clk / 18h Clk / 19h Clk / 1Ah Clk / 1Bh Clk / 1Ch Clk / 1Dh Clk / 1Eh Clk / 1Fh Clk / 20h Clk / 21h Clk / 22h Clk / 23h Clk / 24h Clk / 25h Clk / 26h Clk / 27h Clk / 28h Clk / 29h Clk / 2Ah Clk / Auto★ / 2Bh Clk / 2Ch Clk / 2Dh Clk / 2Eh Clk / 2Fh Clk / 30h Clk / 31h Clk / 32h Clk / 33h Clk / 34h Clk / 35h Clk / 36h Clk / 37h Clk / 38h Clk / 39h Clk / 3Ah Clk
    - _Specify the min RAS# active time._
- [select] **Trc Ctrl** — Auto★ / Manual
    - _Specify Trc_
- [number] **Trc**
    - _Active to Active/Refresh Delay Time. Valid values 87h-1Dh._
- [select] **TrrdS** — Auto★ / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / 0Ch Clk
    - _Activate to Activate Delay Time, different bank group (tRRD_S)_
- [select] **TrrdL** — Auto★ / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / 0Ch Clk
    - _Activate to Activate Delay Time, same bank group (tRRD_L)_
- [select] **Tfaw Ctrl** — Auto★ / Manual
    - _Specify Tfaw_
- [number] **Tfaw**
    - _Four Activate Window Time. Valid values 36h-6h._
- [select] **TwtrS** — Auto★ / 2 Clk / 3 Clk / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / 0Ch Clk / 0Dh Clk / 0Eh Clk
    - _Minimum Write to Read Time, different bank group_
- [select] **TwtrL** — Auto★ / 2 Clk / 3 Clk / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / 0Ch Clk / 0Dh Clk / 0Eh Clk
    - _Minimum Write to Read Time, same bank group_
- [select] **Twr Ctrl** — Auto★ / Manual
    - _Specify Twr_
- [number] **Twr**
    - _Minimum Write Recovery Time. Valid value 51h-Ah_
- [select] **Trcpage Ctrl** — Auto★ / Manual
    - _Specify Trcpage_
- [number] **Trcpage**
    - _SDRAM Optional Features (tMAW, MAC). Valid value 3FFh - 0h_
- [select] **TrdrdScL Ctrl** — Auto★ / Manual
    - _Specify TrdrdScL_
- [number] **TrdrdScL**
    - _CAS to CAS Delay Time, same bank group. Valid values Fh-1h_
- [select] **TwrwrScL Ctrl** — Auto★ / Manual
    - _Specify TwrwrScL_
- [number] **TwrwrScL**
    - _CAS to CAS Delay Time, same bank group. Valid values 3Fh-1h_
- [select] **Trfc Ctrl** — Auto★ / Manual
    - _Specify Trfc_
- [number] **Trfc**
    - _Refresh Recovery Delay Time (tRFC1). Valid values 3DEh-3Ch_
- [select] **Trfc2 Ctrl** — Auto★ / Manual
    - _Specify Trfc2_
- [number] **Trfc2**
    - _Refresh Recovery Delay Time (tRFC2).  Valid values 3DEh-3Ch_
- [select] **Trfc4 Ctrl** — Auto★ / Manual
    - _Specify Trfc4_
- [number] **Trfc4**
    - _Refresh Recovery Delay Time (tRFC4). Valid values 3DEh-3Ch_
- [number] **Fail_CNT**
    - _The number of training failure/retries required before boot from recovery mode_
- [select] **ProcODT** — Auto★ / High Impedance / 480 ohm / 240 ohm / 160 ohm / 120 ohm / 96 ohm / 80 ohm / 68.6 ohm / 60 ohm / 53.3 ohm / 48 ohm / 43.6 ohm / 40 ohm / 36.9 ohm / 34.3 ohm / 32 ohm / 30 ohm / 28.2 ohm
    - _Specifies the Processor ODT_
- [select] **Tcwl** — Auto★ / 9 Clk / 0Ah Clk / 0Bh Clk / 0Ch Clk / 0Eh Clk / 10h Clk / 12h Clk / 14h Clk
    - _No help string_
- [select] **Trtp** — 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / Auto★ / 0Ch Clk / 0Dh Clk / 5 Clk / 6 Clk / 7 Clk / 0Eh Clk
    - _Specifies the read CAS# to precharge time._
- [select] **Tcke** — Auto★ / 1 Clk / 2 Clk / 3 Clk / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / 0Ch Clk / 0Dh Clk / 0Eh Clk / 0Fh Clk / 10h Clk / 11h Clk / 12h Clk / 13h Clk / 14h Clk / 15h Clk / 16h Clk / 17h Clk / 18h Clk / 19h Clk / 1Ah Clk / 1Bh Clk / 1Ch Clk / 1Dh Clk / 1Eh Clk / 1Fh Clk
    - _Specifies the CKE minimum high and low pulse width in memory clock cycles._
- [select] **TrdrdSc** — 1 Clk / 2 Clk / 3 Clk / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / Auto★
    - _write to write timing same DIMM same chip select._
- [select] **TrdrdSd** — 2 Clk / 3 Clk / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / Auto★ / 1 Clk / 0Ch Clk / 0Dh Clk / 0Eh Clk / 0Fh Clk
    - _write to write timing same DIMM same chip select._
- [select] **TrdrdDd** — 2 Clk / 3 Clk / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / Auto★ / 1 Clk / 0Ch Clk / 0Dh Clk / 0Eh Clk / 0Fh Clk
    - _write to write timing same DIMM same chip select._
- [select] **TwrwrSc** — 1 Clk / 2 Clk / 3 Clk / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / Auto★ / 0Ch Clk / 0Dh Clk / 0Eh Clk / 0Fh Clk
    - _write to write timing same DIMM same chip select._
- [select] **TwrwrSd** — 2 Clk / 3 Clk / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / Auto★ / 1 Clk / 0Ch Clk / 0Dh Clk / 0Eh Clk / 0Fh Clk
    - _write to write timing same DIMM same chip select._
- [select] **TwrwrDd** — 2 Clk / 3 Clk / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / Auto★ / 1 Clk / 0Ch Clk / 0Dh Clk / 0Eh Clk / 0Fh Clk
    - _write to write timing same DIMM same chip select._
- [select] **Trdwr** — 2 Clk / 3 Clk / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / 0Ch Clk / 0Dh Clk / 0Eh Clk / 0Fh Clk / 10h Clk / 11h Clk / 12h Clk / 13h Clk / 14h Clk / 15h Clk / 16h Clk / 17h Clk / 18h Clk / 19h Clk / 1Ah Clk / 1Bh Clk / Auto★ / 1 Clk / 1Ch Clk / 1Dh Clk / 1Eh Clk / 1Fh Clk
    - _This sets the tWRTTO time._
- [select] **Twrrd** — 1 Clk / 2 Clk / 3 Clk / 4 Clk / 5 Clk / 6 Clk / 7 Clk / 8 Clk / 9 Clk / 0Ah Clk / 0Bh Clk / Auto★ / 0Ch / 0Dh / 0Eh / 0Fh
    - _Specify the write to read delay when accessing different DIMMs._

## CHAP-Kennwort  (6 settings)

- [select] **CHAP-Kennwort** — MAC-Adresse★ / Permanente MAC-Adresse
    - _CHAP-Geheimnis konfigurieren (12 – 16 Zeichen lang)_
- [select] **Sekundäres Gerät** — MAC-Adresse★
- [select] **Verbinden** — MAC-Adresse / Permanente MAC-Adresse★
    - _Zielherstellung aktivieren/deaktivieren._
- [select] **TCP-Port** — MAC-Adresse★ / Ziel-TCP.Port-Nummer (1..65535) konfigurieren. / TCP-Port
    - _Ziel-TCP.Port-Nummer (1..65535) konfigurieren._
- [number] **Ziel-Boot-LUN-Nummer (0..255) konfigurieren.**
    - _Chip-Typ/Revision._
- [select] **Boot-LUN** — MAC-Adresse / Permanente MAC-Adresse★
    - _Ziel-Boot-LUN-Nummer (0..255) konfigurieren._

## 固定 MAC アドレス  (7 settings)

- [select] **PCIバス：デバイス：機能。** — PCI アドレス / バス：デバイス：機能★
    - _リンク ステータス_
- [select] **リンク ステータス** — 切断完了 / LED を点滅させる / バス：デバイス：機能★
    - _接続完了_
- [select] **LED を最大 15 秒点滅させる。** — 旧式ブート プロトコル / バス：デバイス：機能★
    - _旧式ブート プロトコル_
- [select] **UEFI 以外のブート プロトコルを選択：Preboot Execution Environment (PXE)/iSCSI。** — 旧式ブート プロトコル / iSCSI / バス：デバイス：機能★
    - _PXE_
- [select] **ナシ** — ブート ストラップのタイプ★ / ブート ストラップのタイプを選択する。
- [select] **リンク速度を設定する。** — 旧式ブート プロトコル / iSCSI / バス：デバイス：機能★
    - _プリブート Wake On LAN_
- [select] **プリブート Wake on LAN (WOL) を設定する。** — 旧式ブート プロトコル / iSCSI / バス：デバイス：機能★
    - _Wake On LAN_

## デフォルト ゲートウェイの IP アドレスを設定する。  (2 settings)

- [select] **プライマリ DNS** — セカンダリ DNS / セダンダリ DNS の IP アドレスを設定する。 / iSCSI 名 / バス：デバイス：機能★
- [select] **iSCSI 名を設定する。** — LED を点滅させる / バス：デバイス：機能★
    - _iSCSI 名_

## MAC アドレス  (11 settings)

- [select] **iSCSI 名を設定する。** — 旧式ブート プロトコル / iSCSI 名を設定する。 / CHAP ID / CHAP ID を設定する (32 文字まで)。 / CHAP ID を設定する (128 文字まで)。 / バス：デバイス：機能★
    - _iSCSI 名_
- [select] **CHAP ID** — 旧式ブート プロトコル / iSCSI / バス：デバイス：機能★
    - _CHAP ID を設定する (32 文字まで)。_
- [select] **CHAP ID を設定する (128 文字まで)。** — CHAP ID / CHAP ID を設定する (32 文字まで)。 / バス：デバイス：機能★ / 旧式ブート プロトコル / iSCSI
    - _CHAP ID_
- [select] **CHAP 秘密情報** — 旧式ブート プロトコル / iSCSI / バス：デバイス：機能★
    - _CHAP 秘密情報を設定する (12 ～ 16 文字)。_
- [select] **CHAP 秘密情報を設定する (12 ～ 16 文字)。** — CHAP 秘密情報 / CHAP 秘密情報を設定する (12 ～ 16 文字)。 / バス：デバイス：機能★
    - _CHAP 秘密情報_
- [select] **接続** — 旧式ブート プロトコル / iSCSI / バス：デバイス：機能★ / TCP ポート / ターゲット TCP ポート番号を設定する (1 ～ 65535)。
    - _ターゲットの確立をイネーブル/ディスエーブルする。_
- [select] **ブート LUN** — ブート LUN / ターゲット ブート LUN 番号を設定する (0 ～ 255)。 / セカンダリ デバイス / セカンダリ デバイスの MAC アドレスを入力する。XX:XX:XX:XX:XX:XX 形式を使用する。 / バス：デバイス：機能★
    - _ターゲット ブート LUN 番号を設定する (0 ～ 255)。_
- [select] **セカンダリ デバイス MAC アドレス** — 旧式ブート プロトコル / iSCSI / バス：デバイス：機能★
    - _独立したターゲット ポータルを使用_
- [select] **独立したターゲット ポータルを使用** — 旧式ブート プロトコル / iSCSI / バス：デバイス：機能★
    - _multipath I/O がイネーブルな場合、独立したターゲット ポータルを使用する。_
- [select] **独立したターゲット名を使用** — 旧式ブート プロトコル / iSCSI / バス：デバイス：機能★
- [select] **multipath I/O がイネーブルな場合、独立したターゲット名を使用する。** — 旧式ブート プロトコル / iSCSI / バス：デバイス：機能★
    - _ファミリ ファームウェア バージョン_

## CCM  (3 settings)

- [select] **Target Relative Port Number** — Bus:Device:Function★ / ISCSISecondTargetParameters_BootLUN / AIM Spec Version / VPD-V0. It stores the IBM release string / Software Bundle / Firmware Bundle / Software Bundle Version / 0.0.0a / FlexSystem Mezzanine Connector / SFP+
- [select] **RJ45** — Disabled / Software Bundle / Software Bundle Version / Switch Independent mode / FlexSystem Mezzanine Connector / Bus:Device:Function★
    - _Onboard_
- [select] **Ethernet** — iSCSI / VPD-V0. It stores the IBM release string / Software Bundle / Firmware Bundle / Software Bundle Version / 0.0.0a / FlexSystem Mezzanine Connector / SFP+ / Bus:Device:Function★
    - _Fibre Channel_

## Push PageDown  - Next Page  (6 settings)

- [select] **+ =Move Selection Up** — =Move Highlight /  =Select From Choices / 0-9 a-f are valid inputs
    - _- =Move Selection Down_
- [select] **Enter current password**
    - _Enter New Password_
- [select] **Password do not match** — InsydeH2O Setup Utility (Manufacture)★ / Rev. 5.0 / Esc=Exit Menu / F10=Save and Exit / Invalid password! Please enter new string for setting password.
    - _Invalid password_
- [select] **NV** — Exit Saving Changes / Ok
    - _!!_
- [select] **Setup Warning** — Exit Saving Changes★ / Ok
    - _Setup Notice_
- [number] **[continue]**
    - _Changes have been saved after press _

## Bus:Dispositivo:Función  (1 settings)

- [select] **Soporte de descarga iSCSI** — Dirección MAC / Dirección MAC permanente★
    - _Compatibilidad con arranque iSCSI_

## Administración FW  (1 settings)

- [select] **Parámetros de primer destino de iSCSI** — Dirección MAC / Dirección MAC permanente★

## Configurar parámetros generales de arranque iSCSI.  (1 settings)

- [select] **Parámetros de primer destino de iSCSI** — Dirección MAC / Dirección MAC permanente★

## Configurar parámetros de iniciador de iSCSI.  (1 settings)

- [select] **Parámetros de primer destino de iSCSI** — Dirección MAC / Dirección MAC permanente★

## PCI Bus:Dispositivo:Número de función de este dispositivo.  (2 settings)

- [select] **ID de VLAN (1..4094)** — Dirección MAC★ / Dirección MAC permanente
    - _ID de LAN virtual_
- [select] **Modo LAN virtual** — Dirección MAC★ / Dirección MAC permanente
    - _Configurar modo LAN virtual._

## Desconectado  (6 settings)

- [select] **SMASH** — Dirección MAC
    - _CCM_
- [select] **IPv4** — IPv6 / Menú de configuración MBA★
    - _Menú de configuración de arranque iSCSI_
- [select] **100 Mbps llena** — Habilitado★ / Un solo uso desactivado
    - _Deshabilitado_
- [select] **Configurar parámetros de arranque iSCSI.** — Dirección MAC★ / Dirección MAC permanente
    - _Configuración iSCSI_
- [select] **Configuración iSCSI** — Dirección MAC / Dirección MAC permanente★
    - _Menú de imagen de firmware_
- [select] **Menú de imagen de firmware** — Dirección MAC / Dirección MAC permanente★
    - _Información de imagen del firmware._

## LED intermitentes con una duración de hasta 15 segundos.  (2 settings)

- [select] **Configurar parámetros de dispositivo secundario.** — Dirección MAC / Dirección MAC permanente★
    - _Parámetros de dispositivo secundario iSCSI_
- [select] **Parámetros de dispositivo secundario iSCSI** — Opción ROM★
    - _Configurar parámetros de dispositivo secundario._

## ￱文字数が足りません￰  (21 settings)

- [select] **Setup Warning** — ￱変更を保存しました￰
    - _￱設定注意事項￰_
- [number] **[￱継続￰]** — ￱変更が保存されません。変更を保存して終了しますか?￰ / ￱グエスチョンバリューとオプションバリューは不一致です!￰ / Changes have not saved. Save Changes or not?★
- [number] **￱変更が保存されません。変更を保存して終了しますか?￰**
    - _￱グエスチョンバリューとオプションバリューは不一致です!￰_
- [number] **Changes have not saved. Save Changes or not?**
    - _Press 'Y' to save and exit, 'N' to discard and exit._
- [number] **InsydeH2O ￱セットアップユーティリティ￰**
- [number] **Rev. 5.0**
    - _Esc=Exit Menu_
- [select] **F10=Save and Exit** — + =￱上へ移動￰ / ￱変更を保存しました￰
    - _￱無効なパスワード￰!￱パスワード設定のために新しい文字列を入力してください。￰_
- [number] **￱変更を保存して終了￰**
    - _￱オーケー￰_
- [number] **￱取消￰**
    - _￱はい￰_
- [number] **￱いいえ￰** — + =￱上へ移動￰ / ￱変更を保存しました￰
    - _[￱一般ヘルプ￰]_
- [number] **Pg Up￱キー￰     - ￱ページアップ￰**
    - _Pg Dn￱キー￰     - ￱ページダウン￰_
- [number] **F1**
    - _￱ヘルプ￰_
- [number] **↑↓**
    - _￱アイテム選択￰_
- [select] **F5/F6** — + =￱上へ移動￰ / ￱変更を保存しました￰
    - _￱数値変更￰_
- [number] **F9**
    - _￱デフォルト設定￰_
- [number] **Esc**
    - _￱終了￰_
- [number] **←→**
    - _￱メニュー選択￰_
- [select] **Enter** — + =￱上へ移動￰ / ￱変更を保存しました￰
    - _￱選択￰ ► ￱サブメニューを￰_
- [number] **F10**
    - _￱保存￰&￱終了￰_
- [select] **Pg Dn￱キー￰     - ￱ページダウン￰** — ￱ヘルプ￰★ / ￱アイテム選択￰ / ↑↓
    - _F1_
- [select] **Press 'Y' to save and exit, 'N' to discard and exit.** — ￱＜スペース＞￰ =￱選択／解除￰ / 0-9 a-f￱は有効なインプットです￰★
    - _InsydeH2O ￱セットアップユーティリティ￰_

## 10 Mbps llena  (2 settings)

- [select] **IPv4** — Bus:Dispositivo:Función★ / Revisión/tipo de chip.
    - _IPv6_
- [select] **Configuración iSCSI** — Bus:Dispositivo:Función★ / Revisión/tipo de chip.

## Enroll PK  (1 settings)

- [toggle] **KEK Signature List:**

## DB Options  (2 settings)

- [select] **SHA1** — YES★ / User Customized Security
    - _SHA256_
- [select] **[Error] Invalid GUID string. GUID string should be in 12345678-1234-1234-1234-1234567890ab format.** — YES★ / User Customized Security
    - _Input Owner_GUID in 12345678-1234-1234-1234-1234567890ab format._

## DHCP Vendor ID  (4 settings)

- [select] **IP Address** — ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$ / ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Configure initiator IP address._
- [select] **Configure iSCSI name.** — iSCSI Name★ / Configure iSCSI name. / CHAP ID
    - _CHAP ID_
- [select] **IP-Adresse** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Initiator-IP-Adresse konfigurieren_
- [select] **iSCSI-Name konfigurieren.** — iSCSI-Name★ / iSCSI-Name konfigurieren. / CHAP-ID
    - _CHAP-ID_

## 1567MHz  (7 settings)

- [number] **Sets the tCL time.**
- [select] **24h Clk** — Pstate1 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID★
    - _25h Clk_
- [number] **Disable**
    - _Core Performance Boost_
- [select] **Legal Disclaimer** — Pstate1 FID / Legal Disclaimer
    - _Operating your AMD processor outside of specification or in excess of factory settings, including but not limited to overclocking, may damage or shorten the ..._
- [select] **Enables or disables the streaming stores functionality** — Pstate1 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Enable IBS_
- [select] **0 - L2 TLB ways [11:8] are fully associative.  1 - =L2 TLB ways [11:8] are 4K-only.** — Enable / Enable/disable PFEH, cloak individual banks, and mask deferred error interrupts from each bank.
    - _Platform First Error Handling_
- [select] **1900MHz** — DF Common Options / UMC Common Options★
    - _1933MHz_

## 1667MHz  (11 settings)

- [select] **Sets the tCL time.** — Pstate1 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID★
- [select] **Specifies the core frequency multiplier. COF = 200MHz * FID / DID** — Pstate1 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID★ / Pstate1 DID
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [select] **Pstate4 DID** — Pstate1 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID★
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [select] **Pstate4 VID** — Pstate1 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID★
    - _Specifies the core voltage._
- [select] **Custom Pstate5** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
- [select] **Pstate5 FID** — Pstate1 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID★ / Pstate1 DID
    - _Pstate5 DID_
- [number] **Specifies the core voltage.** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Custom Pstate6_
- [select] **Pstate6 FID** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [select] **Pstate6 DID** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [number] **Pstate6 VID**
    - _Specifies the core voltage._
- [select] **Custom Pstate7** — Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah).★ / Pstate1 VID

## 1800MHz  (1 settings)

- [select] **Sets the tCL time.**

## 1933MHz  (4 settings)

- [select] **System probe filter** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Controls whether or not the probe filter is enabled. Has no effect on parts where the probe filter is fuse disabled._
- [number] **None**
    - _Channel_
- [number] **Memory interleaving size**
    - _Controls the memory interleaving size. The valid values are AUTO, 256 bytes, 512 bytes, 1 Kbytes or 2Kbytes. This determines the starting address of the inte..._
- [select] **Sets the tCL time.**

## 400MHz  (4 settings)

- [select] **Memory interleaving** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Controls fabric level memory interleaving (AUTO, none, channel, die, socket). Note that channel, die, and socket has requirements on memory populations and i..._
- [number] **Die**
    - _Socket_
- [number] **256 Bytes**
    - _512 Bytes_
- [select] **Sets the tCL time.**

## Custom Pstate2  (10 settings)

- [select] **8 Clk** — Pstate1 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID★
    - _0Ah Clk_
- [select] **Disable CPB** — Controls IO based C-state generation and DF C-states. / Enabled / OC Mode
    - _Global C-state Control_
- [select] **Normal Operation** — 0Bh Clk★ / 0Ch Clk / 0Dh Clk / 0Eh Clk
    - _Customized_
- [select] **0Fh Clk** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _11h Clk_
- [select] **12h Clk** — 15h Clk★ / 16h Clk
    - _14h Clk_
- [number] **17h Clk**
    - _19h Clk_
- [select] **Custom Pstates / Throttling** — Voltage (uV)★ / Voltage in uV (1V = 1000 * 1000 uV) / Pstate0 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID / Pstate0 DID
    - _Streaming Stores Control_
- [select] **Enables or disables the streaming stores functionality** — Pstate1 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Enable IBS_
- [select] **Accept** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
- [number] **Custom**
    - _Current core frequency in MHz_

## 1066MHz  (2 settings)

- [select] **Controls whether or not the address bits are hashed during channel interleave mode. This field should not be used unless the interleaving is set to channel and the interleaving size is 256 or 512 bytes.** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Enable / disable DF C-states (DF::CstateControl[DfCstateDisable])_
- [select] **xGMI DLWM control** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Freeze DF module queues on error_

## 2100MHz  (2 settings)

- [select] **DF C-state control** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Enable / disable DF C-states (DF::CstateControl[DfCstateDisable])_
- [select] **Controls xGMI dynamic link width management feature.** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Freeze DF module queues on error_

## Specifies the core frequency multiplier. COF = 200MHz * FID / DID  (10 settings)

- [select] **9 Clk** — Pstate1 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _0Ah Clk_
- [select] **Disabled** — Controls IO based C-state generation and DF C-states. / Enabled / No help string
    - _Global C-state Control_
- [select] **OC1** — 0Bh Clk★ / 0Ch Clk / 0Dh Clk / 0Eh Clk
    - _Customized_
- [select] **10h Clk** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _11h Clk_
- [select] **13h Clk** — 15h Clk★ / 16h Clk
    - _14h Clk_
- [number] **18h Clk**
    - _19h Clk_
- [select] **Core/Thread Enablement** — Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah).★ / Pstate0 VID / Specifies the core voltage. / Custom Pstate1
    - _Streaming Stores Control_
- [select] **When IBS is enabled, SpecLockMap and Stack Engine are disabled.** — Pstate1 FID / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _WARNING - DAMAGE CAUSED BY USE OF YOUR AMD PROCESSOR OUTSIDE OF SPECIFICATION OR IN EXCESS OF FACTORY SETTINGS ARE NOT COVERED UNDER YOUR AMD PRODUCT WARRANT..._
- [select] **Custom Pstate0** — Pstate1 FID★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
- [number] **Frequency (MHz)**
    - _Current core frequency in MHz_

## Off  (1 settings)

- [number] **<VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,10,160,10' ><VerticalLayout height='40' ><Label name='title' fontsize='24' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout childpadding='0'><VerticalLayout width='160' childpadding='4'><Button name='hour_up' width='160' height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='hour' text='1' fontsize='38' align='center' readonly='true' /><Button name='hour_down' width='160' height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='minute_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='minute' fontsize='38' align='center' readonly='true'/><Button name='minute_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout><Label text=':' textcolor='0xFFFFFFFF' fontsize='90' width='40' align='center'><VerticalLayout width='160' childpadding='4'><Button name='second_up' width='160'  height='38' normalimage='@TimeDate1UpNormal' hotimage='@TimeDate1UpNormal' pushimage='@TimeDate1UpPush' /><UiEdit name='second' fontsize='38' align='center' readonly='true'/><Button name='second_down' width='160'  height='38' normalimage='@TimeDate1DownNormal' hotimage='@TimeDate1DownNormal' pushimage='@TimeDate1DownPush' /></VerticalLayout></HorizontalLayout><HorizontalLayout height='30'><Control /><Button name='ok' text='ok'    fontsize='24' /><Button name='cancel' text='canel' fontsize='24' /></HorizontalLayout></VerticalLayout>**
    - _<VerticalLayout name='background' bkcolor='0xFF000000'><Control /><HorizontalLayout height='530' ><Control /><CellLayout name='menuoptionlist' width='710' in..._

## <VerticalLayout name='background' bkcolor='0xFF004D60' inset='160,28,160,28' ><VerticalLayout ><Label name='showstring' fontsize='24' textcolor='0xFFFFFF' /><UiEdit name='input' width='160' fontsize='24' textcolor='0xFF000000' password='true' textpadding='5,0,5,0' /></VerticalLayout><HorizontalLayout  name='content' height='30' /></VerticalLayout>  (8 settings)

- [select] **<VerticalLayout bkcolor='0xFFFFFFFF'><HorizontalLayout inset='0,2,0,2' ><Container name='setupmenu_panel' inset='0,55,0,0' width='300' bkcolor='0xFFF4F4F4' ><VerticalLayout name ='setupmenulist' /></Container><VerticalLayout inset='0,0,0,0' ><Label height='55' name='sub_title' fontsize='40' height='55' /><HorizontalLayout><VerticalLayout name ='menuoptionlist' vscrollbar='true' inset2='10' childpadding='5' /><VerticalLayout width='40' inset='4,0,4,0' name='bootorder' ><Control /><Button name='up'   width='32' height='32' normalimage='@BootOrderUpNormal' hotimage='@BootOrderUpFocus' pushimage='@BootOrderUpPush' /><Button name='down' width='32' height='32' normalimage='@BootOrderUpNormal' hotimage='@BootOrderUpFocus' pushimage='@BootOrderUpPush' /><Control /></VerticalLayout></HorizontalLayout></VerticalLayout></HorizontalLayout><HorizontalLayout height='50' ><Control /><Button name='exit' text='Exit' bkcolor='0xFF123456' align='center' width='70' height='30' /></HorizontalLayout></VerticalLayout>** — textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★ / textcolor='0x00FFFFFF' gradient_vertical='false' textpadding='5,1,1,5' borderround='0,0' fontsize='23' bordercolor='0x80888888' / textcolor='0x00FFFFFF' gradient_vertical='false' textpadding='5,1,1,5' borderround='0,0' fontsize='23' bordercolor='0x80888888' bkcolor3='0' align='bottom'
    - _textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFFFFFFFF' bkcolor='0' bkcolor2='0' bkcolor3='0' bkimagestyle='' bkimage='@ButtonNormal' scale9g..._
- [select] **F9=Reset to Defaults** — textcolor='0x00FFFFFF' gradient_vertical='false' textpadding='5,1,1,5' borderround='0,0' fontsize='23' bordercolor='0x80888888' bkcolor3='0' align='bottom' / textcolor='0x00FFFFFF' gradient_vertical='false' textpadding='5,1,1,5' borderround='0,0' fontsize='23' bordercolor='0x80888888' / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _F10=Save_
- [select] **<Enter>=Select Entry** — Esc=Exit Entry / Esc=Discard Changes / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _<Enter>=Complete Entry_
- [select] **Failed to Save** — + =Move Selection Up / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _+/- =Adjust Value_
- [select] **- =Move Selection Down** — + =Move Selection Up /  =Select From Choices / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _=Move Highlight_
- [select] **0123456789 are valid inputs** — <Spacebar>Toggle Checkbox★ / Enter current password / Enter New Password
    - _0-9 a-f are valid inputs_
- [select] **Invalid password** — + =Move Selection Up /  =Select From Choices / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _Re-enter Password_
- [select] **Please type in your data** — + =Move Selection Up /  =Select From Choices / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _NV_

## Please enter enough characters  (33 settings)

- [select] **Setup Warning** — Changes have been saved. / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _Setup Notice_
- [number] **[continue]** — Changes have not saved. Save Changes and exit? / Question value mismatch with Option value! / Changes have not saved. Save Changes or not?★
    - _Changes have been saved after press _
- [number] **Changes have not saved. Save Changes and exit?**
    - _Question value mismatch with Option value!_
- [number] **Changes have not saved. Save Changes or not?**
    - _Press 'Y' to save and exit, 'N' to discard and exit._
- [number] **InsydeH2O Setup Utility**
    - _InsydeH2O Setup Utility (Manufacture)_
- [number] **Rev. 5.0**
    - _Esc=Exit Menu_
- [select] **F10=Save and Exit** — + =Move Selection Up / Changes have been saved. / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _Invalid password! Please enter new string for setting password._
- [number] **Exit Saving Changes**
    - _Ok_
- [number] **Cancel**
    - _Yes_
- [number] **No** — + =Move Selection Up / Changes have been saved. / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _[General Help]_
- [number] **Push PageUp    - previous**
    - _Push PageDown  - Next Page_
- [number] **F1**
    - _Help_
- [number] **↑↓**
    - _Select Item_
- [select] **F5/F6** — + =Move Selection Up / Changes have been saved. / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _Change Values_
- [number] **F9**
    - _Setup Defaults_
- [number] **Esc**
    - _Exit_
- [number] **←→**
    - _Select Menu_
- [select] **Enter** — + =Move Selection Up / Changes have been saved. / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _Select ► Sub-Menu_
- [number] **F10**
    - _Save and Exit_
- [number] **Password check Fail!! **
    - _Add an new file\Do you wish to add this file to allowable database?_
- [number] **Help**
    - _Select Item_
- [select] **Select Menu** — + =Move Selection Up / Changes have been saved. / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _Select_
- [number] **Change Values**
    - _Setup Default_
- [number] **Exit**
    - _Save and Exit_
- [number] **Item Specific Help**
    - _System Halted_
- [select] **Enter Old password** — + =Move Selection Up / Changes have been saved. / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _Enter New Password_
- [number] **Confirm New Password**
    - _Set password success !_
- [number] **Enter old password incorrect !**
    - _New password confirm fail !_
- [number] **Enter incorrect password over 3 times, system will halt !!**
    - _Copyright (C) Acer Inc._
- [select] **Press Esc for boot options** — + =Move Selection Up / Changes have been saved. / textpadding='60,2,5,2' height='54' fontsize='40' textcolor='0xFF000000' bkcolor='0xF4F4F4' bkimage='0'  bkcolor2='0xF4F4F4'★
    - _Esc is pressed. Go to boot options._
- [select] **Push PageDown  - Next Page** — Help★ / Select Item / ↑↓
    - _F1_
- [toggle] **<VerticalLayout name='background' bkcolor='0xFF004D60' inset='16,28,16,28' ><Label name='title' height='60' align='center' fontsize='40' textcolor='0xFFFFFF' /><VerticalLayout vscrollbar='true' ><Label name='showstring' fontsize='20' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout  name='content' height='30' /></VerticalLayout>** — <VerticalLayout name='background' bkcolor='0xFF004D60' inset='16,28,16,28' ><Label name='title' height='60' align='center' fontsize='40' textcolor='0xFFFFFF' /><VerticalLayout vscrollbar='true' ><Label name='showstring' fontsize='20' textcolor='0xFFFFFF' /></VerticalLayout><HorizontalLayout  name='content' height='30' /></VerticalLayout>★
- [select] **Press 'Y' to save and exit, 'N' to discard and exit.** — <Spacebar>Toggle Checkbox / 0-9 a-f are valid inputs★
    - _InsydeH2O Setup Utility_

## Enable or disable LAN Low Power Mode  (2 settings)

- [select] **Camera 0 Enable** — RT3663 VRM PSI0 Workaround / For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state.★
    - _Enable or disable the power of REAR CAMERA_
- [select] **Disable or enable EVAL card auto detection** — Touch Panel Support★ / Enable/Disable exposing of _HID(PNP0C50) in ACPI ASL code to OS / Touch Pad Support / Under I2C 0 Bus / Under I2C 1 Bus
    - _Enable/Disable exposing of _HID(BCM2F25) in ACPI ASL code to OS_

## Espacio insuficiente para almacenar la imagen.  (18 settings)

- [select] **Menú de configuración MBA** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
- [select] **Administración FW** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Página de configuración principal** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Parámetros generales de iSCSI_
- [select] **Parámetros generales de iSCSI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurar parámetros generales de arranque iSCSI.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Parámetros de iniciador de iSCSI_
- [select] **Parámetros de iniciador de iSCSI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurar parámetros de iniciador de iSCSI.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Parámetros de primer destino de iSCSI_
- [select] **Dispositivo secundario** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configurar parámetros de dispositivo secundario._
- [select] **Parámetros de dispositivo secundario iSCSI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurar parámetros de dispositivo secundario.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Opción ROM** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Habilitar/Deshabilitar opción ROM de arranque** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Detección automática_
- [select] **BBS** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Int 18 h_
- [select] **Int 19 h** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Ocultar solicitud de configuración_
- [select] **Ocultar solicitud de configuración** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configurar si se muestra la solicitud de configuración durante la inicialización ROM._
- [select] **Configurar pulsación de tecla** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurar pulsaciones de teclas para llamar al menú de configuración.** — Ctrl-B / Tiempo de espera de mensaje de banner★
    - _Ctrl-S_
- [select] **Menú de configuración de arranque iSCSI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configurar parámetros de arranque iSCSI._

## RealManage Setup  (36 settings)

- [select] **Gateway** — DNS★ / Echoservice / Set or change DASH DNS
    - _Set or change DASH gateway_
- [toggle] **Enable or Disble DASH Echoservice** — Driver Name: / Host Configuration / Disabled★
    - _Provision Mode_
- [toggle] **Link Speed & Duplex** — Link Speed & Duplex★
- [select] **Provisioning Model** — Device Information / %s★
    - _Configure DASH provision settings_
- [select] **Configure DASH host settings** — TCP/IP Configuration★ / Configure DASH TCP/IP settings
    - _Host Configuration_
- [select] **Configure DASH(Desktop and Mobile Architecture for System Hardware) setting. DASH is a web services-based standard that can support both in-band and out-of-band management.** — Host Configuration / Disabled★
    - _Realtek RealManage Setup_
- [number] **TCP/IP Configuration**
    - _Configure DASH TCP/IP settings_
- [number] **Configure DASH provision settings**
    - _Provisioning Model_
- [number] **Setup and Configuration** — Driver Name: / Host Configuration / Disabled★
    - _Configure DASH security settings_
- [number] **Set or change DASH host name**
    - _Domain Name_
- [number] **Set or change DASH domain name**
    - _DHCPv4_
- [number] **Enable or Disble DASH DHCP service**
    - _OOBip_
- [select] **Set or change DASH IP** — Driver Name: / Host Configuration / Disabled★
    - _Subnetmask_
- [number] **Set or change DASH subnetmask**
    - _Gateway_
- [number] **Set or change DASH gateway**
    - _DNS_
- [number] **Set or change DASH DNS**
    - _Echoservice_
- [number] **Change DASH provision mode. Provision mode support Enterprise/Small business**
    - _Provision State_
- [number] **Change DASH provision state. Provision state support Un-provisioned/Prepared provision/Provisioned**
    - _Provision ServerIP_
- [number] **Set or change DASH provision server IP**
    - _Provision Port_
- [select] **Set or change DASH provision port** — Driver Name: / Host Configuration / Disabled★
    - _Enterprise_
- [number] **Small Business**
    - _Provisioned_
- [number] **Un-Provisioned**
    - _Prepared Provisioned_
- [number] **Security Configuration**
    - _Configure DASH account settings_
- [select] **Modify username** — Driver Name: / Host Configuration / Disabled★
    - _Set or change DASH username_
- [number] **Modify password**
    - _Set or change DASH password_
- [number] **TLS PSK**
    - _PID for PSK_
- [number] **Set or change DASH PSK PID**
    - _PPS for PSK_
- [select] **Set or change DASH PSK PPS** — Driver Name: / Host Configuration / Disabled★
    - _TLS PKI_
- [number] **Manage Certificate Hashes**
    - _Configure DASH PKI hash tables_
- [number] **Certificate Hash1 for PKI**
    - _Affirmative or negative DASH first PKI hash value_
- [number] **Hash1 Value**
    - _Set or change DASH first PKI hash value_
- [select] **Certificate Hash2 for PKI** — Driver Name: / Host Configuration / Disabled★
    - _Affirmative or negative DASH second PKI hash value_
- [number] **Hash2 Value**
    - _Set or change DASH second PKI hash value_
- [number] **Certificate Hash3 for PKI**
    - _Affirmative or negative DASH third PKI hash value_
- [number] **Hash3 Value**
    - _Set or change DASH third PKI hash value_
- [select] **Certificate Hash4 for PKI** — Driver Name: / %s / Disabled★
    - _Affirmative or negative DASH forth PKI hash value_

## VLAN Mode  (42 settings)

- [select] **Use independent target portal when multipath I/O is enabled.** — Energy Efficient Ethernet / Use Independent Target Portal / Input secondary device MAC address. Use XX:XX:XX:XX:XX:XX format.★
    - _Use Independent Target Name_
- [select] **EFI** — Controller BIOS Version★ / MBA
    - _Fcode_
- [select] **NIC Configuration** — iSCSI Boot Configuration Menu★ / iSCSI Configuration / Configure iSCSI boot parameters.
    - _iSCSI Boot Configuration Menu_
- [toggle] **iSCSI Configuration** — Legacy Boot Protocol / VLAN ID (1..4094) / Bus:Device:Function★
    - _Firmware Image Menu_
- [select] **00:00:00:00:00:00** — PCI Device ID★
    - _0_
- [toggle] **Setup Key Stroke**
    - _Configure key strokes to invoke configuration menu._
- [toggle] **Ctrl-S**
    - _Ctrl-B_
- [toggle] **Banner Message Timeout**
- [toggle] **Select timeout value. (0 defaults to 4 seconds, 15 is no delay, 1-14 is timeout value in seconds)**
    - _BRCM ISAN_
- [toggle] **0.0.0.0**
    - _iqn.1995-05.com.broadcom.iscsiboot_
- [toggle] **MAC Address** — MAC Address★
- [select] **100Mbps Half** — Boot Strap Type / None★
    - _100Mbps Full_
- [select] **Virtual LAN ID** — AutoNeg / 10Mbps Half / 10Mbps Full★
    - _Configure virtual LAN ID (1..4094)._
- [select] **Virtual LAN Mode** — VLAN ID (1..4094) / Bus:Device:Function★
    - _Configure virtual LAN mode._
- [number] **AutoNeg**
    - _10Mbps Half_
- [number] **10Mbps Full**
    - _100Mbps Half_
- [number] **100Mbps Full**
    - _Auto Negotiated_
- [number] **10 Mbps Half**
    - _10 Mbps Full_
- [select] **100 Mbps Half** — Legacy Boot Protocol / VLAN ID (1..4094) / Bus:Device:Function★
    - _100 Mbps Full_
- [number] **Disabled**
    - _Enabled_
- [number] **One Time Disabled**
    - _IPv4_
- [number] **IPv6**
    - _MBA Configuration Menu_
- [select] **MBA Configuration Menu** — Legacy Boot Protocol / VLAN ID (1..4094) / Bus:Device:Function★
    - _Configure Multiple Boot Agent (MBA) parameters._
- [number] **iSCSI Boot Configuration Menu**
- [number] **Configure iSCSI boot parameters.**
    - _iSCSI Configuration_
- [number] **Firmware Image Menu**
    - _Firmware image information._
- [number] **Listing of firmware image components (and their corresponding versions) currently programmed on the NVRAM.  N/A indicates the image is not present.**
- [select] **Firmware Image Properties** — Legacy Boot Protocol / VLAN ID (1..4094) / Bus:Device:Function★
    - _TCP/IP Parameters via DHCP_
- [number] **Acquire TCP/IP configuration via DHCP.**
    - _IP Autoconfiguration_
- [number] **IP Auto-Configuration**
    - _Acquire TCP/IP configuration via Stateful or Stateless Autoconfiguration._
- [number] **iSCSI Parameters via DHCP**
    - _Acquire iSCSI parameters via DHCP._
- [select] **CHAP Authentication** — Legacy Boot Protocol / VLAN ID (1..4094) / Bus:Device:Function★
    - _Enable/Disable CHAP authentication._
- [number] **Boot to iSCSI Target**
    - _Boot to Target_
- [number] **Enable/Disable booting to iSCSI target after logon.**
    - _DHCP Vendor ID_
- [number] **Configure DHCP vendor ID (up to 32 bytes long).**
    - _Link Up Delay Time_
- [select] **Configure link up delay time in seconds (0..255).** — Legacy Boot Protocol / VLAN ID (1..4094) / Bus:Device:Function★
    - _Use TCP Timestamp_
- [number] **TCP Timestamp**
    - _Enable/Disable TCP timestamp._
- [number] **Target as First HDD**
    - _Enable/Disable target appears as first hard disk drive (HDD) in the system._
- [number] **LUN Busy Retry Count**
    - _Configure number of retries in 2 second intervals when LUN is busy (0..60)._
- [select] **IP Version** — Legacy Boot Protocol / VLAN ID (1..4094) / Bus:Device:Function★
    - _IP version support.  Modifying this parameter will reset all IP-related fields._
- [number] **IP Address**
    - _Configure initiator IP address._
- [select] **Subnet Mask** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★
    - _Configure IP subnet mask._

## <Enter>=￱選擇項目￰  (1 settings)

- [select] **Press 'Y' to save and exit, 'N' to discard and exit.**
    - _￱系微設置工具￰_

## Esc=￱離開項目￰  (5 settings)

- [select] **￱是￰** — ￱否￰
    - _￱說明￰_
- [select] **￱無效的密碼￰!￱請重輸設定密碼￰** — ￱確定￰★ / ￱取消￰
    - _￱離開並儲存設定￰_
- [select] **↑↓**
    - _￱選擇項目￰_
- [select] **F5/F6**
    - _￱調整數值￰_
- [select] **F9**
    - _￱預設值￰_

## +/- =￱値調整￰  (10 settings)

- [select] **￱新しいパスワード入力￰**
    - _￱パスワード再入力￰_
- [select] **￱パスワードが同一ではありません￰**
    - _￱パスワードに誤りがあります￰_
- [select] **Enter/ESC￱キー￰ - ￱終了￰** — Pg Dn￱キー￰     - ￱ページダウン￰★
    - _Pg Up￱キー￰     - ￱ページアップ￰_
- [select] **Setup Warning** — ￱変更を保存しました￰★ / [￱継続￰]
    - _￱設定注意事項￰_
- [select] **Esc=Exit Menu**
    - _F10=Save and Exit_
- [select] **￱無効なパスワード￰!￱パスワード設定のために新しい文字列を入力してください。￰**
    - _￱変更を保存して終了￰_
- [select] **￱オーケー￰**
    - _￱取消￰_
- [select] **￱はい￰**
    - _￱いいえ￰_
- [select] **Press 'Y' to save and exit, 'N' to discard and exit.**
    - _InsydeH2O ￱セットアップユーティリティ￰_
- [select] **ENTER￱を押してください￰**
    - _￱データ入力￰_

## ↑ and ↓ to change option, ENTER to select an option, ESC to exit  (1 settings)

- [number] **Legacy USB**
    - _Legacy Embedded Network_

## Sello de tiempo TCP  (6 settings)

- [select] **Destino como primera HDD** — Bus:Dispositivo:Función★ / Revisión/tipo de chip.
    - _Habilitar/Deshabilitar la aparición del destino como primera unidad de disco duro (HDD) en el sistema._
- [select] **Versión de IP** — Bus:Dispositivo:Función★ / Revisión/tipo de chip.
    - _Compatibilidad con la versión de IP. Al modificar este parámetro se restablecerán todos los campos relacionados con la IP._
- [select] **Dirección IP** — Bus:Dispositivo:Función★ / Revisión/tipo de chip.
    - _Configurar dirección IP de destino._
- [select] **Máscara de subred** — Bus:Dispositivo:Función★ / Revisión/tipo de chip.
    - _Configurar máscara de subred de IP._
- [select] **Puerta de enlace predeterminada** — Bus:Dispositivo:Función★ / Revisión/tipo de chip.
    - _Configurar dirección IP de puerta de enlace predeterminada._
- [select] **DNS secundario** — Bus:Dispositivo:Función★ / Revisión/tipo de chip.
    - _Configurar dirección IP del DNS secundario._

## CHAP 秘密情報  (6 settings)

- [select] **CHAP 秘密情報** — MAC アドレス★ / 固定 MAC アドレス
    - _CHAP 秘密情報を設定する (12 ～ 16 文字)。_
- [select] **セカンダリ デバイス** — MAC アドレス★
- [select] **接続** — MAC アドレス / 固定 MAC アドレス★
    - _ターゲットの確立をイネーブル/ディスエーブルする。_
- [select] **TCP ポート** — MAC アドレス★ / ターゲット TCP ポート番号を設定する (1 ～ 65535)。 / TCP ポート
    - _ターゲット TCP ポート番号を設定する (1 ～ 65535)。_
- [number] **ターゲット ブート LUN 番号を設定する (0 ～ 255)。**
    - _チップのタイプと改訂番号。_
- [select] **ブート LUN** — MAC アドレス / 固定 MAC アドレス★
    - _ターゲット ブート LUN 番号を設定する (0 ～ 255)。_

## Configurar dirección IP de puerta de enlace predeterminada.  (2 settings)

- [select] **DNS primario** — DNS secundario / Configurar dirección IP del DNS secundario. / Nombre de iSCSI / Bus:Dispositivo:Función★
- [select] **Configurar nombre de iSCSI.** — LED intermitentes / Bus:Dispositivo:Función★
    - _Nombre de iSCSI_

## Dirección MAC  (11 settings)

- [select] **Configurar nombre de iSCSI.** — Protocolo de arranque heredado / Configurar nombre de iSCSI. / ID CHAP / Configurar identificación CHAP (hasta 32 caracteres de longitud). / Configurar identificación CHAP (hasta 128 caracteres de longitud). / Bus:Dispositivo:Función★
    - _Nombre de iSCSI_
- [select] **ID CHAP** — Protocolo de arranque heredado / iSCSI / Bus:Dispositivo:Función★
    - _Configurar identificación CHAP (hasta 32 caracteres de longitud)._
- [select] **Configurar identificación CHAP (hasta 128 caracteres de longitud).** — ID CHAP / Configurar identificación CHAP (hasta 32 caracteres de longitud). / Bus:Dispositivo:Función★ / Protocolo de arranque heredado / iSCSI
    - _ID CHAP_
- [select] **Secreto CHAP** — Protocolo de arranque heredado / iSCSI / Bus:Dispositivo:Función★
    - _Configurar secreto CHAP (entre 12 y 16 caracteres de longitud)._
- [select] **Configurar secreto CHAP (entre 12 y 16 caracteres de longitud).** — Secreto CHAP / Configurar secreto CHAP (entre 12 y 16 caracteres de longitud). / Bus:Dispositivo:Función★
    - _Secreto CHAP_
- [select] **Conectar** — Protocolo de arranque heredado / iSCSI / Bus:Dispositivo:Función★ / Puerto TCP / Configurar número de puerto TCP de destino (1..65535).
    - _Habilitar/Deshabilitar establecimiento de destino._
- [select] **LUN de arranque** — LUN de arranque / Configurar número LUN de arranque de destino (0..255). / Dispositivo secundario / Introducir dirección MAC de dispositivo secundario. Utilizar formato XX:XX:XX:XX:XX:XX. / Bus:Dispositivo:Función★
    - _Configurar número LUN de arranque de destino (0..255)._
- [select] **Dirección MAC de dispositivo secundario** — Protocolo de arranque heredado / iSCSI / Bus:Dispositivo:Función★
    - _Utilizar portal de destino independiente_
- [select] **Utilizar portal de destino independiente** — Protocolo de arranque heredado / iSCSI / Bus:Dispositivo:Función★
    - _Utilizar portal de destino independiente cuando esté habilitada la E/S de múltiples rutas._
- [select] **Utilizar nombre de destino independiente** — Protocolo de arranque heredado / iSCSI / Bus:Dispositivo:Función★
- [select] **Utilizar nombre de destino independiente cuando esté habilitada la E/S de múltiples rutas.** — Protocolo de arranque heredado / iSCSI / Bus:Dispositivo:Función★
    - _Versión del firmware de familia_

## VLAN-Modus  (41 settings)

- [select] **Unabhängiges Zielportal verwenden wenn Multipath I/O aktiviert ist.** — Unabhängiges Zielportal verwenden / Eingabe der MAC-Adresse des sekundären Geräts. XX:XX:XX:XX:XX:XX-Format verwenden.★
    - _Unabhängigen Zielnamen verwenden_
- [select] **EFI** — BIOS-Version des Controllers★ / MBA
    - _Fcode_
- [select] **NIC-Konfiguration** — iSCSI-Boot-Konfigurationsmenü★ / iSCSI-Konfiguration / iSCSI-Bootparameter konfigurieren.
    - _iSCSI-Boot-Konfigurationsmenü_
- [toggle] **iSCSI-Konfiguration** — Bootprotokolle älterer Geräte / VLAN-ID (1..4094) / Bus:Gerät:Funktion★
    - _Menü Firmware Image_
- [select] **00:00:00:00:00:00** — PCI-Geräte-ID★
- [toggle] **Tastenanschlag eingeben**
    - _Tastenanschläge konfigurieren, um das Konfigurationsmenü aufzurufen._
- [toggle] **Strg-S**
    - _Strg-B_
- [toggle] **Banner-Nachricht Zeitüberschreitung**
- [toggle] **Wert für Zeitüberschreitung auswählen. (0 ist standardmäßig auf 4 Sekunden eingestellt, 15 bedeutet keine Zeitüberschreitung, 1-14 ist der Wert der Zeitüberschreitung in Sekunden)**
    - _BRCM ISAN_
- [toggle] **0.0.0.0**
    - _iqn.1995-05.com.broadcom.iscsiboot_
- [toggle] **MAC-Adresse** — MAC-Adresse★
- [select] **100 Mbps Halb** — Boot-Strap-Typ / None★ / Bootprotokolle älterer Geräte / VLAN-ID (1..4094) / Bus:Gerät:Funktion
    - _100 Mbps Voll_
- [select] **Virtuelle LAN-ID** — Auto Neg / 10 Mbps Halb / 10 Mbps Voll★
    - _Virtuelle LAN-ID (1..4094) konfigurieren._
- [select] **Virtuellen LAN-Modus** — VLAN-ID (1..4094) / Bus:Gerät:Funktion★
    - _Virtuellen LAN-Modus konfigurieren._
- [number] **Auto Neg**
    - _10 Mbps Halb_
- [number] **10 Mbps Voll**
    - _100 Mbps Halb_
- [number] **100 Mbps Voll**
    - _Automatische Aushandlung_
- [number] **10 Mbps Halb**
    - _10 Mbps Voll_
- [number] **Deaktiviert**
    - _Aktiviert_
- [number] **Einmalige Deaktivierung**
    - _IPv4_
- [number] **IPv6**
    - _MBA-Konfigurationsmenü_
- [select] **MBA-Konfigurationsmenü** — Bootprotokolle älterer Geräte / VLAN-ID (1..4094) / Bus:Gerät:Funktion★
    - _Multiple-Boot-Agent-Parameter (MBA) konfigurieren._
- [number] **iSCSI-Boot-Konfigurationsmenü**
- [number] **iSCSI-Bootparameter konfigurieren.**
    - _iSCSI-Konfiguration_
- [number] **Menü Firmware Image**
    - _Firmware-Image-Information_
- [number] **Liste mit Firmware-Image-Komponenten (und den entsprechenden Versionen), die momentan auf dem NVRAM gespeichert sind. Ein Gedankenstrich bedeutet, dass das Image nicht vorhanden ist.**
- [select] **Firmware-Image-Eigenschaften** — Bootprotokolle älterer Geräte / VLAN-ID (1..4094) / Bus:Gerät:Funktion★
    - _TCP/IP-Parameter über DHCP_
- [number] **TCP/IP-Konfigurationseinstellungen über DHCP erhalten.**
    - _IP-Autokonfiguration_
- [number] **Automatische IP-Konfiguration**
    - _TCP/IP-Konfigurationseinstellungen über zustandbehaftete oder zustandslose Autokonfiguration erhalten._
- [number] **iSCSI-Parameter über DHCP**
    - _iSCSI-Parameter über DHCP erhalten._
- [select] **CHAP-Authentifizierung** — Bootprotokolle älterer Geräte / VLAN-ID (1..4094) / Bus:Gerät:Funktion★
    - _CHAP-Authentifizierung aktivieren/deaktivieren_
- [number] **Booten von iSCSI-Ziel**
    - _Booten von Ziel_
- [number] **Booten von iSCSI-Ziel nach dem Einloggen aktivieren/deaktivieren**
    - _DHCP Vendor ID_
- [number] **DHCP Vendor ID konfigurieren (bis zu 32 Bytes lang).**
    - _Verzögerung nach Verbindungsaufbau_
- [select] **Verzögerung nach Verbindungsaufbau in Sekunden (0..255) konfigurieren.** — Bootprotokolle älterer Geräte / VLAN-ID (1..4094) / Bus:Gerät:Funktion★
    - _TCP-Zeitstempel verwenden_
- [number] **TCP-Zeitstempel**
    - _TCP-Zeitstempel aktivieren/deaktivieren_
- [number] **Ziel als erstes HDD**
    - _Ziel erscheint als erstes Festplattenlaufwerk (HDD) im System._
- [number] **Anzahl Wiederholungen bei 'LUN besetzt'**
    - _Konfiguration der Anzahl der Wiederholungen auf 2 Sekunden wenn LUN besetzt ist (0..60)._
- [select] **IP-Version** — Bootprotokolle älterer Geräte / VLAN-ID (1..4094) / Bus:Gerät:Funktion★
    - _IP-Version-Support. Eine Änderung dieses Parameters setzt alle IP-bezogenen Felder zurück._
- [number] **IP-Adresse**
    - _Initiator-IP-Adresse konfigurieren_
- [select] **Subnetzmaske** — Bootprotokolle älterer Geräte / iSCSI / Bus:Gerät:Funktion★
    - _Subnetzmaske konfigurieren._

## Disable CPB  (14 settings)

- [select] **Customized** — 33h Clk★ / 34h Clk
    - _Custom Pstates / Throttling_
- [select] **Core/Thread Enablement** — 33h Clk★ / 34h Clk / Specifies the core frequency multiplier. COF = 200MHz * FID / DID
    - _Streaming Stores Control_
- [select] **Custom Pstate0** — Custom★ / Frequency (MHz)
- [select] **Specifies the core voltage.** — 33h Clk★ / 34h Clk
    - _Custom Pstate1_
- [select] **Specifies the core frequency multiplier. COF = 200MHz * FID / DID** — 33h Clk★ / 34h Clk
    - _Pstate1 DID_
- [select] **Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah).** — 33h Clk★ / 34h Clk
    - _Pstate1 VID_
- [select] **Current core frequency in MHz** — Voltage in uV (1V = 1000 * 1000 uV)★ / Pstate0 FID
    - _Voltage (uV)_
- [select] **Enables or disables the streaming stores functionality** — 33h Clk / 34h Clk★
    - _Enable IBS_
- [select] **1900MHz** — 33h Clk / 34h Clk★
    - _1933MHz_
- [select] **1967MHz** — 33h Clk / 34h Clk★
    - _2000MHz_
- [select] **21h Clk** — 33h Clk★ / 34h Clk
    - _Trcdrd_
- [select] **This sets the RAS# Active to CAS# read/write delay.** — 33h Clk★ / 34h Clk
    - _Trcdwr_
- [select] **333MHz** — 33h Clk / 34h Clk★
    - _400MHz_
- [select] **533MHz** — 33h Clk / 34h Clk★
    - _1050MHz_

## Accept  (45 settings)

- [select] **Enable / disable DF C-states (DF::CstateControl[DfCstateDisable])** — Legal Disclaimer / DF C-state control / 2 KB★
    - _xGMI DLWM control_
- [select] **Security** — No help string★ / Operating your AMD processor outside of specification or in excess of factory settings, including but not limited to overclocking, may damage or shorten the life of your processor or other system components, create system instabilities (e.g., data loss and corrupted images) and in extreme cases may result in total system failure. AMD does not provide support or service for issues or damages related to use of an AMD processor outside of processor specifications or in excess of factory settings.
    - _WARNING - DAMAGE CAUSED BY USE OF YOUR AMD PROCESSOR OUTSIDE OF SPECIFICATION OR IN EXCESS OF FACTORY SETTINGS ARE NOT COVERED UNDER YOUR AMD PRODUCT WARRANT..._
- [select] **Specifies the core frequency multiplier. COF = 200MHz * FID / DID** — Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah).★ / Specifies the core voltage. / Pstate2 VID / Normal Operation / No help string
    - _Pstate2 DID_
- [toggle] **Custom Pstate3** — Disabled / Custom / Auto★
- [select] **1Dh Clk** — 1Fh Clk / 20h Clk★
    - _1Eh Clk_
- [toggle] **13h Clk**
    - _14h Clk_
- [toggle] **15h Clk**
    - _16h Clk_
- [toggle] **17h Clk**
    - _18h Clk_
- [toggle] **19h Clk**
    - _1Ah Clk_
- [toggle] **1Bh Clk**
    - _1Ch Clk_
- [toggle] **DF Common Options** — DF Common Options★
- [select] **Frequency (MHz)** — Voltage (uV) / Voltage in uV (1V = 1000 * 1000 uV) / Pstate0 FID★
    - _Current core frequency in MHz_
- [select] **Custom Pstate0** — Custom / Auto★
- [number] **Voltage (uV)**
    - _Voltage in uV (1V = 1000 * 1000 uV)_
- [number] **Pstate0 FID**
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [number] **Pstate0 DID**
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [number] **Pstate0 VID**
    - _Specifies the core voltage._
- [select] **Custom Pstate1** — Disabled / Custom / Auto★
- [number] **Pstate1 FID**
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [number] **Pstate1 DID**
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [number] **Pstate1 VID**
    - _Specifies the core voltage._
- [select] **Custom Pstate2** — Disabled / Custom / Auto★
- [number] **Pstate2 FID**
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [number] **Pstate2 DID**
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [number] **Pstate2 VID**
    - _Specifies the core voltage._
- [number] **Pstate3 FID**
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [number] **Pstate3 DID**
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [number] **Pstate3 VID**
    - _Specifies the core voltage._
- [select] **Custom Pstate4** — Disabled / Custom / Auto★
- [number] **Pstate4 FID**
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [number] **Pstate4 DID**
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [number] **Pstate4 VID**
    - _Specifies the core voltage._
- [select] **Custom Pstate5** — Disabled / Custom / Auto★
- [number] **Pstate5 FID**
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [number] **Pstate5 DID**
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [number] **Pstate5 VID**
    - _Specifies the core voltage._
- [select] **Custom Pstate6** — Disabled / Custom / Auto★
- [number] **Pstate6 FID**
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [number] **Pstate6 DID**
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [number] **Pstate6 VID**
    - _Specifies the core voltage._
- [select] **Custom Pstate7** — Disabled / Custom / Auto★
- [number] **Pstate7 FID**
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_
- [number] **Pstate7 DID**
    - _Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah)._
- [number] **Pstate7 VID**
    - _Specifies the core voltage._
- [select] **Relaxed EDC throttling** — Disabled / Enabled / Auto★

## Overclock  (1 settings)

- [select] **This sets the RAS# Active to CAS# read/write delay.** — 1667MHz★ / 2067MHz / 2100MHz / Tcl / Sets the tCL time. / 8 Clk / 9 Clk
    - _0xA Clk_

## Veuillez entrer des caractères suffisants  (21 settings)

- [select] **Setup Warning** — Des changements ont été sauvegardés
    - _Avis de Configuration_
- [number] **[continuer]** — Enregistrer les modifications et quitter? / Question valeur décalage avec l'option valeur! / Changes have not saved. Save Changes or not?★
    - _Changes have been saved after press _
- [number] **Enregistrer les modifications et quitter?**
    - _Question valeur décalage avec l'option valeur!_
- [number] **Changes have not saved. Save Changes or not?**
    - _Press 'Y' to save and exit, 'N' to discard and exit._
- [number] **Logiciel de Configuration d'InsydeH2O**
- [number] **Rev. 5.0**
    - _Esc=Exit Menu_
- [select] **F10=Save and Exit** — + =rejette des Changements / Des changements ont été sauvegardés
    - _Mot de Passe Invalide! Enter nouvelle chaîneou configurez le mot de passe._
- [number] **Quitter en Sauvegardant les Modifications**
    - _Ok_
- [number] **Annuler**
    - _Oui_
- [number] **Non** — + =rejette des Changements / Des changements ont été sauvegardés
    - _[Aide générale]_
- [number] **Appuyer sur Page Précédente - Précédent**
    - _Appuyer sur Page Suivante   - la Page Suivante_
- [number] **F1**
    - _Aide_
- [number] **↑↓**
    - _Sélect. élément_
- [select] **F5/F6** — + =rejette des Changements / Des changements ont été sauvegardés
    - _Modifier les valeurs_
- [number] **F9**
    - _Définir défauts_
- [number] **Ese**
    - _Quitter_
- [number] **←→**
    - _Sélection menu_
- [select] **Enter** — + =rejette des Changements / Des changements ont été sauvegardés
    - _Sélectionner►Sous-menu_
- [number] **F10**
    - _Enreg. et quit._
- [select] **Appuyer sur Page Suivante   - la Page Suivante** — Aide★ / Sélect. élément / ↑↓
    - _F1_
- [select] **Press 'Y' to save and exit, 'N' to discard and exit.** — <Spacebar>Bascule la Case de pointage / 0-9 a-f sont des données valides★
    - _Logiciel de Configuration d'InsydeH2O_

## 38bit (256GB)  (19 settings)

- [select] **Enable/Disable Reduce Hardware Support. Please disable PME wakeup, when Reduce Hardware enabled.** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state.★ / RT3663 VRM PSI0 Workaround
    - _Wake on PME_
- [select] **VDD18 voltage (ANPEC:-110mv/TI:-112.5mv)** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _VDD18 voltage (ANPEC:-120mv/TI:-125mv)_
- [select] **VDD18 voltage (ANPEC:-130mv/TI:-137.5mv)** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _5V_S5 voltage._
- [select] **5V_S5 voltage setting for ANPEC PSA** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _5v_ALW(default)_
- [select] **5v_ALW +60mv** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _5v_ALW +100mv_
- [select] **AMD KVM Mouse Protocol** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _Swtich KVM Mouse Protocol between Absolut/Simple_
- [select] **Absolute** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _Simple_
- [select] **AMD DPTC interface** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _Dynamic Power and Thermal Control Interface Enable/Disable_
- [select] **GPIO 11 Output Low** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _GPIO 11 Output High_
- [select] **Serial Debug Message Under OS** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _Enable Serial Debug Message Under OS_
- [select] **AMD Firmware Version** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _Show all of AMD Firmware Version_
- [select] **AGESA Version** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _0_
- [select] **PSP BootLoader Version** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _0_
- [select] **PSP SecureOS Version** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _0_
- [select] **ABL Version** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _0_
- [select] **APCB Version** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _0_
- [select] **APOB Version** — For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state. / RT3663 VRM PSI0 Workaround★
    - _0_
- [select] **Ucode Patch Version** — SMU FW Version / 0 / SMU RV2 FW Version★
    - _0_
- [select] **Turn Unused GPP Clocks Off** — RT3663 VRM PSI0 Workaround★ / For NVIDIA mobile DGPU card only. Output DGPU_EN# A19 pin and DGPU_SEL# B17 pin to high at every power on state.
    - _Clock PM: CLK_REQ0_

## <Enter>=Choisir l'Entrée  (1 settings)

- [select] **Press 'Y' to save and exit, 'N' to discard and exit.**
    - _Logiciel de Configuration d'InsydeH2O_

## Esc=Sortir l'Entrée  (5 settings)

- [select] **Oui** — Non
    - _Aide_
- [select] **Mot de Passe Invalide! Enter nouvelle chaîneou configurez le mot de passe.** — Ok★ / Annuler
    - _Quitter en Sauvegardant les Modifications_
- [select] **↑↓**
    - _Sélect. élément_
- [select] **F5/F6**
    - _Modifier les valeurs_
- [select] **F9**
    - _Définir défauts_

## Permanente MAC-Adresse  (7 settings)

- [select] **PCI-Bus:Gerät:Funktionsnummer für dieses Gerät.** — PCI-Adresse / Bus:Gerät:Funktion★
    - _Verbindungsstatus_
- [select] **Verbindungsstatus** — Verbindung getrennt / Blinkende LEDs / Bus:Gerät:Funktion★
    - _Verbunden_
- [select] **Blinkende LEDs für bis zu 15 Sekunden** — Bootprotokolle älterer Geräte / Bus:Gerät:Funktion★
    - _Bootprotokolle älterer Geräte_
- [select] **Nicht-UEFI Boot-Protokoll auswählen: Preboot Execution Environment (PXE)/iSCSI.** — Bootprotokolle älterer Geräte / iSCSI / Bus:Gerät:Funktion★
    - _PXE_
- [select] **NONE** — Boot-Strap-Typ★ / Boot-Strap-Typ auswählen.
    - _None_
- [select] **Übertragungsrate konfigurieren.** — Bootprotokolle älterer Geräte / iSCSI / Bus:Gerät:Funktion★
    - _Pre-boot Wake On LAN_
- [select] **Pre-boot Wake On LAN (WOL) konfigurieren** — Bootprotokolle älterer Geräte / iSCSI / Bus:Gerät:Funktion★
    - _Wake On LAN_

## Configure network parameters.  (1 settings)

- [number] **Local NetMask**

## Zen Common Options  (8 settings)

- [select] **RedirectForReturnDis** — Auto★ / 1 / 0
    - _From a workaround for GCC/C000005 issue for XV Core on CZ A0, setting MSRC001_1029 Decode Configuration (DE_CFG) bit 14 [DecfgNoRdrctForReturns] to 1_
- [select] **L2 TLB Associativity** — 0 / 1 / Auto★
    - _0 - L2 TLB ways [11:8] are fully associative.  1 - =L2 TLB ways [11:8] are 4K-only._
- [select] **Platform First Error Handling** — Enable / Disable / Auto★
    - _Enable/disable PFEH, cloak individual banks, and mask deferred error interrupts from each bank._
- [select] **Core Performance Boost** — Disabled / Auto★
    - _Disable CPB_
- [select] **Global C-state Control** — Disabled / Enabled / Auto★
    - _Controls IO based C-state generation and DF C-states._
- [select] **OC Mode** — Normal Operation★ / OC1 / Customized
    - _No help string_
- [select] **Streaming Stores Control** — Disabled / Enabled / Auto★
    - _Enables or disables the streaming stores functionality_
- [select] **Enable IBS** — Disabled / Enabled / Auto★
    - _When IBS is enabled, SpecLockMap and Stack Engine are disabled._

## Agree  (2 settings)

- [select] **Downcore control** — ONE / TWO / THREE / Auto★
- [select] **SMTEN** — Disable / Auto★

## DF Common Options  (14 settings)

- [select] **DRAM scrub time** — Disabled / 1 hour / 4 hours / 8 hours / 16 hours / 24 hours / 48 hours / Auto★
    - _Provide a value that is the number of hours to scrub memory._
- [select] **Redirect scrubber control** — Disabled / Enabled / Auto★
    - _Control DF::RedirScrubCtrl[EnRedirScrub]_
- [select] **Disable DF sync flood propagation** — Sync flood disabled / Sync flood enabled / Auto★
    - _Control DF::PIEConfig[DisSyncFloodProp]_
- [select] **GMI encryption control** — Disabled / Enabled / Auto★
    - _Control GMI link encryption_
- [select] **xGMI encryption control** — Disabled / Enabled / Auto★
    - _Control xGMI link encryption_
- [select] **CC6 memory region encryption** — Disabled / Enabled / Auto★
    - _Control whether or not the CC6 save/restore memory is encrypted_
- [select] **Location of private memory regions** — Distributed / Consolidated / Auto★
    - _Controls whether or not the private memory regions (PSP, SMU and CC6) are at the top of DRAM or distributed. Note that distributed requires memory on all die..._
- [select] **System probe filter** — Disabled / Enabled / Auto★
    - _Controls whether or not the probe filter is enabled. Has no effect on parts where the probe filter is fuse disabled._
- [select] **Memory interleaving** — None / Channel / Die / Socket / Auto★
    - _Controls fabric level memory interleaving (AUTO, none, channel, die, socket). Note that channel, die, and socket has requirements on memory populations and i..._
- [select] **Memory interleaving size** — 256 Bytes / 512 Bytes / 1 KB / 2 KB / Auto★
    - _Controls the memory interleaving size. The valid values are AUTO, 256 bytes, 512 bytes, 1 Kbytes or 2Kbytes. This determines the starting address of the inte..._
- [select] **Channel interleaving hash** — Disabled / Enabled / Auto★
    - _Controls whether or not the address bits are hashed during channel interleave mode. This field should not be used unless the interleaving is set to channel a..._
- [select] **DF C-state control** — Disabled / Enabled / Auto★
    - _Enable / disable DF C-states (DF::CstateControl[DfCstateDisable])_
- [select] **xGMI DLWM control** — Disabled / Enabled / Auto★
    - _Controls xGMI dynamic link width management feature._
- [select] **Freeze DF module queues on error** — Disabled / Enabled / Auto★

## DRAM Controller Configuration  (3 settings)

- [select] **Cmd2T** — 1T / 2T / Auto★
    - _Select between 1T and 2T mode on ADDR/CMD_
- [select] **Gear Down Mode** — Disabled / Enabled / Auto★
    - _No help string_
- [select] **Data Mask** — Auto★ / Enabled / Disabled
    - _No help string_

## DRAM Power Options  (1 settings)

- [select] **Power Down Enable** — Disabled / Enabled / Auto★
    - _Enable or disable DDR power down mode_

## CAD Bus Configuration  (9 settings)

- [select] **CAD Bus Timing User Controls** — Auto★ / Manual
    - _Setup time on CAD bus signals to Auto or Manual_
- [number] **AddrCmdSetup**
    - _Setup time on CAD bus signals. Valid values 3Fh-0h._
- [number] **CsOdtSetup**
    - _Setup time on CAD bus signals. Valid values 3Fh-0h._
- [number] **CkeSetup**
    - _Setup time on CAD bus signals. Valid values 3Fh-0h._
- [select] **CAD Bus Drive Strength User Controls** — Auto★ / Manual
    - _Drive Strength on CAD bus signals to Auto or Manual_
- [select] **ClkDrvStren** — Auto★ / 120.0 Ohm / 60.0 Ohm / 40.0 Ohm / 30.0 Ohm / 24.0 Ohm / 20.0 Ohm
    - _No help string_
- [select] **AddrCmdDrvStren** — Auto★ / 120.0 Ohm / 60.0 Ohm / 40.0 Ohm / 30.0 Ohm / 24.0 Ohm / 20.0 Ohm
    - _No help string_
- [select] **CsOdtDrvStren** — Auto★ / 120.0 Ohm / 60.0 Ohm / 40.0 Ohm / 30.0 Ohm / 24.0 Ohm / 20.0 Ohm
    - _No help string_
- [select] **CkeDrvStren** — Auto★ / 120.0 Ohm / 60.0 Ohm / 40.0 Ohm / 30.0 Ohm / 24.0 Ohm / 20.0 Ohm
    - _No help string_

## Data Bus Configuration  (4 settings)

- [select] **Data Bus Configuration User Controls** — Auto★ / Manual
    - _Specify the mode for drive strength to Auto or Manual_
- [select] **RttNom** — Rtt_Nom Disable / RZQ/4 / RZQ/2 / RZQ/6 / RZQ/1 / RZQ/5 / RZQ/3 / RZQ/7 / Auto★
    - _No help string_
- [select] **RttWr** — Dynamic ODT Off / RZQ/2 / RZQ/1 / Hi-Z / RZQ/3 / Auto★
    - _No help string_
- [select] **RttPark** — Rtt_PARK Disable / RZQ/4 / RZQ/2 / RZQ/6 / RZQ/1 / RZQ/5 / RZQ/3 / RZQ/7 / Auto★
    - _No help string_

## Common RAS  (1 settings)

- [select] **Data Poisoning** — Disabled / Enabled / Auto★
    - _ Enable/disable data poisoning: UMC_CH::EccCtrl[UcFatalEn] UMC_CH::EccCtrl[WrEccEn] Should be enabled/disabled together._

## ECC Configuration  (2 settings)

- [select] **DRAM ECC Symbol Size** — x4 / x8 / Auto★
    - _DRAM ECC Symbol Size (x4/x8) - UMC_CH::EccCtrl[EccSymbolSize]_
- [select] **DRAM ECC Enable** — Disabled / Enabled / Auto★
    - _Use this option to enable / disable DRAM ECC. Auto will set ECC to enable._

## Security  (3 settings)

- [select] **TSME** — Disabled★ / Enabled / Auto
    - _Transparent SME: AddrTweakEn = 1; ForceEncrEn =0; DataEncrEn = 1_
- [select] **Password on Boot:** — Enabled / Disabled★
- [select] **Change TPM (TCM) State:** — No Change★ / Enable & Active / Deactive & Disable / Enabled / Disabled

## DRAM Memory Mapping  (5 settings)

- [select] **Chipselect Interleaving** — Disabled / Auto★
    - _Interleave memory blocks across the DRAM chip selects for node 0._
- [select] **BankGroupSwap** — APU / CPU / Disabled / Auto★
    - _No help string_
- [select] **BankGroupSwapAlt** — Enabled / Disabled / Auto★
    - _No help string_
- [select] **Address Hash Bank** — Disabled / Enabled / Auto★
    - _Enable or disable bank address hashing_
- [select] **Address Hash CS** — Auto★ / Enabled / Disabled
    - _Enable or disable CS address hashing_

## Memory MBIST  (4 settings)

- [select] **MBIST Enable** — Auto★ / Disabled / Enabled
    - _Enable or disable Memory MBIST_
- [select] **MBIST Test Mode** — Auto★ / Interface Mode / Data Eye Mode
    - _Select MBIST Test Mode -Interface Mode (Tests Single and Multiple CS transactions and Basic Connectivity) or Data Eye Mode (Measures Voltage vs. Timing)_
- [select] **MBIST Aggressors** — Auto★ / Disabled / Enabled
    - _Enable or disable MBIST Aggressor test_
- [select] **MBIST Per Bit Slave Die Reporting** — Auto★ / Disabled / Enabled
    - _Reports 2D Data Eye Results in ABL Log for each DQ, Chipselect, and Channel_

## NBIO Common Options  (3 settings)

- [select] **System Configuration** — 12W POR Configuration - 1 Commercial/Consumer / 15W POR Configuration - 2 Commercial/Consumer / 25W POR Configuration - 3 Commercial/Consumer / 35W POR Configuration - 4 Consumer★ / 45W POR Configuration - 5 Consumer / 54W POR Configuration - 6 Consumer / 35W POR Configuration - 7 Embedded / 45W POR Configuration - 8 Embedded / 54W POR Configuration - 9 Embedded / Auto
- [select] **Audio IOs** — Auto / MAX HDA / MIN SoundWire / MAX mHDA / MIN SoundWire / MAX SoundWire / MIN HDA★ / MAX SoundWire / MIN mHDA / I2S/TDM / DISABLE AUDIO IOs / Soundwire
    - _Audio IOs control_
- [select] **System Temperature Tracking** — Auto★ / Disable / Enable
    - _System Temperature Tracking [0 = disabled; 1 = enabled]_

## GFX Configuration  (6 settings)

- [select] **Integrated Graphics Controller** — Disabled / Forces / Auto★
    - _Enable Integrated Graphics controller_
- [select] **UMA Mode** — Auto★ / UMA_SPECIFIED / UMA_AUTO
- [select] **UMA Version** — Legacy / Non-Legacy / Hybrid Secure / Auto★
- [select] **Display Resulotuon** — 1920x1080 and below / 2560x1600 / 3840x2160 / Auto★
    - _Display Resolution_
- [select] **UMA Frame buffer Size** — Auto★ / 64M / 128M / 256M / 384M / 512M / 80M / 96M / 768M / 1G / 2G / 3G / 4G / 8G / 16G
    - _Set UMA FB size_
- [select] **NB Azalia** — Disabled / Enabled / Auto★
    - _Enable Integrate HD Audio controller_

## NB Configuration  (1 settings)

- [select] **IOMMU** — Disabled / Enabled / Auto★
    - _Enable/Disable IOMMU_

## PCIe Configuration  (1 settings)

- [select] **PSPP Policy** — Disabled / Performance / Balanced / Power Saving / Auto★
    - _No help string_

## Fan Control  (14 settings)

- [select] **Fan Control** — Manual / Auto★
- [select] **Force PWM Control** — Force / Unforce★
- [number] **Force PWM**
    - _Specify the PWM to force the fan to [0-100]_
- [select] **Fan Table Control** — Manual / Auto★
- [number] **Low Temperature**
    - _Low Temperature ['C]_
- [number] **Medium Temperature**
    - _Medium Temperature ['C]_
- [number] **High Temperature**
    - _High Temperature ['C]_
- [number] **Critical Temperature**
    - _Critical Temperature ['C]_
- [number] **Low Pwm**
    - _Low Pwm [0-100]_
- [number] **Medium Pwm**
    - _Medium Pwm [0-100]_
- [number] **High Pwm**
    - _High Pwm [0-100]_
- [number] **Temperature Hysteresis**
    - _Temperature Hysteresis ['C]_
- [select] **Pwm Frequency** — 100Hz / 25kHz★
- [select] **Fan Polarity** — Negative★ / Positive

## SATA Configuration Options  (6 settings)

- [select] **SATA Controller** — Disabled / Enabled / Auto★
    - _Disable or enable OnChip SATA controller_
- [select] **SATA Mode** — AHCI / AHCI as ID 0x7904 / Auto★ / RAID
    - _Select OnChip SATA Type. Don't select RAID for Raven FP5 platform. Raven FP5 doesn't support RAID._
- [select] **Sata RAS Support** — Disabled / Enabled / Auto★
    - _Disable or enable Sata RAS Support_
- [select] **Sata Disabled AHCI Prefetch Function** — Disabled / Enabled / Auto★
    - _Disable or enable Sata Disabled AHCI Prefetch Function_
- [select] **Aggresive SATA Device Sleep Port 0** — Disable / Enable / Auto★
    - _No help string_
- [select] **Aggresive SATA Device Sleep Port 1** — Disable / Enable / Auto★
    - _No help string_

## USB Configuration Options  (2 settings)

- [select] **XHCI0 controller enable** — Enabled / Disabled / Auto★
    - _Enable or disable USB3 controller._
- [select] **XHCI1 controller enable** — Enabled / Disabled / Auto★
    - _Enable or disable USB3 controller._

## Ac Power Loss Options  (1 settings)

- [select] **Ac Loss Control** — Always Off★ / Always On / Reserved / Previous
    - _Select Ac Loss Control Method_

## I2C Configuration Options  (6 settings)

- [select] **I2C 0 Enable** — Disabled / Enabled / Auto★
    - _No help string_
- [select] **I2C 1 Enable** — Disabled / Enabled / Auto★
    - _No help string_
- [select] **I2C 2 Enable** — Disabled / Enabled / Auto★
    - _No help string_
- [select] **I2C 3 Enable** — Disabled / Enabled★ / Auto
    - _No help string_
- [select] **I2C 4 Enable** — Disabled / Enabled / Auto★
    - _No help string_
- [select] **I2C 5 Enable** — Disabled / Enabled / Auto★
    - _No help string_

## Uart Configuration Options  (8 settings)

- [select] **Uart 0 Enable** — Disabled / Enabled / Auto★
    - _Uart 0 has no HW FC if Uart 2 is enabled_
- [select] **Uart 0 Legacy Options** — Disabled / 0x2E8 / 0x2F8 / 0x3E8 / 0x3F8 / Auto★
    - _No help string_
- [select] **Uart 1 Enable** — Disabled / Enabled / Auto★
    - _Uart 1 has no HW FC if Uart 3 is enabled_
- [select] **Uart 1 Legacy Options** — Disabled / 0x2E8 / 0x2F8 / 0x3E8 / 0x3F8 / Auto★
    - _No help string_
- [select] **Uart 2 Enable (no HW FC)** — Disabled / Enabled / Auto★
    - _No help string_
- [select] **Uart 2 Legacy Options** — Disabled / 0x2E8 / 0x2F8 / 0x3E8 / 0x3F8 / Auto★
    - _No help string_
- [select] **Uart 3 Enable (no HW FC)** — Disabled / Enabled / Auto★
    - _No help string_
- [select] **Uart 3 Legacy Options** — Disabled / 0x2E8 / 0x2F8 / 0x3E8 / 0x3F8 / Auto★
    - _No help string_

## ESPI Configuration Options  (1 settings)

- [select] **ESPI Enable** — Disabled / Enabled / Auto★
    - _No help string_

## XGBE Configuration Options  (2 settings)

- [select] **XGBE0 enable** — Enabled / Disabled / Auto★
    - _Enable or disable Ethernet controller._
- [select] **XGBE1 enable** — Enabled / Disabled / Auto★
    - _Enable or disable Ethernet controller._

## eMMC Options  (4 settings)

- [select] **eMMC/SD Configure** — Disabled / SD Normal Speed / SD High Speed / SD UHSI-SDR50 / SD UHSI-DDR50 / SD UHSI-SDR104 / eMMC Emmc Backward Compatibility / eMMC High Speed SDR / eMMC High Speed DDR / eMMC HS200 / eMMC HS400 / eMMC HS300 / Auto★
    - _No help string_
- [select] **Driver Type** — AMD eMMC Driver / MS Driver / MS eMMC Driver / Auto★
    - _Bios will select MS driver for SD selections._
- [select] **D3 Cold Support** — Disabled / Enabled / Auto★
    - _No help string_
- [select] **eMMC Boot** — Disabled / Enabled / Auto★
    - _No help string_

## LPC Options  (1 settings)

- [select] **LPC Clock Run control** — Disabled / Enabled / Auto★
    - _No help string_

## System Control  (1 settings)

- [select] **Toggle All PwrGood On Cf9** — Disabled / Enabled / Auto★
    - _No help string_

## X509_SHA256  (6 settings)

- [select] **Restore all of the Secure Boot Settings to default factory settings and enable Secure Boot.** — Disabled / Enabled / Operation is completed. System will reset!!
    - _Restore all of the secure boot Settings to backup factory settings and enable Secure Boot._
- [select] **Add this hash image to allowed database (db)**
    - _Exit saving changes_
- [select] **Cannot find file!!** — Delete KEK★ / Enter into Delete KEK Form / DB Options / Enroll/Delete Signature / DB Signature List:
    - _File format is incorrect!!_
- [select] **Select Secure Mode** — Unknown / RSA2048_SHA256
    - _Select different secure boot mode. User can select one of 4 different modes (Setup Mode, User Mode, Audit mode and Deployed mode)._
- [select] **Enter into Delete PK Form** — Unknown★ / RSA2048_SHA256
    - _Enroll/Delete KEK_
- [number] **KEK Signature List:**
    - _Enroll KEK Using File_

## Select Signature Format  (6 settings)

- [select] **Restore Secure Boot to Backup Settings** — Disabled / Enabled / This isn't a vaild EFI image. Please select another file!!
    - _Restore all of the secure boot Settings to backup factory settings and enable Secure Boot._
- [select] **Exit Discarding Change**
    - _Exit saving changes_
- [select] **File size is too large!!** — DBX Options★ / Enroll/Delete DBX / DBX Signature List: / Enroll Signature / Delete Signature
    - _File format is incorrect!!_
- [select] **PK Options** — Unknown / RSA2048_SHA256
    - _Enroll/Delete PK_
- [select] **KEK Options** — Unknown★ / RSA2048_SHA256
    - _Enroll/Delete KEK_
- [number] **Enroll KEK**
    - _Enroll KEK Using File_

## iSCSI ファースト ターゲット パラメタ  (3 settings)

- [select] **接続** — 無効★ / 有効
    - _ターゲットの確立をイネーブル/ディスエーブルする。_
- [number] **TCP ポート**
    - _ターゲット TCP ポート番号を設定する (1 ～ 65535)。_
- [number] **ブート LUN**
    - _ターゲット ブート LUN 番号を設定する (0 ～ 255)。_

## iSCSI セカンド ターゲット パラメタ  (3 settings)

- [select] **接続** — 無効★ / 有効
    - _ターゲットの確立をイネーブル/ディスエーブルする。_
- [number] **TCP ポート**
    - _ターゲット TCP ポート番号を設定する (1 ～ 65535)。_
- [number] **ブート LUN**
    - _ターゲット ブート LUN 番号を設定する (0 ～ 255)。_

## MBA コンフィギュレーション メニュー  (10 settings)

- [select] **オプション ROM** — 無効 / 有効★
    - _ブート オプション ROM をイネーブル/ディスネーブルする_
- [select] **旧式ブート プロトコル** — PXE / iSCSI / ナシ
    - _UEFI 以外のブート プロトコルを選択：Preboot Execution Environment (PXE)/iSCSI。_
- [select] **ブート ストラップのタイプ** — 自動検出★ / BBS / Int 18h / Int 19h
    - _ブート ストラップのタイプを選択する。_
- [select] **セットアップ プロンプトを隠す** — 無効★ / 有効
    - _ROM の初期化中にセットアップ プロンプトを表示するかどうかを設定する。_
- [select] **キー操作のセットアップ** — Ctrl-S★ / Ctrl-B
    - _コンフィギュレーション メニューを呼び出すキー操作を設定する。_
- [number] **バナー メッセージのタイムアウト**
    - _タイムアウト値を選択する。(0 はデフォルトの 4 秒、15 は遅延なし、1 ～ 14 は秒単位のタイムアウト値)_
- [select] **リンク速度** — 自動ネゴシエーション★ / 10 Mbps 半二重 / 10 Mbps 全二重 / 100 Mbps 半二重 / 100 Mbps 全二重
    - _リンク速度を設定する。_
- [select] **プリブート Wake On LAN** — 無効 / 有効
    - _プリブート Wake on LAN (WOL) を設定する。_
- [select] **VLAN モード** — 無効★ / 有効
    - _仮想 LAN モードを設定する。_
- [number] **VLAN ID (1..4094)**
    - _バーチャル LAN ID (1..4094) を構成します。_

## セカンダリ デバイス  (2 settings)

- [select] **独立したターゲット ポータルを使用** — 無効★ / 有効
    - _multipath I/O がイネーブルな場合、独立したターゲット ポータルを使用する。_
- [select] **独立したターゲット名を使用** — 無効★ / 有効
    - _multipath I/O がイネーブルな場合、独立したターゲット名を使用する。_

## iSCSI セカンダリ デバイス パラメタ  (2 settings)

- [select] **独立したターゲット ポータルを使用** — 無効★ / 有効
    - _multipath I/O がイネーブルな場合、独立したターゲット ポータルを使用する。_
- [select] **独立したターゲット名を使用** — 無効★ / 有効
    - _multipath I/O がイネーブルな場合、独立したターゲット名を使用する。_

## NICの設定  (10 settings)

- [select] **オプション ROM** — 無効 / 有効
    - _ブート オプション ROM をイネーブル/ディスネーブルする_
- [select] **旧式ブート プロトコル** — PXE / iSCSI / ナシ
    - _UEFI 以外のブート プロトコルを選択：Preboot Execution Environment (PXE)/iSCSI。_
- [select] **ブート ストラップのタイプ** — 自動検出★ / BBS / Int 18h / Int 19h
    - _ブート ストラップのタイプを選択する。_
- [select] **セットアップ プロンプトを隠す** — 無効★ / 有効
    - _ROM の初期化中にセットアップ プロンプトを表示するかどうかを設定する。_
- [select] **キー操作のセットアップ** — Ctrl-S★ / Ctrl-B
    - _コンフィギュレーション メニューを呼び出すキー操作を設定する。_
- [number] **バナー メッセージのタイムアウト**
    - _タイムアウト値を選択する。(0 はデフォルトの 4 秒、15 は遅延なし、1 ～ 14 は秒単位のタイムアウト値)_
- [select] **リンク速度** — 自動ネゴシエート済み★ / 10 Mbps 半二重 / 10 Mbps 全二重 / 100 Mbps 半二重 / 100 Mbps 全二重
    - _リンク速度を設定する。_
- [select] **Wake On LAN** — 無効 / 有効
    - _Wake on LAN (WOL) を構成します。_
- [select] **仮想 LAN** — 無効★ / 有効
    - _仮想 LAN モードを設定する。_
- [number] **バーチャル LAN ID**
    - _バーチャル LAN ID (1..4094) を構成します。_

## Page de configuration principale  (5 settings)

- [select] **Désactiver la fonction de mémoire partagée HP** — Désactivé / Activé★
    - _Désactiver l'utilisation de régions de mémoire réservée pour permettre l'affectation directe de périphérique pour les ordinateurs virtuels invités._
- [number] **Clignotement des voyants**
    - _Fait clignoter les voyants pendant une durée de 15 secondes._
- [select] **Réveil sur LAN au pré-démarrage** — Désactivé / Activé
    - _Configurer le réveil sur LAN au pré-démarrage._
- [select] **Etat de la liaison** — Déconnecté / Connecté
- [select] **Paramètres de la première cible iSCSI** — Adresse MAC / Adresse MAC permanente★

## Paramètres généraux iSCSI  (14 settings)

- [select] **Paramètres TCP/IP via DHCP** — Désactivé / Activé★
    - _Acquérir la configuration TCP/IP via DHCP._
- [select] **Configuration IP automatique** — Désactivé / Activé★
    - _Acquérir la configuration TCP/IP via la configuration automatique avec état ou sans état._
- [select] **Configuration automatique de l'IP** — Désactivé / Activé★
    - _Acquérir la configuration TCP/IP via la configuration automatique avec état ou sans état._
- [select] **Paramètres iSCSI via DHCP** — Désactivé / Activé★
    - _Acquérir les paramètres iSCSI via DHCP._
- [select] **Authentification CHAP** — Désactivé★ / Activé
    - _Activer/Désactiver l'authentification CHAP._
- [select] **Démarrer depuis la cible iSCSI** — Désactivé / Activé★ / Désactivé une fois
    - _Activer/Désactiver le démarrage depuis la cible iSCSI après l'ouverture de la session._
- [select] **Démarrer depuis la cible** — Désactivé / Activé★ / Désactivé une fois
    - _Activer/Désactiver le démarrage depuis la cible iSCSI après l'ouverture de la session._
- [number] **Durée d'établissement de la liaison**
    - _Configurer la durée d'établissement de la liaison en secondes (0 à 255)._
- [select] **Utiliser l'horodatage TCP** — Désactivé★ / Activé
    - _Activer/Désactiver l'horodatage TCP._
- [select] **Horodatage TCP** — Désactivé★ / Activé
    - _Activer/Désactiver l'horodatage TCP._
- [select] **Cibler comme premier disque dur** — Désactivé★ / Activé
    - _Activer/Désactiver l'apparition de la cible comme premier disque dur dans le système._
- [number] **Nombre d'essais de connexion à une unité logique occupée**
    - _Configurer le nombre d'essais à 2 secondes d'intervalle lorsque l'unité logique est occupée (0 à 60)._
- [select] **IP Version** — IPv4★ / IPv6
    - _Prise en charge d'IP Version. La modification de ce paramètre réinitialisera tous les champs relatifs à l'adresse IP._
- [select] **Paramètres de la première cible iSCSI** — Adresse MAC / Adresse MAC permanente★

## Paramètres de l'initiateur iSCSI  (1 settings)

- [select] **Paramètres de la première cible iSCSI** — Adresse MAC / Adresse MAC permanente★

## Paramètres de la première cible iSCSI  (3 settings)

- [select] **Connecter** — Désactivé★ / Activé
    - _Activer/Désactiver l'établissement de la cible._
- [number] **Port TCP**
    - _Configurer le numéro du port TCP de la cible (1 à 65 535)._
- [number] **Unité logique de démarrage**
    - _Configurer le numéro d'unité logique de démarrage cible (0 à 255)._

## Paramètres de la deuxième cible iSCSI  (3 settings)

- [select] **Connecter** — Désactivé★ / Activé
    - _Activer/Désactiver l'établissement de la cible._
- [number] **Port TCP**
    - _Configurer le numéro du port TCP de la cible (1 à 65 535)._
- [number] **Unité logique de démarrage**
    - _Configurer le numéro d'unité logique de démarrage cible (0 à 255)._

## Menu de configuration MBA  (10 settings)

- [select] **ROM en option** — Désactivé / Activé★
    - _Activer/Désactiver la ROM en option d'initialisation_
- [select] **Protocole de démarrage hérité** — PXE / iSCSI / NONE
    - _Sélectionner un protocole de démarrage non UEFI : environnement d'exécution pré-démarrage (PXE)/iSCSI._
- [select] **Type d'amorçage** — Détecter automatiquement★ / BBS / Int 18h / Int 19h
    - _Sélectionner le type d'amorçage._
- [select] **Masquer l'invite de configuration** — Désactivé★ / Activé
    - _Configurer l'affichage de l'invite de configuration pendant l'initialisation de la ROM._
- [select] **Configurer la séquence de touches** — Ctrl-S★ / Ctrl-B
    - _Configurer la séquence de touches permettant d'appeler le menu de configuration._
- [number] **Délai d'inactivité du message de bannière**
    - _Sélectionner une valeur pour le délai d'inactivité. (0 : par défaut, 4 secondes ; 15 : aucun délai ; 1-14 : valeur du délai d'inactivité en secondes)_
- [select] **Vitesse de liaison** — Autonégociation★ / 10 Mbit/s, semi / 10 Mbit/s, intégral / 100 Mbit/s, semi / 100 Mbit/s, intégral
    - _Configurer la vitesse de liaison._
- [select] **Réveil sur LAN au pré-démarrage** — Désactivé / Activé
    - _Configurer le réveil sur LAN au pré-démarrage._
- [select] **Mode VLAN** — Désactivé★ / Activé
    - _Configurer le mode VLAN._
- [number] **ID de VLAN (1 à 4094)**
    - _Configurer l'ID de VLAN (1 à 4094)._

## Périphérique secondaire  (2 settings)

- [select] **Utiliser le portail cible indépendant** — Désactivé★ / Activé
    - _Utiliser le portail cible indépendant lorsque les E/S multivoies sont activées._
- [select] **Utiliser le nom de cible indépendante** — Désactivé★ / Activé
    - _Utiliser le nom de cible indépendante lorsque les E/S multivoies sont activées._

## Paramètres iSCSI du périphérique secondaire  (2 settings)

- [select] **Utiliser le portail cible indépendant** — Désactivé★ / Activé
    - _Utiliser le portail cible indépendant lorsque les E/S multivoies sont activées._
- [select] **Utiliser le nom de cible indépendante** — Désactivé★ / Activé
    - _Utiliser le nom de cible indépendante lorsque les E/S multivoies sont activées._

## Configuration de la carte réseau  (10 settings)

- [select] **ROM en option** — Désactivé / Activé
    - _Activer/Désactiver la ROM en option d'initialisation_
- [select] **Protocole de démarrage hérité** — PXE / iSCSI / None
    - _Sélectionner un protocole de démarrage non UEFI : environnement d'exécution pré-démarrage (PXE)/iSCSI._
- [select] **Type d'amorçage** — Détecter automatiquement★ / BBS / Int 18h / Int 19h
    - _Sélectionner le type d'amorçage._
- [select] **Masquer l'invite de configuration** — Désactivé★ / Activé
    - _Configurer l'affichage de l'invite de configuration pendant l'initialisation de la ROM._
- [select] **Configurer la séquence de touches** — Ctrl-S★ / Ctrl-B
    - _Configurer la séquence de touches permettant d'appeler le menu de configuration._
- [number] **Délai d'inactivité du message de bannière**
    - _Sélectionner une valeur pour le délai d'inactivité. (0 : par défaut, 4 secondes ; 15 : aucun délai ; 1-14 : valeur du délai d'inactivité en secondes)_
- [select] **Vitesse de liaison** — Négociation automatique★ / 10 Mbit/s, semi / 10 Mbit/s, intégral / 100 Mbit/s, semi / 100 Mbit/s, intégral
    - _Configurer la vitesse de liaison._
- [select] **Réveil sur LAN** — Désactivé / Activé
    - _Configurer le réseau local de réveil._
- [select] **Mode VLAN** — Désactivé★ / Activé
    - _Configurer le mode VLAN._
- [number] **ID de VLAN**
    - _Configurer l'ID de VLAN (1 à 4094)._

## Nicht genügend Speicherplatz, um das Bild zu speichern.  (18 settings)

- [select] **MBA-Konfigurationsmenü** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
- [select] **Management FW** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Hauptkonfigurationsseite** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Allgemeine iSCSI-Parameter_
- [select] **Allgemeine iSCSI-Parameter** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Allgemeine iSCSI-Bootparameter konfigurieren.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Initiator-iSCSI-Parameter_
- [select] **Initiator-iSCSI-Parameter** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Initiator-iSCSI-Parameter konfigurieren.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Erste iSCSI-Zielparameter_
- [select] **Sekundäres Gerät** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Parameter des sekundären Geräts konfigurieren._
- [select] **iSCSI-Parameter des sekundären Geräts** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Parameter des sekundären Geräts konfigurieren.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Option ROM** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Boot Option ROM aktivieren/deaktivieren** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Auto Erkennung_
- [select] **BBS** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Int. 18 Std._
- [select] **Int. 19 Std.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Eingabeaufforderung ausblenden_
- [select] **Eingabeaufforderung ausblenden** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Konfigurieren, ob die Eingabeaufforderung während der ROM-Initialisierung angezeigt wird._
- [select] **Tastenanschlag eingeben** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Tastenanschläge konfigurieren, um das Konfigurationsmenü aufzurufen.** — Strg-B / Banner-Nachricht Zeitüberschreitung★
    - _Strg-S_
- [select] **iSCSI-Boot-Konfigurationsmenü** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _iSCSI-Bootparameter konfigurieren._

## Boot LUN  (2 settings)

- [select] **Configure target boot LUN number (0..255).** — Input secondary device MAC address. Use XX:XX:XX:XX:XX:XX format.★ / Secondary Device MAC Address
    - _Secondary Device_
- [select] **Configure CHAP ID (up to 32 characters in length).** — ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★ / ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configure CHAP ID (up to 128 characters in length)._

## Controls IO based C-state generation and DF C-states.  (2 settings)

- [select] **ONE** — THREE / SMTEN★ / DRAM scrub time / Provide a value that is the number of hours to scrub memory. / 1 hour / 4 hours / 8 hours
    - _TWO_
- [toggle] **Normal Operation**
    - _OC1_

## OC Mode  (6 settings)

- [select] **48 hours** — DF Common Options / UMC Common Options★
    - _Redirect scrubber control_
- [select] **Control DF::RedirScrubCtrl[EnRedirScrub]** — DF Common Options / UMC Common Options★
    - _Disable DF sync flood propagation_
- [select] **Control DF::PIEConfig[DisSyncFloodProp]** — DF Common Options / UMC Common Options★
    - _Sync flood disabled_
- [select] **Sync flood enabled** — DF Common Options / UMC Common Options★
    - _GMI encryption control_
- [select] **Control GMI link encryption** — DF Common Options / UMC Common Options★
    - _xGMI encryption control_
- [select] **400MHz** — DF Common Options / UMC Common Options★
    - _533MHz_

## CC6 memory region encryption  (7 settings)

- [select] **Controls whether or not the private memory regions (PSP, SMU and CC6) are at the top of DRAM or distributed. Note that distributed requires memory on all dies. Note that it will always be at the top of DRAM if some dies don't have memory regardless of this option's setting.** — DF Common Options★ / UMC Common Options
    - _Consolidated_
- [select] **Distributed** — DF Common Options / UMC Common Options★
    - _Consolidated_
- [select] **1050MHz** — NBIO Common Options / DF Common Options★
    - _1066MHz_
- [select] **System probe filter** — DF Common Options / UMC Common Options★
    - _Controls whether or not the probe filter is enabled. Has no effect on parts where the probe filter is fuse disabled._
- [select] **None** — DF Common Options★ / Socket / Die
    - _Channel_
- [number] **Controls the memory interleaving size. The valid values are AUTO, 256 bytes, 512 bytes, 1 Kbytes or 2Kbytes. This determines the starting address of the interleave (bit 8, 9, 10 or 11).**
    - _From a workaround for GCC/C000005 issue for XV Core on CZ A0, setting MSRC001_1029 Decode Configuration (DE_CFG) bit 14 [DecfgNoRdrctForReturns] to 1_
- [select] **Memory interleaving** — DF Common Options★ / UMC Common Options
    - _Controls fabric level memory interleaving (AUTO, none, channel, die, socket). Note that channel, die, and socket has requirements on memory populations and i..._

## Control whether or not the CC6 save/restore memory is encrypted  (2 settings)

- [select] **256 Bytes** — DF Common Options / UMC Common Options★
    - _512 Bytes_
- [select] **1 KB** — DF Common Options / NBIO Common Options★
    - _2 KB_

## Will be valid on next boot  (3 settings)

- [select] **Range: 0 to 65535 seconds, 0 means no wait, 65535 means waiting for key** — Delete Boot Option★ / Add EFI Application or Removable Fs as Boot Option
    - _Boot Next Value_
- [select] **Load Option Reconnect** — Modify system boot options★ / Driver Options
    - _Commit Changes and Exit_
- [select] **Next boot use this boot option** — Modify system boot options★ / Driver Options
    - _Input the description_

## Bus:Périphérique:Fonction  (1 settings)

- [select] **Prise en charge du déchargement iSCSI** — Adresse MAC / Adresse MAC permanente★
    - _Prise en charge de l'initialisation iSCSI_

## Micrologiciel de gestion  (1 settings)

- [select] **Paramètres de la première cible iSCSI** — Adresse MAC / Adresse MAC permanente★

## Configurer les paramètres généraux iSCSI de démarrage.  (1 settings)

- [select] **Paramètres de la première cible iSCSI** — Adresse MAC / Adresse MAC permanente★

## Configurer les paramètres de l'initiateur iSCSI.  (1 settings)

- [select] **Paramètres de la première cible iSCSI** — Adresse MAC / Adresse MAC permanente★

## Etat de la liaison  (4 settings)

- [select] **Int 18h** — Adresse MAC / Délai d'inactivité du message de bannière / iqn.1995-05.com.broadcom.iscsiboot★
    - _Int 19h_
- [select] **Sélectionner une valeur pour le délai d'inactivité. (0 : par défaut, 4 secondes ; 15 : aucun délai ; 1-14 : valeur du délai d'inactivité en secondes)** — BRCM ISAN / 0.0.0.0★
- [select] **Masquer l'invite de configuration** — Adresse MAC / Adresse MAC permanente★
- [select] **100 Mbit/s, semi** — Adresse MAC
    - _100 Mbit/s, intégral_

## Déconnecté  (6 settings)

- [select] **SMASH** — Adresse MAC
    - _CCM_
- [select] **IPv4** — IPv6 / Menu de configuration MBA★
    - _Menu de configuration du démarrage iSCSI_
- [select] **100 Mbit/s, intégral** — Activé★ / Désactivé une fois
    - _Désactivé_
- [select] **Configurer les paramètres de démarrage iSCSI.** — Adresse MAC★ / Adresse MAC permanente
    - _Configuration iSCSI_
- [select] **Configuration iSCSI** — Adresse MAC / Adresse MAC permanente★
    - _Menu Image de micrologiciel_
- [select] **Menu Image de micrologiciel** — Adresse MAC / Adresse MAC permanente★
    - _Informations sur l'image du microprogramme ._

## Fait clignoter les voyants pendant une durée de 15 secondes.  (2 settings)

- [select] **Configurer les paramètres du périphérique secondaire.** — Adresse MAC / Adresse MAC permanente★
    - _Paramètres iSCSI du périphérique secondaire_
- [select] **Paramètres iSCSI du périphérique secondaire** — ROM en option★
    - _Configurer les paramètres du périphérique secondaire._

## Protocole de démarrage hérité  (28 settings)

- [select] **ASF** — Adresse MAC / Adresse MAC permanente★
    - _NC-SI_
- [select] **Préfixe du masque de sous-réseau** — Adresse MAC permanente / Configurer la clé secrète CHAP (12 à 16 caractères).★
    - _Configurer la longueur du préfixe du masque de sous-réseau de l'adresse IP._
- [select] **Passerelle par défaut** — Adresse MAC / Adresse MAC permanente★
    - _Configurer l'adresse IP de la passerelle par défaut._
- [select] **Masque de sous-réseau** — Adresse MAC / Adresse MAC permanente★
    - _Configurer le masque du sous-réseau de l'adresse IP._
- [select] **CCM** — Adresse MAC / Adresse MAC permanente★
    - _UMP_
- [select] **EFI** — Adresse MAC / Adresse MAC permanente★
- [select] **Fcode** — Adresse MAC / Adresse MAC permanente★
- [select] **Version du BIOS du contrôleur** — Adresse MAC / Adresse MAC permanente★
- [select] **MBA** — Adresse MAC / Adresse MAC permanente★
- [select] **Initialisation iSCSI** — Adresse MAC / Adresse MAC permanente★
- [select] **Sélectionner le type d'amorçage.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Vitesse de liaison_
- [select] **Vitesse de liaison** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Configurer la vitesse de liaison._
- [select] **Configurer les paramètres MBA.** — Configuration de la carte réseau★
    - _Configuration de la carte réseau_
- [select] **Mode VLAN** — ID de VLAN (1 à 4094)★ / ID de VLAN
    - _Configurer le mode VLAN._
- [select] **10 Mbit/s, intégral** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _100 Mbit/s, semi_
- [select] **100 Mbit/s, intégral** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Désactivé_
- [select] **Activé** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Désactivé une fois_
- [select] **IPv4** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _IPv6_
- [select] **Configurer l'ID de VLAN (1 à 4094).** — 10 Mbit/s, semi★ / 10 Mbit/s, intégral
    - _Autonégociation_
- [select] **100 Mbit/s, semi** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _100 Mbit/s, intégral_
- [select] **Négociation automatique** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _10 Mbit/s, semi_
- [select] **Réveil sur LAN au pré-démarrage** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configurer le réveil sur LAN au pré-démarrage._
- [select] **Paramètres de la première cible iSCSI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurer les paramètres de la première cible iSCSI.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Paramètres de la deuxième cible iSCSI_
- [select] **ID du périphérique PCI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
- [select] **Paramètres de la deuxième cible iSCSI** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
- [select] **Configurer les paramètres de la deuxième cible iSCSI.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Périphérique secondaire_
- [select] **Démarrer depuis la cible** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Activer/Désactiver le démarrage depuis la cible iSCSI après l'ouverture de la session._

## <Enter>=￱選択￰  (1 settings)

- [select] **Press 'Y' to save and exit, 'N' to discard and exit.**
    - _InsydeH2O ￱セットアップユーティリティ￰_

## Esc=￱入力を終了します￰  (5 settings)

- [select] **￱はい￰** — ￱いいえ￰
    - _￱ヘルプ￰_
- [select] **￱無効なパスワード￰!￱パスワード設定のために新しい文字列を入力してください。￰** — ￱オーケー￰★ / ￱取消￰
    - _￱変更を保存して終了￰_
- [select] **↑↓**
    - _￱アイテム選択￰_
- [select] **F5/F6**
    - _￱数値変更￰_
- [select] **F9**
    - _￱デフォルト設定￰_

## =￱ハイライト移動￰  (1 settings)

- [toggle] **￱＜スペース＞￰ =￱選択／解除￰**
    - _￱パスワード入力￰_

## Display IPv6 network parameters.  (8 settings)

- [select] **The hardware address of the network interface.** — Host addresses    :★ / The address list which contain the local IPv6 addresses and the corresponding prefix length information. / Route Table       :
- [select] **The route table of the IPv6 network stack runs on this interface.** — Route Table       : / The address list which contain the local IPv6 addresses and the corresponding prefix length information. / Host addresses    :★
    - _Gateway addresses :_
- [select] **Current gateway IPv6 addresses.** — Current DNS server list. / Interface ID / Host addresses    :★
    - _DNS addresses     :_
- [select] **The 64 bit alternative interface ID for the device. The string is colon separated. e.g. ff:dd:88:66:cc:1:2:3** — The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address. A value of zero indicates that Duplicate Address Detection is not performed. / Host addresses    :★
    - _DAD Transmit Count_
- [select] **Policy** — The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address. A value of zero indicates that Duplicate Address Detection is not performed. / automatic / Host addresses    :★
    - _automatic or manual_
- [select] **manual** — Configure the interface manually. IP address, gateway address, and DNS server address can be configured.★ / New IPv6 address / Manual IP address can only be configured under manual policy. Separate the IP address with blank space to configure more than one address. e.g. 2002::1/64 2002::2/64
    - _Advanced Configuration_
- [select] **New DNS addresses** — The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address. A value of zero indicates that Duplicate Address Detection is not performed. / automatic / Host addresses    :★
    - _DNS addresses can only be configured under manual policy. e.g. 2002::4. Separate the IP address with blank space to configure more than one address._
- [select] **Save Changes and Exit** — The number of consecutive Neighbor Solicitation messages sent while performing Duplicate Address Detection on a tentative address. A value of zero indicates that Duplicate Address Detection is not performed. / automatic / Host addresses    :★
    - _Save Changes for interface ID, DAD transmit count, policy, and data in advanced configuration._

## Advanced Settings  (8 settings)

- [select] **10 Mpbs HALF Duplex** — Disabled★ / Save RealManage Configuration / Save RealManage Configuration to NvRam
    - _Enabled_
- [select] **Exit RealManage Setup** — Save RealManage Configuration to NvRam / Save RealManage Configuration / Disabled★
- [select] **Configuration Menu** — Configure Realtek ethernet controller parameter / Disabled★
    - _Advanced Settings_
- [select] **Driver Information** — Driver Name: / Disabled★
    - _Realtek UEFI UNDI driver information_
- [select] **%s** — Driver Name: / %s / Disabled★
    - _Driver Version:_
- [select] **Driver Released Date:** — Device Information★ / Device Name: / %s
    - _%s_
- [select] **%02x:%02x:%02x:%02x:%02x:%02x** — Driver Name: / %s / Disabled★
    - _PCI Slot:_
- [select] **The PCI address of Realtek ethernet controller** — Driver Name: / %s / Disabled★
    - _%02d:%02d:%02d_

## Affirmative or negative DASH fifth PKI hash value  (2 settings)

- [select] **Hash5 Value** — Certificate Hash6 for PKI / Affirmative or negative DASH sixth PKI hash value / Hash6 Value / Disabled★
    - _Set or change DASH fifth PKI hash value_
- [select] **Set or change DASH sixth PKI hash value** — Disabled★
    - _FQDN_

## Link Speed & Duplex  (1 settings)

- [select] **Set or change DASH PKI FQDN** — Driver Name: / Set or change DASH PKI DNS suffix / Please Enter Username & Password / Please Input Password / Disabled★
    - _PKI DNS Suffix_

## Adresse MAC permanente  (7 settings)

- [select] **Numéro Bus PCI:Périphérique:Numéro de fonction de ce périphérique.** — Adresse PCI / Bus:Périphérique:Fonction★
    - _Etat de la liaison_
- [select] **Etat de la liaison** — Déconnecté / Clignotement des voyants / Bus:Périphérique:Fonction★
    - _Connecté_
- [select] **Fait clignoter les voyants pendant une durée de 15 secondes.** — Protocole de démarrage hérité / Bus:Périphérique:Fonction★
    - _Protocole de démarrage hérité_
- [select] **Sélectionner un protocole de démarrage non UEFI : environnement d'exécution pré-démarrage (PXE)/iSCSI.** — Protocole de démarrage hérité / iSCSI / Bus:Périphérique:Fonction★
    - _PXE_
- [select] **NONE** — Type d'amorçage★ / Sélectionner le type d'amorçage.
    - _None_
- [select] **Configurer la vitesse de liaison.** — Protocole de démarrage hérité / iSCSI / Bus:Périphérique:Fonction★
    - _Réveil sur LAN au pré-démarrage_
- [select] **Configurer le réveil sur LAN au pré-démarrage.** — Protocole de démarrage hérité / iSCSI / Bus:Périphérique:Fonction★
    - _Réveil sur LAN_

## Configurer l'adresse IP de la passerelle par défaut.  (2 settings)

- [select] **Serveur DNS principal** — Serveur DNS secondaire / Configurer l'adresse IP du serveur DNS secondaire. / Nom iSCSI / Bus:Périphérique:Fonction★
- [select] **Configurer le nom iSCSI.** — Clignotement des voyants / Bus:Périphérique:Fonction★
    - _Nom iSCSI_

## Adresse MAC  (11 settings)

- [select] **Configurer le nom iSCSI.** — Protocole de démarrage hérité / Configurer le nom iSCSI. / Réf. CHAP / Configurer la réf. CHAP (jusqu'à 32 caractères). / Configurer la réf. CHAP (jusqu'à 128 caractères). / Bus:Périphérique:Fonction★
    - _Nom iSCSI_
- [select] **Réf. CHAP** — Protocole de démarrage hérité / iSCSI / Bus:Périphérique:Fonction★
    - _Configurer la réf. CHAP (jusqu'à 32 caractères)._
- [select] **Configurer la réf. CHAP (jusqu'à 128 caractères).** — Réf. CHAP / Configurer la réf. CHAP (jusqu'à 32 caractères). / Bus:Périphérique:Fonction★ / Protocole de démarrage hérité / iSCSI
    - _Réf. CHAP_
- [select] **Clé secrète CHAP** — Protocole de démarrage hérité / iSCSI / Bus:Périphérique:Fonction★
    - _Configurer la clé secrète CHAP (12 à 16 caractères)._
- [select] **Configurer la clé secrète CHAP (12 à 16 caractères).** — Clé secrète CHAP / Configurer la clé secrète CHAP (12 à 16 caractères). / Bus:Périphérique:Fonction★
    - _Clé secrète CHAP_
- [select] **Connecter** — Protocole de démarrage hérité / iSCSI / Bus:Périphérique:Fonction★ / Port TCP / Configurer le numéro du port TCP de la cible (1 à 65 535).
    - _Activer/Désactiver l'établissement de la cible._
- [select] **Unité logique de démarrage** — Unité logique de démarrage / Configurer le numéro d'unité logique de démarrage cible (0 à 255). / Périphérique secondaire / Adresse MAC du périphérique secondaire d'entrée. Utiliser le format XX:XX:XX:XX:XX:XX. / Bus:Périphérique:Fonction★
    - _Configurer le numéro d'unité logique de démarrage cible (0 à 255)._
- [select] **Adresse MAC du périphérique secondaire** — Protocole de démarrage hérité / iSCSI / Bus:Périphérique:Fonction★
    - _Utiliser le portail cible indépendant_
- [select] **Utiliser le portail cible indépendant** — Protocole de démarrage hérité / iSCSI / Bus:Périphérique:Fonction★
    - _Utiliser le portail cible indépendant lorsque les E/S multivoies sont activées._
- [select] **Utiliser le nom de cible indépendante** — Protocole de démarrage hérité / iSCSI / Bus:Périphérique:Fonction★
- [select] **Utiliser le nom de cible indépendante lorsque les E/S multivoies sont activées.** — Protocole de démarrage hérité / iSCSI / Bus:Périphérique:Fonction★
    - _Version du microprogramme famille_

## 256 Bytes  (2 settings)

- [select] **512 Bytes** — 2 KB★ / Channel interleaving hash
    - _1 KB_
- [select] **Control DF::RedirScrubCtrl[EnRedirScrub]** — 34h Clk★ / 33h Clk
    - _Disable DF sync flood propagation_

## Bus:Device:Function  (1 settings)

- [select] **iSCSI Offload Support** — MAC Address / Permanent MAC Address★
    - _iSCSI Boot Support_

## Configure iSCSI general boot parameters.  (1 settings)

- [select] **iSCSI First Target Parameters** — MAC Address / Permanent MAC Address★

## Configure iSCSI initiator parameters.  (1 settings)

- [select] **iSCSI First Target Parameters** — MAC Address / Permanent MAC Address★

## Disconnected  (6 settings)

- [select] **SMASH** — MAC Address
    - _CCM_
- [select] **IPv4** — IPv6 / MBA Configuration Menu★
    - _iSCSI Boot Configuration Menu_
- [select] **100 Mbps Full** — Enabled★ / One Time Disabled
    - _Disabled_
- [select] **Configure iSCSI boot parameters.** — MAC Address★ / Permanent MAC Address
    - _iSCSI Configuration_
- [select] **iSCSI Configuration** — MAC Address / Permanent MAC Address★
    - _Firmware Image Menu_
- [select] **Firmware Image Menu** — MAC Address / Permanent MAC Address★
    - _Firmware image information._

## Blink LEDs for a duration up to 15 seconds.  (2 settings)

- [select] **Configure Secondary device parameters.** — MAC Address / Permanent MAC Address★
    - _iSCSI Secondary Device Parameters_
- [select] **iSCSI Secondary Device Parameters** — Option ROM★
    - _Configure Secondary device parameters._

## Auto  (1 settings)

- [select] **0xB Clk** — DF Common Options / UMC Common Options★
    - _0xC Clk_

## Modify next boot behavior  (1 settings)

- [select] **Set COM Flow Control** — Modify system boot options / Modify boot driver options★
    - _Set COM Baud Rate_

## Modify automatic boot time-out value  (5 settings)

- [select] **7200** — 4800 / 2400★
    - _300_
- [select] **57600** — 19200★ / 9600
    - _38400_
- [select] **150** — Modify system boot options★ / Driver Options
    - _134_
- [select] **110** — Modify system boot options / Driver Options★
    - _75_
- [select] **50** — Modify system boot options / Driver Options★
    - _5_

## Configure default gateway IP address.  (2 settings)

- [select] **Primary DNS** — Secondary DNS / Configure secondary DNS IP address. / iSCSI Name / Bus:Device:Function★
    - _Configure primary DNS IP address._
- [select] **Configure iSCSI name.** — Blink LEDs / Bus:Device:Function★
    - _iSCSI Name_

## MAC Address  (11 settings)

- [select] **Configure iSCSI name.** — Legacy Boot Protocol / Configure iSCSI name. / CHAP ID / Configure CHAP ID (up to 32 characters in length). / Configure CHAP ID (up to 128 characters in length). / Bus:Device:Function★
    - _iSCSI Name_
- [select] **CHAP ID** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★
    - _Configure CHAP ID (up to 32 characters in length)._
- [select] **Configure CHAP ID (up to 128 characters in length).** — CHAP ID / Configure CHAP ID (up to 32 characters in length). / Bus:Device:Function★ / Legacy Boot Protocol / iSCSI
    - _CHAP ID_
- [select] **CHAP Secret** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★
    - _Configure CHAP Secret (12 to 16 characters in length)._
- [select] **Configure CHAP Secret (12 to 16 characters in length).** — CHAP Secret / Configure CHAP Secret (12 to 16 characters in length). / Bus:Device:Function★
    - _CHAP Secret_
- [select] **Connect** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★ / TCP Port / Configure target TCP port number (1..65535).
    - _Enable/Disable target establishment._
- [select] **Boot LUN** — Boot LUN / Configure target boot LUN number (0..255). / Secondary Device / Input secondary device MAC address. Use XX:XX:XX:XX:XX:XX format. / Bus:Device:Function★
    - _Configure target boot LUN number (0..255)._
- [select] **Secondary Device MAC Address** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★
    - _Use Independent Target Portal_
- [select] **Use Independent Target Portal** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★
    - _Use independent target portal when multipath I/O is enabled._
- [select] **Use Independent Target Name** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★
- [select] **Use independent target name when multipath I/O is enabled.** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★
    - _Family Firmware Version_

## Max Speed  (1 settings)

- [select] **Current Work Protocol Ethernet** — Legacy Boot Protocol / iSCSI / Bus:Device:Function★

## 5v_ALW +100mv  (14 settings)

- [select] **Show all of AMD Firmware Version**
- [select] **Enable or disable CLK_REQ5# for M.2 SSD Slot J3704** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support.★
    - _Clock PM: CLK_REQ6_
- [select] **Enable or disable CLK_REQ6# for MXM x8 Slot J3604** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support.★
    - _Wireless LAN Recovery suppport Enable/Disable_
- [select] **Wireless LAN Recovery** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support.★
    - _Wireless LAN Recovery suppport Enable/Disable_
- [select] **MITT/WITT Selection** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support.★
    - _MITT Only_
- [select] **WITT Only** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _Both disable_
- [select] **LAN Power Enable** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support.★ / MS Resource
    - _LAN Low Power Mode_
- [select] **Enable or disable LAN Power** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support.★ / MS Resource
    - _LAN Low Power Mode_
- [number] **Enable/Disable KBC Support under OS**
    - _HDD Power Enable_
- [select] **Enable or disable the power of HDD** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _Enable or disable the power of ODD_
- [select] **ODD Power Enable** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _Enable or disable the power of ODD_
- [select] **Zero-Power ODD** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _Enable/Disable Zero-Power ODD Feature_
- [number] **SSD Power Enable**
    - _Enable or disable the power of SSD_
- [select] **SSD x2** — Auto: USB interrupt resource is controlled automatically; Enable: Enable USB current resource for MS; Disable: Disable USB current resource for MS.★ / Reduce Hardware Support
    - _SSD x4_

## Simple  (1 settings)

- [select] **Show all of AMD Firmware Version**

## StallForUnlock Enable/Disable  (4 settings)

- [select] **AmdDcTimer Setting.** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _AmdAcTimer_
- [number] **SATA/ SATA express selection  Setting.**
    - _SATA_
- [number] **VDDP voltage  Setting.**
    - _VDDP voltage (0.9V)_
- [select] **Show all of AMD Firmware Version**

## SW BreakPoint for S3 Enable/Disable  (4 settings)

- [select] **AmdAcTimer Setting.** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _SATA/ SATA express selection_
- [number] **SATA express**
    - _VDDP voltage_
- [number] **VDDP voltage (+10mv)**
    - _VDDP voltage (+20mv)_
- [select] **Show all of AMD Firmware Version**

## Wake on PME  (9 settings)

- [select] **AGESA Version** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support.★
    - _PSP BootLoader Version_
- [select] **Enable/Disable Discrete GPU Display HPD Circuitry** — Discrete GPU's Audio / Disable Discrete GPU's Audio or keep its ROM strap setting / Keep ROM Strap Setting
    - _Pulse Circuitry_
- [select] **Enable/Disable Discrete GPU BOMACO Support** — 0★ / PSP SecureOS Version / ABL Version
    - _MACO-PWR Timing: MACO_EN assert to PWR_EN deassert_
- [select] **0** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
- [select] **APOB Version** — 0★ / SMU FW Version
    - _Ucode Patch Version_
- [select] **PWROFF-RST Timing (ms)** — UCSI tunnel at MMIO 0xFEEC2000★ / S3/Modern Standby Support / Switch S3/Modern Standby / S3 Enable / Modern Standby Enable
    - _PWRON-RST Timing  (ms)_
- [select] **PWRON-RST Timing: PWR_EN assert to PERSTb deassert** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support.
    - _RST-MACO Timing   (ms)_
- [select] **Enable/Disable PCIe x8 Slot D3Cold** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _Enable/Disable UCSI (USB Type-C Connector System Software Interface)_
- [number] **UCSI tunnel location**
    - _UCSI tunnel at EC RAM_

## GPIO 11 Output Low  (2 settings)

- [select] **VDDP voltage (+60mv)** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _VDDP voltage (+80mv)_
- [select] **VDDP voltage (+90mv)** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _VDDP voltage (-10mv)_

## Enable Serial Debug Message Under OS  (2 settings)

- [select] **VDDP voltage (+70mv)** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _VDDP voltage (+80mv)_
- [select] **VDDP voltage (+100mv)** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _VDDP voltage (-10mv)_

## Enable/Disable Sensor Fusion User Mode Driver  (9 settings)

- [select] **0** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support. / 0★ / SMU FW Version
    - _PSP BootLoader Version_
- [select] **OR Circuitry** — Discrete GPU's Audio / Disable Discrete GPU's Audio or keep its ROM strap setting / Discrete GPU BOMACO Support
    - _Pulse Circuitry_
- [select] **MACO-PWR Timing   (us)** — 0★ / PSP SecureOS Version / ABL Version
    - _MACO-PWR Timing: MACO_EN assert to PWR_EN deassert_
- [select] **APCB Version** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _0_
- [number] **SMU RV2 FW Version**
    - _0_
- [select] **PWROFF-RST Timing: PWR_EN deassert to PERSTb assert** — Modern Standby Type★ / Select S0I2 or S0I3 type for Modern Standby. / Modern Standby + S0i2 / Modern Standby + S0i3 / Modern Standby + S0i2 + S0i3
    - _PWRON-RST Timing  (ms)_
- [select] **RST-MACO Timing: PERSTb deassert to MACO_EN deassert** — SATA D3cold Enable / Enable/Disable SATA devies D3-COLD support.
    - _Primary Video Adaptor_
- [select] **UCSI Support** — SATA D3cold Enable★ / Enable/Disable SATA devies D3-COLD support.
    - _Enable/Disable UCSI (USB Type-C Connector System Software Interface)_
- [number] **UCSI tunnel can be put on ECRAM or MMIO space, this option specify which one is selected.**
    - _UCSI tunnel at EC RAM_

## VDD18 voltage (ANPEC:+90mv/TI:+87.5mv)  (1 settings)

- [select] **0** — 5v_ALW +100mv★ / Serial Debug Message Under OS / Enable Serial Debug Message Under OS / AMD Firmware Version / Show all of AMD Firmware Version / AGESA Version / 0
    - _EC FW Version_

## ID de proveedor DHCP  (2 settings)

- [select] **Dirección IP** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _Configurar dirección IP de iniciador._
- [select] **Configurar nombre de iSCSI.** — Nombre de iSCSI★ / Configurar nombre de iSCSI. / ID CHAP
    - _ID CHAP_

##  octets dela mémoire de système essayée D'ACCORD  (1 settings)

- [select] **Which USB boot option do you want to select?** — Which network boot option do you want to select?★ / The timeout value is %d seconds and it is larger than maximum timeout value %d. Restore timeout variable to %d!!!
    - _Which CD/DVD boot option do you want to select?_

## Insufficient space to store image.  (18 settings)

- [select] **MBA Configuration Menu** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$
- [select] **Management FW** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
- [select] **Main Configuration Page** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _iSCSI General Parameters_
- [select] **iSCSI General Parameters** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
- [select] **Configure iSCSI general boot parameters.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _iSCSI Initiator Parameters_
- [select] **iSCSI Initiator Parameters** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
- [select] **Configure iSCSI initiator parameters.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _iSCSI First Target Parameters_
- [select] **Secondary Device** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _Configure Secondary device parameters._
- [select] **iSCSI Secondary Device Parameters** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
- [select] **Configure Secondary device parameters.** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
- [select] **Option ROM** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
- [select] **Enable/Disable Boot Option ROM** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _Auto Detect_
- [select] **BBS** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _Int 18h_
- [select] **Int 19h** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _Hide Setup Prompt_
- [select] **Hide Setup Prompt** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
    - _Configure whether Setup Prompt is displayed during ROM initialization._
- [select] **Setup Key Stroke** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$ / ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★
- [select] **Configure key strokes to invoke configuration menu.** — Ctrl-B / Banner Message Timeout★
    - _Ctrl-S_
- [select] **iSCSI Boot Configuration Menu** — ^(([0-9](?!\d)|[1-9][0-9](?!\d)|1[0-9]{2}(?!\d)|2[0-4][0-9](?!\d)|25[0-5](?!\d))[.]?){4}$★ / ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configure iSCSI boot parameters._

## 667MHz  (1 settings)

- [select] **933MHz** — DF Common Options / 1200MHz / 1333MHz / 1367MHz★ / 1400MHz / NBIO Common Options
    - _1067MHz_

## 1433MHz  (1 settings)

- [select] **1900MHz** — DF Common Options / UMC Common Options★
    - _1933MHz_

## 1500MHz  (1 settings)

- [select] **1900MHz** — DF Common Options / UMC Common Options★
    - _1933MHz_

## 1633MHz  (1 settings)

- [select] **1900MHz** — DF Common Options / UMC Common Options★
    - _1933MHz_

## 1700MHz  (1 settings)

- [select] **1900MHz** — DF Common Options / UMC Common Options★
    - _1933MHz_

## 1767MHz  (1 settings)

- [select] **1900MHz** — DF Common Options / UMC Common Options★
    - _1933MHz_

## 1833MHz  (1 settings)

- [select] **1900MHz** — DF Common Options / UMC Common Options★
    - _1933MHz_

## Platform First Error Handling  (4 settings)

- [select] **0Dh Clk** — DF Common Options / 18h Clk / 1Ch Clk★
    - _0Eh Clk_
- [select] **19h Clk** — 1Ah Clk / 1Bh Clk★
- [select] **0Fh Clk** — DF Common Options / UMC Common Options★
    - _10h Clk_
- [select] **Specifies the core frequency multiplier. COF = 200MHz * FID / DID** — DF Common Options / NBIO Common Options★
    - _Pstate0 DID_

## Enable  (5 settings)

- [select] **Overclock** — DF Common Options / NBIO Common Options★
    - _Memory Overclock Settings_
- [select] **Specifies the core frequency divisor (DID[0] should zero if DID[5:0]>1Ah).** — Pstate1 VID / Custom Pstate2★ / Specifies the core frequency multiplier. COF = 200MHz * FID / DID / Pstate1 DID
- [select] **Pstate2 VID** — DF Common Options★ / UMC Common Options
    - _Specifies the core voltage._
- [select] **Custom Pstate3** — DF Common Options / UMC Common Options★
- [select] **Pstate3 FID** — DF Common Options / UMC Common Options★
    - _Specifies the core frequency multiplier. COF = 200MHz * FID / DID_

## Core Performance Boost  (2 settings)

- [select] **2033MHz** — DF Common Options / UMC Common Options★
    - _2067MHz_
- [select] **2100MHz** — Sets the tCL time. / 8 Clk★
    - _Tcl_

## Memory Clock Speed  (4 settings)

- [select] **1967MHz** — NBIO Common Options★ / 333MHz
    - _2000MHz_
- [select] **Channel interleaving hash** — DF Common Options / UMC Common Options★
    - _Controls whether or not the address bits are hashed during channel interleave mode. This field should not be used unless the interleaving is set to channel a..._
- [select] **DF C-state control** — DF Common Options / UMC Common Options★
    - _Enable / disable DF C-states (DF::CstateControl[DfCstateDisable])_
- [select] **xGMI DLWM control** — DF Common Options / UMC Common Options★
    - _Controls xGMI dynamic link width management feature._

## DHCP ベンダ ID  (2 settings)

- [select] **IP アドレス** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$★
    - _イニシエータ IP アドレスを設定する。_
- [select] **iSCSI 名を設定する。** — iSCSI 名★ / iSCSI 名を設定する。 / CHAP ID
    - _CHAP ID_

## ￱電源￰  (5 settings)

- [select] **ACPI S1** — ￱停用￰★ / ￱啟用￰
    - _￱啟動￰/￱關閉￰ ACPI S1/S3 ￱睡眠狀態￰_
- [select] **ThermalCtl Fan** — ￱自動￰ / ￱停用￰★
    - _Enable/Disable ThermalCtl Fan_
- [select] **￱在￰PME￱中甦醒￰** — ￱停用￰ / ￱啟用￰★
    - _￱當系統能源被關掉和￰PCI￱能源管理致能甦醒事件發生時￰, ￱決定採取何種行動￰._
- [select] **￱自動甦醒在￰S5** — ￱停用￰★ / ￱以日￰ / ￱以月日￰
    - _￱以日或月或擇選時間自動在￰S5￱甦醒￰_
- [number] **￱以月日￰**
    - _￱日￰ ￱的有效值範圍從￰ 1 ￱至￰ 31. (￱若輸入不符￰ month/day/year￱組合￰, ￱將會自動偵錯￰.)_

## ￱進階￰ CPU ￱控制￰  (1 settings)

- [select] **Cool N' Quiet ￱設定￰** — ￱停用￰ / ￱啟用￰★
    - _￱開啟或關閉切速￰._

## Configurations PCI Express  (1 settings)

- [select] **PSPP Politique** — Désactiver / Performance / Balanced-Bas★ / Power Saving / Automatique
    - _La politique PCIe asservie à la vitesse_

## APU GPP #0 Caractéristiques  (1 settings)

- [select] **GPP Activé** — Désactiver / Activer★
    - _Pour activé cette AUTO GPP. Signifie que ce port va suivre sa mise en œuvre par défaut._

## APU GPP #1 Caractéristiques  (1 settings)

- [select] **GPP Activé** — Désactiver / Activer★
    - _Pour activé cette AUTO GPP. Signifie que ce port va suivre sa mise en œuvre par défaut._

## APU GPP #2 Caractéristiques  (1 settings)

- [select] **GPP Activé** — Désactiver / Activer★
    - _Pour activé cette AUTO GPP. Signifie que ce port va suivre sa mise en œuvre par défaut._

## APU GPP #3 Caractéristiques  (1 settings)

- [select] **GPP Activé** — Désactiver / Activer★
    - _Pour activé cette AUTO GPP. Signifie que ce port va suivre sa mise en œuvre par défaut._

## APU GPP #4 Caractéristiques  (1 settings)

- [select] **GPP Activé** — Désactiver / Activer★
    - _Pour activé cette AUTO GPP. Signifie que ce port va suivre sa mise en œuvre par défaut._

## APU GPP #5 Caractéristiques  (1 settings)

- [select] **GPP Activé** — Désactiver / Activer★
    - _Pour activé cette AUTO GPP. Signifie que ce port va suivre sa mise en œuvre par défaut._

## APU GPP #6 Caractéristiques  (1 settings)

- [select] **GPP Activé** — Désactiver / Activer★
    - _Pour activé cette AUTO GPP. Signifie que ce port va suivre sa mise en œuvre par défaut._

## Configuration Amorçage  (2 settings)

- [select] **Numlock** — Off★ / On
    - _Selectionner l'état d'allumer la Puissance pour Numlock_
- [select] **Fast Recovery** — Désactiver★ / Activer
    - _Enable / Disable Fast Recovery test_

## Configuration Périphérique  (3 settings)

- [select] **Trust Platform Module** — Désactiver / Enable discrete TPM / Enable firmware TPM★
    - _Enable/Disable TPM physical presence. Need to reboot when set from disable to enable before selecting TPM Operation._
- [select] **Erase fTPM NV for factory reset** — Désactiver / Activer★
    - _Control if need to erase the TPM NV when fTPM factory reset flag set._
- [select] **Azalia** — Désactiver / Automatique★
    - _AUTO: Auto-detecter Azalia code.  Desactivé: Desactiver Azalia controleur peut etre selectionné._

## Configuration IDE  (2 settings)

- [select] **SATA** — Désactiver / Automatique★
    - _AUTO: Auto detect the SATA controller.  DISABLED: Disable the SATA controller_
- [select] **SATA Configure as** — IDE / AHCI★
    - _Set SATA Configure Type_

## Configuration de Vidéo  (2 settings)

- [select] **HDMI Audio** — Désactiver / Activer★
    - _Enable/Disable HDMI Audio_
- [select] **Contrôle du rétroéclairage** — Video BIOS / VGA driver★
    - _Sélectionnez contrôle du rétroéclairage_

## Configuration USB  (9 settings)

- [select] **EHCI0** — Désactiver / Activer★
    - _AUTO: Auto detect the EHCI controller 0 (Device12 Function 0).  DISABLED: Disable the EHCI controller 0_
- [select] **USB BIOS Support** — Désactiver / Activer★ / UEFI Only
    - _USB keyboard/mouse/storage support under UEFI environment_
- [select] **USB2.0** — Désactiver / Activer★
- [select] **USB PORT 0** — Désactiver / Activer★
    - _Enable/Disable USB Port 0_
- [select] **USB PORT 1** — Désactiver / Activer★
- [select] **USB PORT 2** — Désactiver / Activer★
- [select] **USB PORT 3** — Désactiver / Activer★
- [select] **USB PORT 4** — Désactiver / Activer★
- [select] **USB PORT 5** — Désactiver / Activer★

## Configuration de Chipset  (2 settings)

- [select] **PCI Temps Retardé** — 32 / 64★ / 96 / 128 / 160 / 192 / 224 / 248
- [toggle] **STIBP Status**
    - _Disable/Enable the Single Thread Indirect Branch Predictor(STIBP)._

## ACPI Table/ Caractère de Contrôle  (6 settings)

- [select] **FACP - C2 Valeur Retardée** — Désactiver / Activer★
    - _Seule valeur de l'ACPI. Sélectionnez la valeur pour le champ P_LVL2_LAT trouve dans le tableau où FACP: plus petit que 100 Enabled = C2, plus grand que 100 =..._
- [select] **FACP - C3 Valeur Retardée** — Désactiver / Activer★
    - _Seule valeur de l'ACPI. Sélectionnez la valeur pour le champ P_LVL3_LAT trouve dans le tableau où FACP: plus petit que 1000 Enabled = C3, plus grand que 1000..._
- [select] **FACP - RTC S4 Wakeup** — Désactiver / Activer★
    - _Valeur juste pour ACPI. Activer/Desactiver pour S4 Reveille du RTC_
- [select] **APIC - IO APIC Mode** — Désactiver / Activer★
    - _Cet item est valide juste pour WIN2k et WINXP. Aussi, une installation initialle OS doit se produire quand APIC Mode est desiré. Tester IO ACPI par determine..._
- [select] **HPET - HPET Support** — Désactiver / Activer★
    - _High Precision Event Timer est pris en charge dans Windows Vista ou supérieur. contrôleur HPET doit pas être considérée dans Windows XP, peu importe activer ..._
- [select] **_OSC Méthode** — Désactiver / Activer★

## Cpu mise connexes  (4 settings)

- [select] **CPU P-Etat fixant** — Automatique★ / Lowest Speed
- [select] **SVM support** — Désactiver / Activer★
    - _Enable/Disable SVM support_
- [select] **SVM Lock** — Désactiver / Activer★
    - _Enable or disable the SVM Lock registers._
- [select] **SMM Code Lock** — Désactiver / Activer★
    - _Enable or disable the SMM code segment/registers._

## ￱パワー￰  (3 settings)

- [select] **ThermalCtl Fan** — ￱オートマチック￰ / ￱使用しない￰★
    - _Enable/Disable ThermalCtl Fan_
- [select] **PME ￱による起床￰** — ￱使用しない￰ / ￱使用する￰★
    - _￱ システムの電源がオフで￰PCI Power Management Enable￱起床イベントが起きた際の動作を決めます￰._
- [select] **S5￱からの自動起床￰** — ￱使用しない￰★ / ￱毎日￰ / ￱日付￰
    - _￱日付または毎日の固定時刻での￰S5￱からの自動起床￰_

## Selectionner l'état d'allumer la Puissance pour Numlock  (10 settings)

- [select] **Enable or disable the SVM Lock registers.** — IRQ9 / SVM Lock / Enable/Disable Multi CORE Support★
    - _SMM Code Lock_
- [select] **USB PORT 1** — USB PORT 3★ / USB PORT 4
    - _USB PORT 2_
- [select] **AMDAHCI** — Set SATA Configure Type★
    - _IDE->AMDAHCI_
- [select] **Canal A** — DIMM 1 / Canal B★
    - _DIMM 0_
- [toggle] **DT x1 slot and ExpressCard slot are sharing one GPP port, please choose the configuration based on the board BOM**
    - _ExpressCard Slot_
- [toggle] **DT x1 slot**
    - _Ir Activity Led Enable_
- [toggle] **Enable/Disable Ir Activity Led**
    - _Enable discrete TPM_
- [toggle] **Désactiver** — Désactiver★
- [select] **Azalia** — STIBP Status /    ★
    - _AUTO: Auto-detecter Azalia code.  Desactivé: Desactiver Azalia controleur peut etre selectionné._
- [select] **Enable / Disable Fast Recovery test** — Selectionner Zip Emulation comme FDD ou HDD / FDD / HDD★
    - _Type de Zip Emulation_

## SATA  (3 settings)

- [select] **[Pas Installé]** — APU GPP #3 Caractéristiques★ / Enable/Disable HDMI Audio / Contrôle du rétroéclairage / Sélectionnez contrôle du rétroéclairage / Video BIOS / VGA driver
- [select] **[￱未安裝￰]** — APU GPP #3 ￱設定￰★ / Enable/Disable HDMI Audio / ￱背光設置方式￰ / ￱選擇背光設置方式￰ / Video BIOS / VGA driver
- [select] **[Not Installed]** — APU GPP #3 Features★ / Enable/Disable HDMI Audio / Brightness Control Method / Select Brightness Control Method / Video BIOS / VGA driver / InsydeH2O Version

## Advanced  (6 settings)

- [select] **Graphic mode:** — MSHybrid★ / dGPU only
    - _GPU switch control: MSHybrid or dGPU only_
- [select] **Wake Up System on time** — Disabled★ / Enabled
    - _Enable/Disable RTC wake from S3/S4/S5 function_
- [number] **Wake Up hour**
    - _Setup wake up hour (ISO 8601), allow 0~23_
- [number] **Wake up minute**
    - _Setup wake up minute , allow 0~59_
- [number] **Wake up second**
    - _Setup wake up second , allow 0~59_
- [select] **Above 4GB MMIO** — Disabled / Enabled★
    - _Enable/Disable above 4GB MemoryMappedIO BIOS assignment. It's only available with Uefi Boot Mode._

## Device Configuration  (19 settings)

- [select] **Wake on WLAN:** — Disabled★ / Enabled
- [select] **Wi-Fi:** — Disabled / Enabled★
    - _Wi-Fi Switch._
- [select] **WiGig:** — Disabled / Enabled★
    - _WiGig Switch._
- [select] **Bluetooth:** — Disabled / Enabled★
    - _Bluetooth Switch._
- [select] **CVNi Wi-Fi/BT:** — Disabled / Enabled★
    - _CVNi Wi-Fi/BT Switch._
- [select] **3G/LTE:** — Disabled / Enabled★
    - _3G Switch._
- [select] **Card Reader:** — Disabled / Enabled★
    - _Card Reader Switch._
- [select] **USB Ports:** — Disabled / Enabled★
    - _USB Ports Switch._
- [select] **Wired Lan:** — Disabled / Enabled★
    - _Wired Lan Switch._
- [select] **Optical Drive:** — Disabled / Enabled★
    - _Enable/Disable Optical Drive_
- [select] **Audio:** — Disabled / Enabled★
    - _Audio Switch._
- [select] **Speaker & Headphone:** — Disabled / Enabled★
    - _Enable/Disable Speaker & Headphone._
- [select] **Microphone:** — Disabled / Enabled★
    - _Enable/Disable Microphone._
- [select] **Camera:** — Disabled / Enabled★
    - _Camera Switch._
- [select] **Fingerprint:** — Disabled / Enabled★
    - _Fingerprint Switch._
- [select] **Type C** — Disabled / Enabled★
    - _Enable/Disable device connected through Type C (Display Port not included)_
- [select] **Power-off USB Charge:** — Disabled / Enabled★
    - _Enables you to charge mobile devices when your computer is off or in Sleep mode._
- [select] ** Battery Threshold:** — 10% / 20% / 30%★
    - _Set a computer battery charge limit, below which charging stops._
- [select] **USB Boot:** — Enabled★ / Disabled

## ￱PCI Express組態￰  (1 settings)

- [select] **PSPP ￱政策￰** — ￱停用￰ / ￱性能￰ / ￱平衡式低￰★ / ￱省電￰ / ￱自動￰
    - _PCIe ￱速度電力政策￰_

## APU GPP #0 ￱設定￰  (1 settings)

- [select] **GPP ￱致能￰** — ￱停用￰ / ￱啟用￰★
    - _￱開起這個￰GPP￱。￰AUTO￱意謂這個埠將遵守它的預設實作。￰_

## APU GPP #1 ￱設定￰  (1 settings)

- [select] **GPP ￱致能￰** — ￱停用￰ / ￱啟用￰★
    - _￱開起這個￰GPP￱。￰AUTO￱意謂這個埠將遵守它的預設實作。￰_

## APU GPP #2 ￱設定￰  (1 settings)

- [select] **GPP ￱致能￰** — ￱停用￰ / ￱啟用￰★
    - _￱開起這個￰GPP￱。￰AUTO￱意謂這個埠將遵守它的預設實作。￰_

## APU GPP #3 ￱設定￰  (1 settings)

- [select] **GPP ￱致能￰** — ￱停用￰ / ￱啟用￰★
    - _￱開起這個￰GPP￱。￰AUTO￱意謂這個埠將遵守它的預設實作。￰_

## APU GPP #4 ￱設定￰  (1 settings)

- [select] **GPP ￱致能￰** — ￱停用￰ / ￱啟用￰★
    - _￱開起這個￰GPP￱。￰AUTO￱意謂這個埠將遵守它的預設實作。￰_

## APU GPP #5 ￱設定￰  (1 settings)

- [select] **GPP ￱致能￰** — ￱停用￰ / ￱啟用￰★
    - _￱開起這個￰GPP￱。￰AUTO￱意謂這個埠將遵守它的預設實作。￰_

## APU GPP #6 ￱設定￰  (1 settings)

- [select] **GPP ￱致能￰** — ￱停用￰ / ￱啟用￰★
    - _￱開起這個￰GPP￱。￰AUTO￱意謂這個埠將遵守它的預設實作。￰_

## ￱開機設定￰  (3 settings)

- [select] **Numlock** — ￱關￰★ / ￱開￰
    - _￱選擇￰Numlock￱開機狀態￰_
- [select] **Fast Recovery** — ￱停用￰★ / ￱啟用￰
    - _Enable / Disable Fast Recovery test_
- [select] **PeiGop** — ￱停用￰★ / ￱啟用￰
    - _PeiGop function Enable / Disable_

## ￱設定週邊￰  (3 settings)

- [select] **Trust Platform Module** — ￱停用￰ / Enable discrete TPM / Enable firmware TPM★
    - _Enable/Disable TPM physical presence. Need to reboot when set from disable to enable before selecting TPM Operation._
- [select] **Erase fTPM NV for factory reset** — ￱停用￰ / ￱啟用￰★
    - _Control if need to erase the TPM NV when fTPM factory reset flag set._
- [select] **Azalia￱音效設定￰** — ￱停用￰ / ￱自動￰★
    - _￱自動，自動偵測編碼方式。停用，取消控制￰_

## IDE ￱設定￰  (1 settings)

- [select] **SATA** — ￱停用￰ / ￱自動￰★
    - _AUTO: Auto detect the SATA controller.  DISABLED: Disable the SATA controller_

## ￱顯示設定￰  (2 settings)

- [select] **HDMI Audio** — ￱停用￰ / ￱啟用￰★
    - _Enable/Disable HDMI Audio_
- [select] **￱背光設置方式￰** — Video BIOS / VGA driver★
    - _￱選擇背光設置方式￰_

## USB ￱設定￰  (9 settings)

- [select] **EHCI0** — ￱停用￰ / ￱啟用￰★
    - _AUTO: Auto detect the EHCI controller 0 (Device12 Function 0).  DISABLED: Disable the EHCI controller 0_
- [select] **USB2.0** — ￱停用￰ / ￱啟用￰★
- [select] **USB PORT 0** — ￱停用￰ / ￱啟用￰★
    - _Enable/Disable USB Port 0_
- [select] **USB PORT 1** — ￱停用￰ / ￱啟用￰★
- [select] **USB PORT 2** — ￱停用￰ / ￱啟用￰★
- [select] **USB PORT 3** — ￱停用￰ / ￱啟用￰★
- [select] **USB PORT 4** — ￱停用￰ / ￱啟用￰★
- [select] **USB PORT 5** — ￱停用￰ / ￱啟用￰★
- [select] **USB BIOS Support** — ￱使用しない￰ / ￱使用する￰★ / UEFI Only
    - _USB keyboard/mouse/storage support under UEFI environment_

## ￱晶片組設定￰  (2 settings)

- [select] **PCI ￱潛在時間計時器￰** — 32 / 64★ / 96 / 128 / 160 / 192
- [toggle] **STIBP Status**
    - _Disable/Enable the Single Thread Indirect Branch Predictor(STIBP)._

## ACPI ￱表￰/￱特性￰ ￱控制￰  (5 settings)

- [select] **FACP - C2 ￱潛在值￰** — ￱停用￰ / ￱啟用￰★
    - _ACPI￱獨有的值￰. ￱在￰FACP￱表裡選擇一個值給￰P_LVL2_LAT￱範圍￰, ￱小於￰100 = C2￱啟用￰ , ￱大於￰100 = C2 ￱禁用￰_
- [select] **FACP - C3 ￱潛在值￰** — ￱停用￰ / ￱啟用￰★
    - _ACPI￱獨有的值￰. ￱在￰FACP￱表裡選擇一個值給￰P_LVL3_LAT￱範圍￰, ￱小於￰1000 = C3￱啟用￰ , ￱大於￰1000 = C3 ￱禁用￰_
- [select] **APIC - IO APIC ￱模式￰** — ￱停用￰ / ￱啟用￰★
    - _￱這個項目僅在￰win2k￱和￰winxp￱下有效￰_
- [select] **HPET-HPET￱模式￰** — ￱停用￰ / ￱啟用￰★
    - _￱高精確度事件計時器被支援在￰Windows Vista￱或以上。無論啟用￰/￱禁用￰HPET￱，￰HPET￱控制器都不應該在￰Windows XP￱下的裝置管理員中被發現。若啟用此功能，￰HPET￱表將被加載到￰ACPI￱表。￰_
- [select] **￱_OSC 運算式￰** — ￱停用￰ / ￱啟用￰★

## ￱中央處理器相關設定￰  (1 settings)

- [select] **￱CPU P-State設定￰** — ￱自動￰★ / ￱最低速￰

## ￱選擇￰Numlock￱開機狀態￰  (8 settings)

- [select] **USB PORT 1** — USB PORT 3★ / USB PORT 4
    - _USB PORT 2_
- [select] **￱通道￰ A** — ￱記憶體插槽￰ 1 / ￱通道￰ B★
    - _￱記憶體插槽￰ 0_
- [toggle] **DT x1 slot and ExpressCard slot are sharing one GPP port, please choose the configuration based on the board BOM**
    - _ExpressCard Slot_
- [toggle] **DT x1 slot**
    - _Ir Activity Led Enable_
- [toggle] **Enable/Disable Ir Activity Led**
    - _Enable discrete TPM_
- [toggle] **￱停用￰** — ￱停用￰★
- [select] **Azalia￱音效設定￰** — STIBP Status /    ★
    - _￱自動，自動偵測編碼方式。停用，取消控制￰_
- [select] **Enable / Disable Fast Recovery test** — ￱選擇￰Zip￱模擬軟碟或硬碟￰ / ￱軟碟機￰ / ￱硬碟機￰★
    - _Zip￱模擬種類￰_

## Serial ATA Port 1         (4 settings)

- [select] **Uninstall**
- [select] **64** — 96★ / 128 / 160 / FACP - C2 ￱潛在值￰ / ACPI￱獨有的值￰. ￱在￰FACP￱表裡選擇一個值給￰P_LVL2_LAT￱範圍￰, ￱小於￰100 = C2￱啟用￰ , ￱大於￰100 = C2 ￱禁用￰ / FACP - C2 Latency Value / Value only for ACPI. Select the value for the P_LVL2_LAT field found in the FACP Table where: smaller than 100 = C2 Enabled, Larger than 100 = C2 Disabled / FACP - C2 Valeur Retardée / Seule valeur de l'ACPI. Sélectionnez la valeur pour le champ P_LVL2_LAT trouve dans le tableau où FACP: plus petit que 100 Enabled = C2, plus grand que 100 = C2 handicapés
- [select] **￱なし￰**
- [select] **Uninstalle**

## ￱調整顯示設定￰.  (15 settings)

- [select] **PCI ￱插槽￰4 IRQ ￱優先權￰**
    - _PCI ￱插槽￰5 IRQ ￱優先權￰_
- [select] **PCI ￱插槽￰6 IRQ ￱優先權￰**
    - _￱手動￰ IRQ ￱選擇並不保證￰ PCI ￱插槽裝置會以選擇作調整￰, ￱因為￰ PCI ￱裝置可能已被設定了可利用的資源￰._
- [select] **PeiGop** — Fast Recovery★ / Enable / Disable Fast Recovery test
    - _PeiGop function Enable / Disable_
- [select] **￱序列埠￰A￱中斷向量與其他裝置衝突￰,￱請重新選擇￰**
    - _￱序列埠￰B￱中斷向量與其他裝置衝突￰,￱請重新選擇￰_
- [select] **Zip￱模擬種類￰** — ￱軟碟機￰★ / ￱硬碟機￰
    - _￱選擇￰Zip￱模擬軟碟或硬碟￰_
- [select] **Azalia￱音效設定￰**
    - _￱自動，自動偵測編碼方式。停用，取消控制￰_
- [select] **￱資源衝突￰. ￱請重新選擇￰**
    - _￱此中斷向量已被￰PCI SLOT￱使用￰_
- [select] **IRQ3**
    - _IRQ4_
- [select] **GPP ￱致能￰**
    - _￱開起這個￰GPP￱。￰AUTO￱意謂這個埠將遵守它的預設實作。￰_
- [select] **￱CPU P-State設定￰**
- [select] **￱記憶體插槽￰ 0**
    - _￱記憶體插槽￰ 1_
- [select] **[￱未安裝￰]**
- [select] **￱最低速￰**
    - _￱_OSC 運算式￰_
- [select] **￱_OSC 運算式￰**
    - _ThermalCtl Fan_
- [select] **Serial ATA Port 5 Device configuration**
    - _Serial ATA Port 0       _

## Serial Number:  (1 settings)

- [select] **Graphic mode:** — CPU Speed: / [Not Detected]★
    - _GPU switch control: MSHybrid or dGPU only_

## Exit system setup and without saving your changes.  (1 settings)

- [select] **Save & shutdown** — CPU Speed: / Setup Confirmation\Save changes and then continue to shutdown? / Load Setup Defaults / Load Optimal Defaults.★ / Setup Confirmation\Load default configuration now? / EMMC Model Name:
    - _Save changes and shutdown the system._

## Wi-Fi:  (1 settings)

- [select] **xHCI Support:** — CPU Speed: / [Not Detected]★
    - _Enable/Disable external USB3.0 controller._

## WiGig:  (1 settings)

- [select] **xHCI Support:** — CPU Speed: / [Not Detected]★
    - _Enable/Disable external USB3.0 controller._

## Bluetooth:  (1 settings)

- [select] **xHCI Support:** — CPU Speed: / [Not Detected]★
    - _Enable/Disable external USB3.0 controller._

## CVNi Wi-Fi/BT:  (1 settings)

- [select] **xHCI Support:** — CPU Speed: / [Not Detected]★
    - _Enable/Disable external USB3.0 controller._

## 3G/LTE:  (1 settings)

- [select] **xHCI Support:** — CPU Speed: / [Not Detected]★
    - _Enable/Disable external USB3.0 controller._

## Card Reader:  (1 settings)

- [select] **xHCI Support:** — CPU Speed: / [Not Detected]★
    - _Enable/Disable external USB3.0 controller._

## USB Ports:  (1 settings)

- [select] **xHCI Support:** — CPU Speed: / [Not Detected]★
    - _Enable/Disable external USB3.0 controller._

## System Time:  (9 settings)

- [select] **Delete This Boot Option** — CPU Speed: / [Not Detected]★
    - _Exit_
- [select] **[Cancel the pairing of Pad & Dock]** — [Not Detected] / Erase all Secure Boot Setting:★
    - _[Set]_
- [select] **[Clean]** — CPU Speed: / [Not Detected]★ / Current TPM (TCM) Version:
    - _[Frozen]_
- [select] **Frozen** — CPU Speed: / [Not Detected]★
    - _SwitchLock:_
- [select] **No Accessed  ** — CPU Speed: / [Not Detected]★
    - _Disable _
- [select] **Set OPAL Device Password** — CPU Speed: / [Not Detected]★
- [select] **Revert OPAL Device** — CPU Speed: / [Not Detected]★
- [select] **The available boot devices will not change until a reboot!** — CPU Speed: / [Not Detected]★
- [select] **Microsoft recommends executing Windows 8 and the version above under UEFI boot mode to enjoy the full features.** — CPU Speed: / [Not Detected]★

## System Date:  (1 settings)

- [toggle] **Video Memory:**
    - _None_

## Total Memory:  (6 settings)

- [select] **Enabled** — CPU Speed: / [Not Detected]★
    - _Disabled_
- [select] **Secure Boot:** — CPU Speed: / [Not Detected]★
    - _Enable or Disable secure boot check_
- [select] **Secure Boot Mode:** — CPU Speed: / [Not Detected]★
    - _ _
- [select] **Select Secure Boot Mode** — CPU Speed: / [Not Detected]★
    - _Standard_
- [select] **Custom** — CPU Speed: / [Not Detected]★
    - _[Enter]_
- [select] **When the option set to ** — CPU Speed: / [Not Detected]★
    - _Fast Boot_

## Setup Confirmation\Save configuration changes and exit now?  (4 settings)

- [select] **POST Animation & Sound:** — EMMC Model Name:★ / Internal KB Numpad
    - _Enable/Disable POST Animation & Sound effect._
- [select] **Legacy** — CPU Speed: / [Not Detected]★
    - _Boot priority order:_
- [select] **Use <↑> or <↓> to select a device, then press <F6> to move it up the list, or <F5> to move it down the list. Press <Esc> to escape the menu** — CPU Speed: / [Not Detected]★
    - _HDD : _
- [select] **HDD%d : ** — CPU Speed: / [Not Detected]★
    - _ATAPI CDROM : _

## Configures video settings.  (19 settings)

- [select] **PCI Slot4 IRQ Priority**
    - _PCI Slot5 IRQ Priority_
- [select] **PCI Slot6 IRQ Priority**
    - _Manual IRQ selection does not garantee PCI slot device will be configured with choice because PnP ISA Cards (if present) are assigned the available resources..._
- [select] **LEGACY IDE** — AMDAHCI★
    - _IDE->AHCI_
- [select] **PeiGop** — Fast Recovery★ / Enable / Disable Fast Recovery test
    - _PeiGop function Enable / Disable_
- [select] **Serial Port A IRQ Conflict. Please re-select!**
    - _Serial Port B IRQ Conflict. Please re-select!_
- [select] **  AHCI supporting as**
    - _Setting AHCI supporting as Native uEFI Mode or Legacy Mode_
- [select] **Legacy Mode**
    - _UEFI Mode_
- [select] **SATA Configure as**
    - _IDE_
- [select] **Zip Emulation Type** — FDD★ / HDD
    - _Selects Zip Emulation as FDD or HDD_
- [select] **Azalia**
    - _AUTO: Auto detect the Azalia codec.  DISABLED: Disable the Azalia controller can be selectable._
- [select] **Resources Conflict. Please re-select!**
    - _The IRQ was used by PCI SOLT._
- [select] **IRQ3**
    - _IRQ4_
- [select] **GPP Enabled**
    - _To enabled this GPP. AUTO means this port will follow its default implementation._
- [select] **CPU P-State Setting**
- [select] **DIMM 0**
    - _DIMM 1_
- [select] **[Not Installed]**
- [select] **Lowest Speed**
    - __OSC Support_
- [select] **_OSC Method**
    - _Thermal Fan Control_
- [select] **Serial ATA Port 5 Device configuration**
    - _Serial ATA Port 0       _

## Power  (7 settings)

- [select] **ACPI S1** — Disabled★ / Enabled
    - _Enable/Disable ACPI S1/S3 Sleep state_
- [select] **ACPI S3** — Disabled / Enabled★
    - _Enable/Disable ACPI S1/S3 Sleep state_
- [select] **Thermal Fan Control** — Auto / Disabled★
    - _Enable/Disable ThermalCtl Fan_
- [select] **Wake on PME** — Disabled / Enabled★
    - _Determines the action taken when the system power is off and a PCI Power Management Enable wake up event occurs._
- [select] **Auto Wake on S5** — Disabled★ / By Every Day / By Day of Month
    - _Auto wake on S5, By Day of Month or Fixed time of every day_
- [number] **  Day of Month**
    - _This is the help for the day field. Valid range is from 1 to 31. (Error checking will be done against month/day/year combinations that are not supported.) RE..._
- [select] **S5 Long Run Test** — Disabled★ / Enabled
    - _Enable : force to enable RTC S5 wake up, even if OS disables it. Support ipwrtest to do RTC S5 wakeup._

## Advanced CPU Control  (2 settings)

- [select] **Cool N' Quiet Support** — Disabled / Enabled★
    - _Enable or Disable Cool and Quiet._
- [select] **Multi CORE Support** — Disabled / Auto★
    - _Enable/Disable Multi CORE Support_

## Cool N' Quiet Support  (3 settings)

- [select] **Enable or Disable Cool and Quiet.** — Enable/Disable Multi CORE Support★ / SVM support
    - _Multi CORE Support_
- [select] **FACP - C3 Latency Value**
    - _Value only for ACPI. Select the value for the P_LVL3_LAT field found in the FACP Table where: smaller than 1000 = C3 Enabled, Larger than 1000 = C3 Disabled_
- [select] **FACP - C3 Valeur Retardée**
    - _Seule valeur de l'ACPI. Sélectionnez la valeur pour le champ P_LVL3_LAT trouve dans le tableau où FACP: plus petit que 1000 Enabled = C3, plus grand que 1000..._

## Configurer le réglage de vidéo.  (16 settings)

- [select] **PCI Slot4 IRQ Priorité**
    - _PCI Slot5 IRQ Priority_
- [select] **PCI Slot6 IRQ Priority**
    - _le fait que Manuel IRQ selection ne guaranti pas PCI slot device sera configuré avec option parceque PnP ISA Cartes (si presente) sont assignées comme resour..._
- [select] **LEGACY IDE** — AMDAHCI★
    - _IDE->AHCI_
- [select] **Serial Port A IRQ Conflict. Please re-select!**
    - _Serial Port B IRQ Conflict. Please re-select!_
- [select] **SATA Configure as**
    - _IDE_
- [select] **Type de Zip Emulation** — FDD★ / HDD
    - _Selectionner Zip Emulation comme FDD ou HDD_
- [select] **Azalia**
    - _AUTO: Auto-detecter Azalia code.  Desactivé: Desactiver Azalia controleur peut etre selectionné._
- [select] **Conflict des Resources. Veuillez reselectionner!**
    - _The IRQ was used by PCI SOLT._
- [select] **IRQ3**
    - _IRQ4_
- [select] **GPP Activé**
    - _Pour activé cette AUTO GPP. Signifie que ce port va suivre sa mise en œuvre par défaut._
- [select] **CPU P-Etat fixant**
- [select] **DIMM 0**
    - _DIMM 1_
- [select] **[Pas Installé]**
- [select] **Lowest Speed**
    - __OSC Méthode_
- [select] **_OSC Méthode**
    - _ThermalCtl Fan_
- [select] **Serial ATA Port 5 Device configuration**
    - _Serial ATA Port 0       _

## Erase all content in secure four variables PK, KEK, db, and dbx  (8 settings)

- [select] **When this option is selected, users may select all available .efi in FAT32 partitions and add the .efi hash into secure DB** — CPU Speed: / [Not Detected]★
    - _ _
- [select] **Enable/Disable Fast Boot** — EMMC Model Name: / CPU Speed:★
    - _Wired Lan:_
- [select] **This isn't a vaild EFI image. Please select another file!!** — CPU Speed: / [Not Detected]★
    - _Add an new file\Do you wish to add this file to allowable database?_
- [select] **FILE is exist** — CPU Speed:★ / Cannot find file!! / Restore secure boot to factory default
    - _Erase all Secure boot settings_
- [number] **Acer Disk Sanitizer Tool**
    - _None_
- [select] **The Boot Description is exist** — CPU Speed:★ / [Not Detected]
    - _max 5 entries are allowed_
- [select] **Boot** — CPU Speed: / [Not Detected]★
    - _Boot Mode:_
- [select] **Set System Boot Mode** — CPU Speed: / EMMC Model Name:★
    - _UEFI_

## Cool N' Quiet ￱設定￰  (2 settings)

- [select] **￱開啟或關閉切速￰.**
- [select] **FACP - C3 ￱潛在值￰**
    - _ACPI￱獨有的值￰. ￱在￰FACP￱表裡選擇一個值給￰P_LVL3_LAT￱範圍￰, ￱小於￰1000 = C3￱啟用￰ , ￱大於￰1000 = C3 ￱禁用￰_

## ￱ディスプレイなどの表示装置に関する設定を行います。￰  (9 settings)

- [select] **PCI ￱スロット￰4 IRQ ￱優先順位￰**
- [select] **Zip￱エミュレーションの種類￰**
    - _FDD￱または￰ HDD ￱の￰ Zip ￱エミュレーションを選択する￰_
- [select] **GPP ￱有効￰**
    - _￱この￰GPP￱を有効にする。￰AUTO￱手段は、このポートはデフォルトの実装を情報通信技術に従います。￰_
- [select] **￱CPUの設定状態のP -￰**
- [select] **￱メモリスロット￰ 0**
    - _￱メモリスロット￰ 1_
- [select] **[￱なし￰]**
- [select] **￱最低速度￰**
    - _￱_osc法￰_
- [select] **￱_osc法￰**
    - _ThermalCtl Fan_
- [select] **Serial ATA Port 5 Device configuration**
    - _Serial ATA Port 0       _

## ￱構成のPCIエクスプレス￰  (1 settings)

- [select] **PCIe￱ポリシー￰** — ￱使用しない￰ / ￱パフォーマンス￰ / ￱バランスのとれた低￰★ / ￱パワーセーブ￰ / ￱オートマチック￰
    - _PCIe￱のスピードの電源ポリシー￰_

## APU GPP #0 ￱の機能￰  (1 settings)

- [select] **GPP ￱有効￰** — ￱使用しない￰ / ￱使用する￰★
    - _￱この￰GPP￱を有効にする。￰AUTO￱手段は、このポートはデフォルトの実装を情報通信技術に従います。￰_

## APU GPP #1 ￱の機能￰  (1 settings)

- [select] **GPP ￱有効￰** — ￱使用しない￰ / ￱使用する￰★
    - _￱この￰GPP￱を有効にする。￰AUTO￱手段は、このポートはデフォルトの実装を情報通信技術に従います。￰_

## APU GPP #2 ￱の機能￰  (1 settings)

- [select] **GPP ￱有効￰** — ￱使用しない￰ / ￱使用する￰★
    - _￱この￰GPP￱を有効にする。￰AUTO￱手段は、このポートはデフォルトの実装を情報通信技術に従います。￰_

## APU GPP #3 ￱の機能￰  (1 settings)

- [select] **GPP ￱有効￰** — ￱使用しない￰ / ￱使用する￰★
    - _￱この￰GPP￱を有効にする。￰AUTO￱手段は、このポートはデフォルトの実装を情報通信技術に従います。￰_

## APU GPP #4 ￱の機能￰  (1 settings)

- [select] **GPP ￱有効￰** — ￱使用しない￰ / ￱使用する￰★
    - _￱この￰GPP￱を有効にする。￰AUTO￱手段は、このポートはデフォルトの実装を情報通信技術に従います。￰_

## APU GPP #5 ￱の機能￰  (1 settings)

- [select] **GPP ￱有効￰** — ￱使用しない￰ / ￱使用する￰★
    - _￱この￰GPP￱を有効にする。￰AUTO￱手段は、このポートはデフォルトの実装を情報通信技術に従います。￰_

## APU GPP #6 ￱の機能￰  (1 settings)

- [select] **GPP ￱有効￰** — ￱使用しない￰ / ￱使用する￰★
    - _￱この￰GPP￱を有効にする。￰AUTO￱手段は、このポートはデフォルトの実装を情報通信技術に従います。￰_

## ￱起動設定￰  (2 settings)

- [select] **￱起動時の￰Numlock￱設定￰** — ￱オフ￰★ / ￱オン￰
    - _￱本パソコンの起動時に、￰  ￱キーボードを￰Numlock ￱状￰  ￱態にするかどうかを設定￰  ￱します。￰                [￱オフ￰]                   ￱起動時に、キーボードを￰Numlock ￱状態にしません。￰                         [￱オ..._
- [select] **Fast Recovery** — ￱使用しない￰★ / ￱使用する￰
    - _Enable / Disable Fast Recovery test_

## ￱周辺機器設定￰  (2 settings)

- [select] **Trust Platform Module** — ￱使用しない￰ / Enable discrete TPM / Enable firmware TPM★
    - _Enable/Disable TPM physical presence. Need to reboot when set from disable to enable before selecting TPM Operation._
- [select] **Erase fTPM NV for factory reset** — ￱使用しない￰ / ￱使用する￰★
    - _Control if need to erase the TPM NV when fTPM factory reset flag set._

## ￱ディスプレイ設定￰  (2 settings)

- [select] **HDMI Audio** — ￱使用しない￰ / ￱使用する￰★
    - _Enable/Disable HDMI Audio_
- [select] **￱後光は方式を設置￰** — Video BIOS / VGA driver★
    - _￱後光セットアップ方式を選ぶ￰_

## ACPI ￱テーブル￰/￱機能の操作￰  (3 settings)

- [select] **FACP - C2 ￱レイテンシの値￰** — ￱使用しない￰ / ￱使用する￰★
    - _￱値の￰ACPI￱のみ。 ￰P_LVL2_LAT￱フィールドの値を選択します￰FACP￱テーブル内の場所￰：100 = C2￱有効、拡大よりも￰100 = C2￱よりも小さい障害が見つかりました￰_
- [select] **FACP - 32 ￱レイテンシの値￰** — ￱使用しない￰ / ￱使用する￰★
    - _￱値の￰ACPI￱のみ。 ￰P_LVL3_LAT￱フィールドの値を選択します￰FACP￱テーブル内の場所￰：1000 = C3￱有効、拡大よりも￰1000 = C3￱よりも小さい障害が見つかりました￰_
- [select] **￱_osc法￰** — ￱使用しない￰ / ￱使用する￰★

## ￱cpuの関連の設定￰  (1 settings)

- [select] **￱CPUの設定状態のP -￰** — ￱オートマチック￰★ / ￱最低速度￰

## Allumer  (6 settings)

- [select] **ACPI S1** — Désactiver★ / Activer
    - _Activé/Désactivé ACPI S1/S3 En reveille_
- [select] **ACPI S3** — Désactiver / Activer★
    - _Activé/Désactivé ACPI S1/S3 En reveille_
- [select] **ThermalCtl Fan** — Automatique / Désactiver★
    - _Enable/Disable ThermalCtl Fan_
- [select] **Reveiller sur PME** — Désactiver / Activer★
    - _Determiner l'action prise quand la puissance système est eteinte et un Puissance Management ActivéPCI reveille les incidents se passer._
- [select] **Auto Wake on S5** — Désactiver★ / Par Chaque Jour / Par Jour du Mois
    - _Auto-Reveille sur S5, Par Jour du Mois ou Fixé temps du chaque jours_
- [number] **  Par Jour du Mois**
    - _C'est utile pour regler l'jour. Champsvalide est de 1 à 31. (Verification incorrecte sera contre les combinaison de mois/jour/an qui sont pas supportées.) AU..._

## CPU Contrôle Advancée  (2 settings)

- [select] **Cool N' Quiet Support** — Désactiver / Activer★
    - _Enable or Disable Cool and Quiet._
- [select] **Multi CORE Support** — Désactiver / Automatique★
    - _Enable/Disable Multi CORE Support_

## Main  (20 settings)

- [select] **Network Boot:** — Disabled★ / Enabled
- [select] **F12 Boot Menu:** — Disabled★ / Enabled
    - _User could choose if to display 'Press <F12> to display Boot Menu' during POST._
- [select] **SATA Mode:** — AHCI★
    - _SATA Mode help._
- [select] **Touchpad** — I2C★ / PS2
    - _Please make sure I2C driver is installed before select to I2C mode. Otherwise, touchpad will be no function._
- [select] **Wake on LAN:** — Disabled★ / Enabled
- [select] **TBT Wake:** — Disabled / Enabled★
    - _Enable/Disable S3 wake capability of TBT_
- [select] **TBT Wake from S4 Support** — Disabled★ / Enabled
    - _Support TBT wake from S4_
- [select] **USB Wake from S4 Support** — Disabled★ / Enabled
    - _Support USB wake S4_
- [select] **Function key behavior:** — Function Key★ / Media Key
    - _[Media Key]: Perform the media function by default. Hold the <Fn> key to activate F1 to F12. [Function Key]: Activate F1 to F12 by default, Hold the <Fn> key..._
- [select] **Lid Open Resume** — Disabled / Enabled★
    - _System will resume from S3 state by Lid open._
- [select] **Wake on USB while lid closed** — Disabled★ / Enabled
    - _Default disabled. If enabled, USB devices can wake the system, even if the lid is closed._
- [select] **D2D Recovery:** — Disabled / Enabled★
    - _To do Acer disc-to-disc system recovery via Alt+F10 key during POST._
- [select] **xHCI Support:** — Disabled / Enabled★
    - _Enable/Disable external USB3.0 controller._
- [select] **POST Animation & Sound:** — Disabled / Enabled★
    - _Enable/Disable POST Animation & Sound effect._
- [select] **Customize POST animation:** — Disabled★ / Enabled
    - _User can put the favorite file format GIF/JPG in USB storage and rename to AcerLogo.gif/jpg to replace of acer Predator animation.  If user's content is over..._
- [select] **Customize POST Audio:** — Disabled★ / Enabled
    - _Enable/Disable Customize Audio function_
- [select] **Keyboard Backlight Timeout:** — Disabled / Enabled★
    - _Enable/Disable Keyboard Backlight Timeout function_
- [select] **Internal KB Numpad** — Disabled / Enabled★
    - _When the option set to _
- [select] **Fast Boot** — Disabled / Enabled★
    - _Enable/Disable Fast Boot_
- [select] **Real Time Clock reset** — Disabled / Enabled★
    - _Enable/Disable RTC reset hot key(Keep Pressing Power Button 10s)_

## Selects Power-on state for Numlock  (13 settings)

- [select] **Enable or disable the SVM Lock registers.** — IRQ9 / SVM Lock / Enable/Disable Multi CORE Support★
    - _SMM Code Lock_
- [select] **USB PORT 1** — USB PORT 3★ / USB PORT 4
    - _USB PORT 2_
- [select] **AMDAHCI** — Set SATA Configure Type★ / Force Raid Mode
    - _IDE->AMDAHCI_
- [toggle] **SATA Port 0**
    - _SATA Port 0 Enable/Disable_
- [select] **Channel A** — DIMM 1 / Channel B★
    - _DIMM 0_
- [toggle] **DT x1 slot and ExpressCard slot are sharing one GPP port, please choose the configuration based on the board BOM**
    - _ExpressCard Slot_
- [toggle] **DT x1 slot**
    - _Ir Activity Led Enable_
- [toggle] **Enable/Disable Ir Activity Led**
    - _Enable discrete TPM_
- [toggle] **Enable LPC or SPI TPM**
    - _Enable LPC TPM_
- [toggle] **Enable SPI TPM**
    - _Enable firmware TPM_
- [toggle] **Disabled** — Disabled★
- [select] **Azalia** — STIBP Status / Configures ACPI Tables/Features setting.★
    - _AUTO: Auto detect the Azalia codec.  DISABLED: Disable the Azalia controller can be selectable._
- [select] **Enable / Disable Fast Recovery test** — Selects Zip Emulation as FDD or HDD / FDD / HDD★
    - _Zip Emulation Type_

## CPU Related setting  (4 settings)

- [select] **CPU P-State Setting** — Auto★ / Lowest Speed
- [select] **SVM support** — Disabled / Enabled★
    - _Enable/Disable SVM support_
- [select] **SVM Lock** — Disabled / Enabled★
    - _Enable or disable the SVM Lock registers._
- [select] **SMM Code Lock** — Disabled / Enabled★
    - _Enable or disable the SMM code segment/registers._

## PicassoPI-FP5_1.0.0.B  (3 settings)

- [select] **Above 4GB MMIO** — Setup Confirmation\Save changes and then continue to shutdown?★ / 05.32.42
    - _Enable/Disable above 4GB MemoryMappedIO BIOS assignment. It's only available with Uefi Boot Mode._
- [select] **11/05/2020**
    - _Press Esc for boot options_
- [number] **Esc is pressed. Go to boot options.**

## PCI Express Configurations  (1 settings)

- [select] **PSPP Policy** — Disabled / Performance / Balanced-High / Balanced-Low★ / Power Saving / Auto
    - _PCIe speed power policy_

## APU GPP #0 Features  (1 settings)

- [select] **GPP Enabled** — Disabled / Enabled★
    - _To enabled this GPP. AUTO means this port will follow its default implementation._

## APU GPP #1 Features  (1 settings)

- [select] **GPP Enabled** — Disabled / Enabled★
    - _To enabled this GPP. AUTO means this port will follow its default implementation._

## APU GPP #2 Features  (1 settings)

- [select] **GPP Enabled** — Disabled / Enabled★
    - _To enabled this GPP. AUTO means this port will follow its default implementation._

## APU GPP #3 Features  (1 settings)

- [select] **GPP Enabled** — Disabled / Enabled★
    - _To enabled this GPP. AUTO means this port will follow its default implementation._

## APU GPP #4 Features  (1 settings)

- [select] **GPP Enabled** — Disabled / Enabled★
    - _To enabled this GPP. AUTO means this port will follow its default implementation._

## APU GPP #5 Features  (1 settings)

- [select] **GPP Enabled** — Disabled / Enabled★
    - _To enabled this GPP. AUTO means this port will follow its default implementation._

## APU GPP #6 Features  (1 settings)

- [select] **GPP Enabled** — Disabled / Enabled★
    - _To enabled this GPP. AUTO means this port will follow its default implementation._

## Boot Configuration  (3 settings)

- [select] **Numlock** — Off★ / On
    - _Selects Power-on state for Numlock_
- [select] **Fast Recovery** — Disabled★ / Enabled
    - _Enable / Disable Fast Recovery test_
- [select] **PeiGop** — Disabled★ / Enabled
    - _PeiGop function Enable / Disable_

## Peripheral Configuration  (4 settings)

- [select] **Trust Platform Module** — Disabled / Enable discrete TPM / Enable firmware TPM★
    - _Enable/Disable TPM physical presence. Need to reboot when set from disable to enable before selecting TPM Operation._
- [select] **Enable LPC or SPI TPM** — Enable LPC TPM / Enable SPI TPM★
- [select] **Erase fTPM NV for factory reset** — Disabled / Enabled★
    - _Control if need to erase the TPM NV when fTPM factory reset flag set._
- [select] **Azalia** — Disabled / Auto★
    - _AUTO: Auto detect the Azalia codec.  DISABLED: Disable the Azalia controller can be selectable._

## IDE Configuration  (6 settings)

- [select] **SATA** — Disabled / Auto★
    - _AUTO: Auto detect the SATA controller.  DISABLED: Disable the SATA controller_
- [select] **SATA Configure as** — IDE / AHCI★
    - _Set SATA Configure Type_
- [select] **  AHCI supporting as** — Legacy Mode★ / UEFI Mode
    - _Setting AHCI supporting as Native uEFI Mode or Legacy Mode_
- [select] **Force Raid Mode** — Disabled★ / Enabled
- [select] **SATA Port 0** — Disabled / Enabled★
    - _SATA Port 0 Enable/Disable_
- [select] **SATA Port 1** — Disabled / Enabled★
    - _SATA Port 1 Enable/Disable_

## Video Configuration  (2 settings)

- [select] **HDMI Audio** — Disabled / Enabled★
    - _Enable/Disable HDMI Audio_
- [select] **Brightness Control Method** — Video BIOS / VGA driver★
    - _Select Brightness Control Method_

## USB Configuration  (10 settings)

- [select] **EHCI0** — Disabled / Enabled★
    - _AUTO: Auto detect the EHCI controller 0 (Device12 Function 0).  DISABLED: Disable the EHCI controller 0_
- [select] **XHCI0** — Enabled / Disable★
    - _Enable/Disable external USB3.0(Device 10,Function 0) controller._
- [select] **USB BIOS Support** — Disabled / Enabled★ / UEFI Only
    - _USB keyboard/mouse/storage support under UEFI environment_
- [select] **USB2.0** — Disabled / Enabled★
    - _Enable/Disable BIOS support for USB2.0 device_
- [select] **USB PORT 0** — Disabled / Enabled★
    - _Enable/Disable USB Port 0_
- [select] **USB PORT 1** — Disabled / Enabled★
- [select] **USB PORT 2** — Disabled / Enabled★
- [select] **USB PORT 3** — Disabled / Enabled★
- [select] **USB PORT 4** — Disabled / Enabled★
- [select] **USB PORT 5** — Disabled / Enabled★

## Chipset Configuration  (2 settings)

- [select] **PCI Latency Timer** — 32 / 64★ / 96 / 128 / 160 / 192 / 224 / 248
- [toggle] **STIBP Status**
    - _Disable/Enable the Single Thread Indirect Branch Predictor(STIBP)._

## ACPI Table/Features Control  (6 settings)

- [select] **FACP - C2 Latency Value** — Disabled / Enabled★
    - _Value only for ACPI. Select the value for the P_LVL2_LAT field found in the FACP Table where: smaller than 100 = C2 Enabled, Larger than 100 = C2 Disabled_
- [select] **FACP - C3 Latency Value** — Disabled / Enabled★
    - _Value only for ACPI. Select the value for the P_LVL3_LAT field found in the FACP Table where: smaller than 1000 = C3 Enabled, Larger than 1000 = C3 Disabled_
- [select] **FACP - RTC S4 Wakeup** — Disabled / Enabled★
    - _Value only for ACPI. Enable/Disable for S4 Wakeup from RTC_
- [select] **APIC - IO APIC Mode** — Disabled / Enabled★
    - _This item is valid only for WIN2k and WINXP.Also,a fresh install of the OS must occur when APIC Mode is desired.Test the IO ACPI by setting item to Enable.Th..._
- [select] **HPET - HPET Support** — Disabled / Enabled★
    - _High Precision Event Timer is supported in Windows Vista or above. HPET controller should not been seen in Windows XP no matter enable/disable in SCU. If thi..._
- [select] **_OSC Support** — Disabled / Enabled★
    - __OSC Method_

## ￱本パソコンの起動時に、￰  ￱キーボードを￰Numlock ￱状￰  ￱態にするかどうかを設定￰  ￱します。￰                [￱オフ￰]                   ￱起動時に、キーボードを￰Numlock ￱状態にしません。￰                         [￱オン￰]                  ￱起動時に、キーボードを￰Numlock ￱状態にします。￰  (6 settings)

- [select] **￱チャンネル￰ A** — ￱メモリスロット￰ 1 / ￱チャンネル￰ B★
    - _￱メモリスロット￰ 0_
- [toggle] **DT x1 slot and ExpressCard slot are sharing one GPP port, please choose the configuration based on the board BOM**
    - _ExpressCard Slot_
- [toggle] **DT x1 slot**
    - _Ir Activity Led Enable_
- [toggle] **Enable/Disable Ir Activity Led**
    - _Enable discrete TPM_
- [toggle] **￱使用しない￰** — ￱使用しない￰★
- [select] **Enable / Disable Fast Recovery test** — FDD￱または￰ HDD ￱の￰ Zip ￱エミュレーションを選択する￰
    - _Zip￱エミュレーションの種類￰_

## Exit Saving Changes  (1 settings)

- [select] **Keyboard Backlight Timeout:** — CVNi Wi-Fi/BT Switch.★ / Optical Drive: / Enable/Disable Optical Drive / Audio: / Audio Switch. / Speaker & Headphone: / Enable/Disable Speaker & Headphone.
    - _Enable/Disable Keyboard Backlight Timeout function_

## Boot  (2 settings)

- [select] **Boot Mode:** — UEFI★ / Legacy
    - _Set System Boot Mode_
- [select] **Secure Boot:** — Enabled★ / Disabled
    - _Enable or Disable secure boot check_

## LUN de arranque  (2 settings)

- [select] **Configurar número LUN de arranque de destino (0..255).** — Introducir dirección MAC de dispositivo secundario. Utilizar formato XX:XX:XX:XX:XX:XX.★ / Dirección MAC de dispositivo secundario
    - _Dispositivo secundario_
- [select] **Configurar identificación CHAP (hasta 32 caracteres de longitud).** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configurar identificación CHAP (hasta 128 caracteres de longitud)._

## Appuyer sur Page Suivante   - la Page Suivante  (6 settings)

- [select] **+ =rejette des Changements** — =Essentiel de mouvement /  =Choisir des Choix / 0-9 a-f sont des données valides
    - _- =rejette des Changements_
- [select] **S'il vous plait tape votre mot de passe**
    - _S'il vous plait tape votre nouveau mot de passe_
- [select] **Les mots de passe ne sont pas pareils** — Rev. 5.0 / Esc=Exit Menu / F10=Save and Exit / Mot de Passe Invalide! Enter nouvelle chaîneou configurez le mot de passe.
    - _Mauvais mot de passe_
- [select] **NV** — Quitter en Sauvegardant les Modifications / Ok
    - _!!_
- [select] **Setup Warning** — Quitter en Sauvegardant les Modifications★ / Ok
    - _Avis de Configuration_
- [number] **[continuer]**
    - _Changes have been saved after press _

## Horodatage TCP  (6 settings)

- [select] **Cibler comme premier disque dur** — Bus:Périphérique:Fonction★ / Type de puce/Révision.
    - _Activer/Désactiver l'apparition de la cible comme premier disque dur dans le système._
- [select] **IP Version** — Bus:Périphérique:Fonction★ / Type de puce/Révision.
    - _Prise en charge d'IP Version. La modification de ce paramètre réinitialisera tous les champs relatifs à l'adresse IP._
- [select] **Adresse IP** — Bus:Périphérique:Fonction★ / Type de puce/Révision.
    - _Configurer l'adresse IP de la cible._
- [select] **Masque de sous-réseau** — Bus:Périphérique:Fonction★ / Type de puce/Révision.
    - _Configurer le masque du sous-réseau de l'adresse IP._
- [select] **Passerelle par défaut** — Bus:Périphérique:Fonction★ / Type de puce/Révision.
    - _Configurer l'adresse IP de la passerelle par défaut._
- [select] **Serveur DNS secondaire** — Bus:Périphérique:Fonction★ / Type de puce/Révision.
    - _Configurer l'adresse IP du serveur DNS secondaire._

## IP-Adresse des Standard-Gateways konfigurieren  (2 settings)

- [select] **Primäre DNS** — Sekundäre DNS / Sekundäre DNS-IP-Adresse konfigurieren. / iSCSI-Name / Bus:Gerät:Funktion★
- [select] **iSCSI-Name konfigurieren.** — Blinkende LEDs / Bus:Gerät:Funktion★
    - _iSCSI-Name_

## MAC-Adresse  (11 settings)

- [select] **iSCSI-Name konfigurieren.** — Bootprotokolle älterer Geräte / iSCSI-Name konfigurieren. / CHAP-ID / CHAP-ID konfigurieren (bis zu 32 Zeichen lang) / CHAP-ID konfigurieren (bis zu 128 Zeichen lang) / Bus:Gerät:Funktion★
    - _iSCSI-Name_
- [select] **CHAP-ID** — Bootprotokolle älterer Geräte / iSCSI / Bus:Gerät:Funktion★
    - _CHAP-ID konfigurieren (bis zu 32 Zeichen lang)_
- [select] **CHAP-ID konfigurieren (bis zu 128 Zeichen lang)** — CHAP-ID / CHAP-ID konfigurieren (bis zu 32 Zeichen lang) / Bus:Gerät:Funktion★ / Bootprotokolle älterer Geräte / iSCSI
    - _CHAP-ID_
- [select] **CHAP-Kennwort** — Bootprotokolle älterer Geräte / iSCSI / Bus:Gerät:Funktion★
    - _CHAP-Geheimnis konfigurieren (12 – 16 Zeichen lang)_
- [select] **CHAP-Geheimnis konfigurieren (12 – 16 Zeichen lang)** — CHAP-Kennwort / CHAP-Geheimnis konfigurieren (12 – 16 Zeichen lang) / Bus:Gerät:Funktion★
    - _CHAP-Kennwort_
- [select] **Verbinden** — Bootprotokolle älterer Geräte / iSCSI / Bus:Gerät:Funktion★ / TCP-Port / Ziel-TCP.Port-Nummer (1..65535) konfigurieren.
    - _Zielherstellung aktivieren/deaktivieren._
- [select] **Boot-LUN** — Boot-LUN / Ziel-Boot-LUN-Nummer (0..255) konfigurieren. / Sekundäres Gerät / Eingabe der MAC-Adresse des sekundären Geräts. XX:XX:XX:XX:XX:XX-Format verwenden. / Bus:Gerät:Funktion★
    - _Ziel-Boot-LUN-Nummer (0..255) konfigurieren._
- [select] **MAC-Adresse des sekundären Geräts** — Bootprotokolle älterer Geräte / iSCSI / Bus:Gerät:Funktion★
    - _Unabhängiges Zielportal verwenden_
- [select] **Unabhängiges Zielportal verwenden** — Bootprotokolle älterer Geräte / iSCSI / Bus:Gerät:Funktion★
    - _Unabhängiges Zielportal verwenden wenn Multipath I/O aktiviert ist._
- [select] **Unabhängigen Zielnamen verwenden** — Bootprotokolle älterer Geräte / iSCSI / Bus:Gerät:Funktion★
- [select] **Unabhängigen Zielnamen verwenden wenn Multipath I/O aktiviert ist.** — Bootprotokolle älterer Geräte / iSCSI / Bus:Gerät:Funktion★
    - _Firmware-Version der Familie_

## Unité logique de démarrage  (2 settings)

- [select] **Configurer le numéro d'unité logique de démarrage cible (0 à 255).** — Adresse MAC du périphérique secondaire d'entrée. Utiliser le format XX:XX:XX:XX:XX:XX.★ / Adresse MAC du périphérique secondaire
    - _Périphérique secondaire_
- [select] **Configurer la réf. CHAP (jusqu'à 32 caractères).** — ^([0-9]{1,3}.){3}\[0-9]{1,3}|[0-9a-fA-F:]{2,39}$
    - _Configurer la réf. CHAP (jusqu'à 128 caractères)._

## Set or change DASH IP  (6 settings)

- [select] **Realtek UEFI UNDI driver information** — Driver Version: / %s / Driver Released Date:
    - _%s_
- [select] **Device Information**
    - _%s_
- [select] **MAC Address:** — TCP/IP Configuration★ / Configure DASH TCP/IP settings / Provisioning Model / Configure DASH provision settings
    - _%02x:%02x:%02x:%02x:%02x:%02x_
- [select] **PCI Slot:** — Set or change DASH host name / Domain Name
    - _The PCI address of Realtek ethernet controller_
- [select] **RealManage Setup** — Set or change DASH host name★ / Domain Name
    - _Realtek RealManage Setup_
- [number] **Host Configuration**

## Gateway  (6 settings)

- [select] **Driver Name:** — Driver Version: / %s
    - _%s_
- [select] **Device Name:**
    - _%s_
- [select] **Current network address** — Provisioning Model★ / Setup and Configuration / Configure DASH security settings / Host Name
    - _%02x:%02x:%02x:%02x:%02x:%02x_
- [select] **%02d:%02d:%02d** — Set or change DASH host name / Domain Name
    - _Driver Provider:_
- [select] **Configure DASH(Desktop and Mobile Architecture for System Hardware) setting. DASH is a web services-based standard that can support both in-band and out-of-band management.** — Set or change DASH host name★ / Domain Name
    - _Realtek RealManage Setup_
- [number] **Configure DASH host settings**
    - _Host Configuration_

