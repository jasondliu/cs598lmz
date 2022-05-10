import _struct
# Test _struct.Struct.
def test_struct():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'\x00\x00\x00*') == (42,)
    assert s.unpack_from(b'\x00\x00\x00*', 3) == (42,)
    assert s.unpack_from(memoryview(b'\x00\x00\x00*'), 3) == (42,)
    assert s.unpack_from(bytearray(b'\x00\x00\x00*'), 3) == (42,)
    raises(struct.error, s.unpack_from, b'\x00\x00\x00')
    raises(struct.error, s.unpack_from, b'\x00\x00\x00', 4)
    raises(
