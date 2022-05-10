import _struct
# Test _struct.Struct compatibility with struct module

FORMAT = "hhl"
SIZE = _struct.calcsize(FORMAT)

def test_unpack():
    s = _struct.Struct(FORMAT)
    if _sys.byteorder != "big":
        s = s.newbyteorder()
    assert s.unpack(b"1234") == (0x12, 0x34, 0)
    assert s.unpack(b"1234567") == (0x12, 0x34, 0x567)
    assert s.unpack(b"123456789") == (0x12, 0x34, 0x56789)

def test_unpack_from():
    s = _struct.Struct(FORMAT)
    if _sys.byteorder != "big":
        s = s.newbyteorder()
    assert s.unpack_from(b"1234") == (0x12, 0x34, 0)
    assert s.unpack_from(b"1234567") == (0x12, 0x34, 0x567)

