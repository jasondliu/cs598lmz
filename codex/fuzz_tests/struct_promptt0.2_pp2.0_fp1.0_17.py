import _struct
# Test _struct.Struct.__new__()

def test_new():
    # Test that _struct.Struct() can be called with a format string.
    s = _struct.Struct('i')
    assert s.format == 'i'
    assert s.size == _struct.calcsize('i')
    assert s.pack(42) == _struct.pack('i', 42)
    assert s.unpack(_struct.pack('i', 42)) == (42,)
    assert s.unpack_from(_struct.pack('i', 42), 0) == (42,)
    assert s.unpack_from(_struct.pack('i', 42) + b'x', 0) == (42,)
    assert s.unpack_from(_struct.pack('i', 42) + b'x', 1) == ()
    assert s.unpack_from(_struct.pack('i', 42) + b'x', 2) == ()
    assert s.unpack_from(_struct.pack('i', 42) + b'x', 3) == ()
    assert s.unpack_from(_struct.pack('i',
