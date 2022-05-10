import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x01\x00\x00\x00'*2) == (1, 1)
    assert s.unpack(b'\x01\x00\x00\x00'*3) == (1, 1, 1)
    assert s.unpack(b'\x01\x00\x00\x00'*4) == (1, 1, 1, 1)
    assert s.unpack(b'\x01\x00\x00\x00'*5) == (1, 1, 1, 1, 1)
    assert s.unpack(b'\x01\x00\x00\x00'*6) == (1, 1, 1, 1, 1, 1)
    assert s.unpack(b'\x01\x00\x00\x00'*7) == (
