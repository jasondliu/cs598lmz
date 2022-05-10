import _struct
# Test _struct.Struct

def test_struct():
    import _struct
    assert _struct.Struct('i').size == 4
    assert _struct.Struct('i').pack(42) == b'*\x00\x00\x00'
    assert _struct.Struct('i').unpack(b'*\x00\x00\x00') == (42,)
    assert _struct.Struct('i').unpack_from(b'abcdef', 3) == (11259375,)
    assert _struct.Struct('i').unpack_from(b'abcdef', 3, 2) == (11259375,)
    assert _struct.Struct('i').unpack_from(memoryview(b'abcdef'), 3) == (11259375,)
    assert _struct.Struct('i').unpack_from(memoryview(b'abcdef'), 3, 2) == (11259375,)
    assert _struct.Struct('i').unpack_from(bytearray(b'abcdef'), 3) == (11259375,)
    assert _struct.Struct('i').unpack_from(bytear
