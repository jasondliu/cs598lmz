import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct("i")
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(0)) == (0,)
    assert s.unpack(s.pack(-1)) == (-1,)
    assert s.unpack(s.pack(sys.maxint)) == (sys.maxint,)
    assert s.unpack(s.pack(-sys.maxint-1)) == (-sys.maxint-1,)
    raises(struct.error, s.unpack, "")
    raises(struct.error, s.unpack, "x")
    raises(struct.error, s.unpack, "xx")
    raises(struct.error, s.unpack, "xxx")
    raises(struct.error, s.unpack, "xxxx")
    raises(struct.error, s.unpack, "xxxxx")
    raises(struct.error, s.unpack, "xxxxxx")
