import _struct
# Test _struct.Struct.__new__

def test_new():
    # Test that the constructor works
    s = _struct.Struct('i')
    assert s.format == 'i'
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00') == (1,)

    # Test that the constructor accepts a format string
    s = _struct.Struct('i')
    assert s.format == 'i'
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00') == (1,)

    # Test that the
