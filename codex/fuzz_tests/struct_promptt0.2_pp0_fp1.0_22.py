import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x00\x00\x00\x00') == (0,)
    assert s.unpack(b'\xff\xff\xff\xff') == (-1,)
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x00\x00\x00\x00') == (0,)
    assert s.unpack(b'\xff\xff\xff\xff') == (-1,)
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x00\x00\x00\x00') == (0,)
    assert s.unpack(b'\xff\xff\xff
