import _struct
# Test _struct.Struct()

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(1)) == (1,)
    assert s.unpack(s.pack(0)) == (0,)
    assert s.unpack(s.pack(-1)) == (-1,)
    assert s.unpack(s.pack(sys.maxint)) == (sys.maxint,)
    assert s.unpack(s.pack(-sys.maxint-1)) == (-sys.maxint-1,)
    raises(struct.error, s.unpack, s.pack(1.0))
    raises(struct.error, s.unpack, s.pack(1+1j))
    raises(struct.error, s.unpack, s.pack(None))
    raises(struct.error, s.unpack, s.pack('abc'))
    raises(struct.error, s.unpack, s.pack(u'abc'))
    raises(struct.error, s.unpack, s.pack(object()))
