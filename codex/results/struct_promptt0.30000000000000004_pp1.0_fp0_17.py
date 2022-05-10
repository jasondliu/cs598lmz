import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(42)) == (42,)
    assert s.unpack(s.pack(sys.maxsize)) == (sys.maxsize,)
    assert s.unpack(s.pack(-sys.maxsize-1)) == (-sys.maxsize-1,)

def test_struct_unpack_from():
    s = _struct.Struct('i')
    assert s.unpack_from(s.pack(42), 0) == (42,)
    assert s.unpack_from(s.pack(sys.maxsize), 0) == (sys.maxsize,)
    assert s.unpack_from(s.pack(-sys.maxsize-1), 0) == (-sys.maxsize-1,)
