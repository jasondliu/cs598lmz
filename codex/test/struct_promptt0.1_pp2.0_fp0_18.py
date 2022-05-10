import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x01\x00\x00\x00'*2) == (1, 1)
    assert s.unpack(b'\x01\x00\x00\x00'*2, 4) == (1,)
    assert s.unpack(b'\x01\x00\x00\x00'*2, 8) == ()
    assert s.unpack(b'\x01\x00\x00\x00'*2, 4, 1) == ()
    assert s.unpack(b'\x01\x00\x00\x00'*2, 4, 2) == (1,)
    assert s.unpack(b'\x01\x00\x00\x00'*2, 4, 3) == (1, 1)
