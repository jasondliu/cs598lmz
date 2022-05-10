import _struct
# Test _struct.Struct

def test_struct_simple():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(10) == b'\n\x00\x00\x00'
    assert s.unpack(b'\n\x00\x00\x00') == (10,)
    assert s.unpack_from(b'\n\x00\x00\x00') == (10,)
    assert s.unpack_from(b'\n\x00\x00\x00', 0) == (10,)
    raises(struct.error, s.unpack_from, b'\n\x00\x00\x00', 1)
    raises(struct.error, s.unpack_from, b'\n\x00\x00')
    raises(struct.error, s.unpack_from, b'\n\x00\x00', 1)
    raises(struct.error, s.unpack_from, b'\n\x00\x00', 1, 1)
    raises(struct
