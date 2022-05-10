import _struct
# Test _struct.Struct

def test_struct():
    import _struct
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'*\x00\x00\x00', 0) == (42,)
    assert s.unpack_from(b'*\x00\x00\x00', 1) == (0,)
    assert s.unpack_from(b'*\x00\x00\x00', 2) == (0,)
    assert s.unpack_from(b'*\x00\x00\x00', 3) == (0,)
    assert s.unpack_from(b'*\x00\x00\x00', 4) == (0,)
