import _struct
# Test _struct.Struct.__new__

def test_new():
    # Test _struct.Struct.__new__
    s = _struct.Struct('i')
    assert s.format == 'i'
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'*\x00\x00\x00', 0) == (42,)
    assert s.unpack_from(b'*\x00\x00\x00', 1) == ()
    assert s.unpack_from(b'*\x00\x00\x00', 2) == ()
    assert s.unpack_from(b'*\x00\x00\x00', 3) == ()
    assert s.unpack_from(b'*\x00\x00
