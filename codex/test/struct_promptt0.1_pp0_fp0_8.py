import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(42)) == (42,)
    assert s.unpack(s.pack(sys.maxint)) == (sys.maxint,)
    assert s.unpack(s.pack(-sys.maxint-1)) == (-sys.maxint-1,)
    raises(struct.error, s.unpack, 'ii')
    raises(struct.error, s.unpack, 'i'*(sys.maxint//2))
    raises(struct.error, s.unpack, 'i'*(sys.maxint//2+1))
    raises(struct.error, s.unpack, 'i'*(sys.maxint//2-1))
    raises(struct.error, s.unpack, 'i'*(sys.maxint//2+2))
    raises(struct.error, s.unpack, 'i'*(sys.maxint//2-2))
