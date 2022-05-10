import _struct
# Test _struct.Struct.pack_into()


def test_pack_into():
    data = bytearray(b'\x00\x00\x00\x00')
    struct.pack_into(">i", data, 0, 1)
    assert data == b"\x00\x00\x00\x01"
    struct.pack_into("=i", data, 0, 0xffffffff)
    assert data == b"\xff\xff\xff\xff"
    struct.pack_into("<i", data, 0, 0x0a0b0c0d)
    assert data == b"\x0d\x0c\x0b\x0a"
    struct.pack_into("=i", data, 0, 0xffffffff)
    assert data == b"\xff\xff\xff\xff"
    struct.pack_into("<i", data, 0, 0x0a0b0c0d)
    assert data == b"\x0d\x0c\x0b\x0a"

    # out of bounds
    raises
