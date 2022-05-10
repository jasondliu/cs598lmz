import _struct
# Test _struct.Struct

def test_struct_pack():
    s = _struct.Struct("i")
    assert s.size == 4
    assert s.pack(12345) == b"\x39\x30\x00\x00"
    assert s.pack(0xffffffff) == b"\xff\xff\xff\xff"
    assert s.pack(-1) == b"\xff\xff\xff\xff"
    assert s.pack(0) == b"\x00\x00\x00\x00"
    assert s.pack(0xffffffffffffffff) == b"\xff\xff\xff\xff"
    assert s.pack(-1) == b"\xff\xff\xff\xff"
    assert s.pack(0) == b"\x00\x00\x00\x00"
    raises(OverflowError, s.pack, 0x100000000)
    raises(OverflowError, s.pack, -0x100000000)
    raises(OverflowError, s.pack, 0x10000000000000000)
