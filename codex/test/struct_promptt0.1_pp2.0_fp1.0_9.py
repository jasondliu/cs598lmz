import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(42)) == (42,)
    assert s.unpack(s.pack(sys.maxint)) == (sys.maxint,)
    assert s.unpack(s.pack(-sys.maxint-1)) == (-sys.maxint-1,)
    assert s.unpack(s.pack(0)) == (0,)
    assert s.unpack(s.pack(-1)) == (-1,)
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(-2)) == (-2,)
    assert s.unpack(s.pack(2)) == (2,)
    assert s.unpack(s.pack(-3)) == (-3,)
    assert s.unpack(s.pack(3)) == (3,)
    assert s.unpack(s.pack(-4)) == (-4,)
    assert s.unpack(s.pack(4)) == (4,)
