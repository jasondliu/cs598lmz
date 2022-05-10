import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x00\x00\x00\x00') == (0,)
    assert s.unpack(b'\xFF\xFF\xFF\xFF') == (-1,)
    assert s.unpack(b'\x80\x00\x00\x00') == (-2147483648,)
    assert s.unpack(b'\x7F\xFF\xFF\xFF') == (2147483647,)
    raises(struct.error, s.unpack, b'\x01\x00\x00')
    raises(struct.error, s.unpack, b'\x01\x00\x00\x00\x00')
    s = _struct.Struct('I')
