import _struct
# Test _struct.Struct
def test_struct():
    s = _struct.Struct("i")
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'abcdef') == (1633837924,)
    assert s.unpack_from(b'abcdef', 2) == (1633837924,)
    assert s.unpack_from(b'abcdef', 2, 1) == ()
    assert s.unpack_from(b'abcdef'*2, 2) == (1633837924,)
    assert s.unpack_from(b'abcdef'*2, 2, 1) == (1633837924,)
    assert s.unpack_from(b'abcdef'*2, 2, 2) == ()

    s = _struct.Struct("ii")
    assert s.size == 8
    assert s.pack(42, 666) == b'*\x
