import struct, sys, binascii, uuid

src, dst = sys.argv[1], sys.argv[2]
target_name = "Setup"
patches = {0x24E: 0x01}   # Customize POST animation = Enabled

buf = open(src, "rb").read()
out = bytearray()
pos = 0
while pos < len(buf):
    name_size, data_size = struct.unpack_from("<II", buf, pos)
    rec_len = 4 + 4 + name_size + 16 + 4 + data_size + 4
    rec = bytearray(buf[pos:pos + rec_len])
    name = rec[8:8 + name_size].decode("utf-16-le").rstrip("\0")
    guid = uuid.UUID(bytes_le=bytes(rec[8 + name_size:8 + name_size + 16]))
    attrs = struct.unpack_from("<I", rec, 8 + name_size + 16)[0]
    data_off = 8 + name_size + 16 + 4
    stored_crc = struct.unpack_from("<I", rec, data_off + data_size)[0]
    calc_crc = binascii.crc32(bytes(rec[:data_off + data_size])) & 0xFFFFFFFF
    print(f"{name:8s} guid={guid} attrs={attrs} size=0x{data_size:X} crc_ok={stored_crc == calc_crc}")
    if name == target_name:
        for off, val in patches.items():
            old = rec[data_off + off]
            ctx = rec[data_off + 0x248: data_off + 0x250].hex(" ")
            print(f"  byte 0x{off:X}: {old:02X} -> {val:02X}   (row 0x248: {ctx})")
            rec[data_off + off] = val
        new_crc = binascii.crc32(bytes(rec[:data_off + data_size])) & 0xFFFFFFFF
        struct.pack_into("<I", rec, data_off + data_size, new_crc)
        print(f"  new crc=0x{new_crc:08X}")
    out += rec
    pos += rec_len

open(dst, "wb").write(out)
print(f"wrote {dst} ({len(out)} bytes)")
