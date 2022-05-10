import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x01\x00\x00\x00', 0) == (1,)
    assert s.unpack(b'\x01\x00\x00\x00', 1) == (0,)
    assert s.unpack(b'\x01\x00\x00\x00', 2) == (0,)
    assert s.unpack(b'\x01\x00\x00\x00', 3) == (0,)
    assert s.unpack(b'\x01\x00\x00\x00', 4) == (0,)
    assert s.unpack(b'\x01\x00\x00\x00', 5) == (0,)
    assert s.unpack(b'\x01\x00\x00\x00', 6) == (0,)
