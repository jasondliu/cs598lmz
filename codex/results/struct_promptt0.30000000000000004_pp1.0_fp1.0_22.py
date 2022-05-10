import _struct
# Test _struct.Struct

def test_struct_unpack():
    # Test _struct.Struct.unpack()
    s = _struct.Struct('i')
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x00\x00\x00\x01') == (1,)
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x00\x00\x00\x01') == (1,)
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x00\x00\x00\x01') == (1,)
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack(b'\x00\x00\x00\x01') == (1,)
    assert s.unpack
