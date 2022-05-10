import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(42)) == (42,)
    assert s.unpack(s.pack(sys.maxint)) == (sys.maxint,)
    assert s.unpack(s.pack(-sys.maxint-1)) == (-sys.maxint-1,)
    raises(struct.error, s.unpack, '\x00\x00\x00')
    raises(struct.error, s.unpack, '\x00\x00\x00\x00\x00')
    raises(struct.error, s.unpack_from, '\x00\x00\x00')
    raises(struct.error, s.unpack_from, '\x00\x00\x00\x00\x00')
    raises(struct.error, s.unpack_from, '\x00\x00\x00', 1)
    raises(struct.error, s.unpack_from, '\x00\x00\x00
