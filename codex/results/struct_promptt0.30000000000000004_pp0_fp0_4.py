import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(42)) == (42,)
    assert s.unpack(s.pack(sys.maxsize)) == (sys.maxsize,)
    assert s.unpack(s.pack(-sys.maxsize-1)) == (-sys.maxsize-1,)
    raises(struct.error, s.unpack, s.pack(1.0))
    raises(struct.error, s.unpack, s.pack(1+2j))
    raises(struct.error, s.unpack, s.pack(None))
    raises(struct.error, s.unpack, s.pack(True))
    raises(struct.error, s.unpack, s.pack(False))
    raises(struct.error, s.unpack, s.pack(""))
    raises(struct.error, s.unpack, s.pack("a"))
    raises(struct.error, s.unpack, s.pack("abc"))
    raises(struct.error, s
