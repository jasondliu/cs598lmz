import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('I I')
    b = s.pack(1, 2)
    assert s.unpack(b) == (1, 2)
    assert s.unpack(b, 0) == (1, 2)
    assert s.unpack(b, 1) == (0, 2)
    assert s.unpack(b, 2) == (0, 0)
    assert s.unpack(b, 3) == (0, 0)
    assert s.unpack(b, 4) == (0, 0)
    assert s.unpack(b, 5) == (0, 0)
    assert s.unpack(b, 6) == (0, 0)
    assert s.unpack(b, 7) == (0, 0)
    assert s.unpack(b, 8) == (0, 0)
    raises(struct.error, s.unpack, b, 9)
    raises(struct.error, s.unpack, b, -1)
