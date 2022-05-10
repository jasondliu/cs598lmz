import _struct
# Test _struct.Struct

def test_struct_simple():
    import _struct
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'abcdef', 3) == (11259375,)
    assert s.unpack_from(b'abcdef', 3, 1) == (11259375,)
    assert s.unpack_from(memoryview(b'abcdef'), 3) == (11259375,)
    assert s.unpack_from(memoryview(b'abcdef'), 3, 1) == (11259375,)
    assert s.unpack_from(bytearray(b'abcdef'), 3) == (11259375,)
    assert s.unpack_from(bytearray(b'abcdef'), 3, 1) == (11259375,)

def test_struct_format():
    import _struct

