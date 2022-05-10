import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x01\x00\x00\x00', 0) == (1,)
    assert s.unpack(b'\x01\x00\x00\x00', 1) == (16777216,)
    assert s.unpack(b'\x01\x00\x00\x00', 2) == (67108864,)
    assert s.unpack(b'\x01\x00\x00\x00', 3) == (268435456,)
    assert s.unpack(b'\x01\x00\x00\x00', 4) == (1073741824,)
    assert s.unpack(b'\x01\x00\x00\x00', 5) == (4294967296,)
    assert s.unpack(b'\x01\x00\x00
