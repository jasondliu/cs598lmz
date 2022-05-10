import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(42)) == (42,)
    assert s.unpack(s.pack(sys.maxint)) == (sys.maxint,)
    assert s.unpack(s.pack(-42)) == (-42,)
    assert s.unpack(s.pack(-sys.maxint-1)) == (-sys.maxint-1,)
    raises(struct.error, s.unpack, s.pack(sys.maxint+1))
    raises(struct.error, s.unpack, s.pack(-sys.maxint-2))
    raises(struct.error, s.unpack, s.pack(2.5))
    raises(struct.error, s.unpack, s.pack(True))
    raises(struct.error, s.unpack, s.pack(False))
    raises(struct.error, s.unpack, s.pack(None))
    raises(struct.error, s.unpack, s.pack([]))
   
