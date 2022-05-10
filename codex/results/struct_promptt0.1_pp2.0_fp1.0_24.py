import _struct
# Test _struct.Struct

def test_struct():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 0) == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 1) == (0,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 2) == (0,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 3) == (0,)
    assert s.unpack_from(b'\x01\x00\x00\x00',
