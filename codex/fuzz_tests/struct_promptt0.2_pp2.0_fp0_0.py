import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(42)) == (42,)
    assert s.unpack(s.pack(-42)) == (-42,)
    assert s.unpack(s.pack(sys.maxint)) == (sys.maxint,)
    assert s.unpack(s.pack(-sys.maxint-1)) == (-sys.maxint-1,)
    raises(struct.error, s.unpack, s.pack(1.5))
    raises(struct.error, s.unpack, s.pack(1<<100))
    raises(struct.error, s.unpack, s.pack(-1<<100))
    raises(struct.error, s.unpack, s.pack(1<<10000))
    raises(struct.error, s.unpack, s.pack(-1<<10000))
    raises(struct.error, s.unpack, s.pack(1<<1000000))
    raises(struct.error, s.unpack, s.pack(-1<<1
