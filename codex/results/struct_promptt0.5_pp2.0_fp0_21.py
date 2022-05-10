import _struct
# Test _struct.Struct

def test_struct():
    s = _struct.Struct("i")
    assert s.size == 4
    assert s.pack(1) == b"\x01\x00\x00\x00"
    assert s.unpack(b"\x01\x00\x00\x00") == (1,)
    assert s.unpack_from(b"\x01\x00\x00\x00", 0) == (1,)
    assert s.unpack_from(b"\x00\x01\x00\x00\x00", 1) == (1,)
    assert s.pack_into(b"12345678", 2, 1) == None
    assert b"12345678" == b"\x31\x32\x01\x00\x00\x00\x37\x38"
    raises(struct.error, s.pack_into, b"12345678", 3, 1)
    raises(struct.error, s.pack_into, b"12345678", 2, 1, 2)
    raises(struct
