import _struct
# Test _struct.Struct

def test_struct_i():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 0) == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 1) == ()
    assert s.unpack_from(b'\x01\x00\x00\x00', 2) == ()
    assert s.unpack_from(b'\x01\x00\x00\x00', 3) == ()
    assert s.unpack_from(b'\x01\x00\x00\x00', 4) == ()
