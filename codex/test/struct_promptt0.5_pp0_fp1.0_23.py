import _struct
# Test _struct.Struct.

def test_struct_unpack():
    assert _struct.Struct('i').unpack(b'\x01\x00\x00\x00') == (1,)
    assert _struct.Struct('i').unpack(b'\x00\x00\x00\x01') == (1,)
    assert _struct.Struct('i').unpack(b'\x01\x00\x00\x00') == (1,)
    assert _struct.Struct('i').unpack(b'\x00\x00\x00\x01') == (1,)
    assert _struct.Struct('i').unpack(b'\x00\x00\x00\x01') == (1,)
    assert _struct.Struct('i').unpack(b'\x01\x00\x00\x00') == (1,)
    assert _struct.Struct('i').unpack(b'\x00\x00\x00\x01') == (1,)
