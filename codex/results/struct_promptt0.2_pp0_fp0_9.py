import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x01\x00\x00\x00', 0) == (1,)
    assert s.unpack(b'\x01\x00\x00\x00', 0, 1) == (1,)
    raises(TypeError, s.unpack, b'\x01\x00\x00\x00', 0, 1, 2)
    raises(TypeError, s.unpack, b'\x01\x00\x00\x00', 0, 1, 2, 3)
    raises(TypeError, s.unpack, b'\x01\x00\x00\x00', 0, 1, 2, 3, 4)
    raises(TypeError, s.unpack, b'\x01\x00\x00\x00', 0, 1, 2, 3, 4, 5)
    raises(
