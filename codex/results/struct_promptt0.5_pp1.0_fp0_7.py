import _struct
# Test _struct.Struct with a format string and no buffer
def test_struct_no_buf():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x01\x00\x00\x00'[::-1]) == (16777216,)
    assert s.unpack_from(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00'[::-1]) == (16777216,)
    raises(struct.error, s.pack, 1.0)
    raises(struct.error, s.pack, '1')
    raises(struct.error, s.unpack, b'\x01\x00\x00')
    raises(struct.error, s.un
