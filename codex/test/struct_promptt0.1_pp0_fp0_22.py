import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\x00\x00\x00\x00') == (0,)
    assert s.unpack(b'\x00\x00\x00\x01') == (1,)
    assert s.unpack(b'\x00\x00\x00\x02') == (2,)
    assert s.unpack(b'\x00\x00\x00\x03') == (3,)
    assert s.unpack(b'\x00\x00\x00\x04') == (4,)
    assert s.unpack(b'\x00\x00\x00\x05') == (5,)
    assert s.unpack(b'\x00\x00\x00\x06') == (6,)
    assert s.unpack(b'\x00\x00\x00\x07') == (7,)
