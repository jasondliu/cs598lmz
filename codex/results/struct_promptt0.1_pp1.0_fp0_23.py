import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x01\x00\x00\x00', 0) == (1,)
    assert s.unpack(b'\x01\x00\x00\x00', 1) == ()
    assert s.unpack(b'\x01\x00\x00\x00', 2) == ()
    assert s.unpack(b'\x01\x00\x00\x00', 3) == ()
    assert s.unpack(b'\x01\x00\x00\x00', 4) == ()
    assert s.unpack(b'\x01\x00\x00\x00', 5) == ()
    assert s.unpack(b'\x01\x00\x00\x00', 6) == ()
    assert s.unpack(b'\x01\x00\
