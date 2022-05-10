import _struct
# Test _struct.Struct

def test_struct_1():
    s = _struct.Struct("i")
    assert s.format == "i"
    assert s.size == 4
    assert s.pack(1) == "\x01\x00\x00\x00"
    assert s.pack_into(buffer("a" * 8), 4, 1) == None
    assert buffer("a" * 8) == "\x00" * 4 + "\x01\x00\x00\x00" + "\x00" * 4
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack_from(s.pack(1) + "abc", 0) == (1,)
    assert s.unpack_from(buffer(s.pack(1) + "abc"), 0) == (1,)
    raises(struct.error, s.unpack_from, "abc")
    raises(TypeError, s.pack_into, "abc", 0, 1)
    raises(TypeError, s.unpack_from, "abc", 0, 1)
    raises(
