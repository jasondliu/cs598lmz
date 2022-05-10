import _struct
# Test _struct.Struct

def test_struct():
    import _struct
    assert _struct.Struct('i')
    assert _struct.Struct('i').size == 4
    assert _struct.Struct('i').pack(42) == '*\x00\x00\x00'
    assert _struct.Struct('i').unpack('*\x00\x00\x00') == (42,)
    assert _struct.Struct('ii').size == 8
    assert _struct.Struct('ii').pack(42, 47) == '*\x00\x00\x00/\x00\x00\x00'
    assert _struct.Struct('ii').unpack('*\x00\x00\x00/\x00\x00\x00') == (42, 47)
    assert _struct.Struct('ii').pack_into('a'*8, 0, 42, 47) == '*\x00\x00\x00/\x00\x00\x00'
    assert _struct.Struct('ii').unpack_from('*\x00\x00\x00/
