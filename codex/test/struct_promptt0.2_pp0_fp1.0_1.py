import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct("i")
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(1)) == (1,)

