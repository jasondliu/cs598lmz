import _struct
# Test _struct.Struct

def test_struct():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(12345) == b'\x39\x30\x00\x00'
    assert s.unpack(b'\x39\x30\x00\x00') == (12345,)
    assert s.unpack_from(b'\x00\x00\x00\x00\x39\x30\x00\x00') == (12345,)
    assert s.unpack_from(b'\x00\x00\x00\x00\x39\x30\x00\x00', 4) == (12345,)
    assert s.unpack_from(b'\x00\x00\x00\x00\x39\x30\x00\x00', 4, 1) == (12345,)
    raises(struct.error, s.unpack_from, b'\x00\x00\x00\x00\x39\x30\x00')
