import _struct
# Test _struct.Struct

def test_simple_pack():
    s = _struct.Struct("i")
    assert s.size == 4
    assert s.pack(1) == b"\x01\x00\x00\x00"
    assert s.pack(1, 2, 3) == b"\x01\x00\x00\x00"
    raises(struct.error, s.pack)
    raises(struct.error, s.pack, 1, 2, 3, 4)
    raises(struct.error, s.pack, 1.5)
    raises(struct.error, s.pack, "1")

def test_simple_unpack():
    s = _struct.Struct("i")
    assert s.unpack(b"\x01\x00\x00\x00") == (1,)
    assert s.unpack(b"\x01\x00\x00\x00"*2) == (1, 1)
    raises(struct.error, s.unpack, b"")
    raises(struct.error, s.unpack, b"
