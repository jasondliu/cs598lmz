import _struct
# Test _struct.Struct
def test_struct():
    # Simple struct
    s = _struct.Struct("b")
    assert s.size == 1
    assert s.pack(42) == b'*'
    assert s.unpack(b'*') == (42,)

    # More complex struct
    s = _struct.Struct("3s3s3s3s")
    assert s.size == 12
    assert s.pack(b'abc', b'def', b'ghi', b'jkl') == b'abcdefghijkl'
    assert s.unpack(b'abcdefghijkl') == (b'abc', b'def', b'ghi', b'jkl')

    # Alignment
    s = _struct.Struct("10x")
    assert s.size == 10
    assert s.pack() == b'\0' * 10
    assert s.unpack(b'\0' * 10) == ()
    s = _struct.Struct("10b")
    assert s.size == 10
