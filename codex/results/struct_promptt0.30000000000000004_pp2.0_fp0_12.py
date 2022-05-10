import _struct
# Test _struct.Struct.__new__
def test_new():
    s = _struct.Struct('i')
    assert s.format == 'i'
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'*\x00\x00\x00', 0) == (42,)
    assert s.unpack_from(b'*\x00\x00\x00', 0, 1) == (42,)
    assert s.unpack_from(bytearray(b'*\x00\x00\x00'), 0, 1) == (42,)
    raises(TypeError, _struct.Struct, 'i', 'i')
    raises(TypeError, _struct.Struct, 'i', 'i', 'i')
    raises(TypeError,
