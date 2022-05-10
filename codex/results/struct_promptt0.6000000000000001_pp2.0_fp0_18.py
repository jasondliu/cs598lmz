import _struct
# Test _struct.Struct.


def test_struct():
    assert _struct.Struct('i').size == 4
    assert _struct.Struct('i').pack(1) == b'\x01\x00\x00\x00'
    assert _struct.Struct('i').unpack(b'\x01\x00\x00\x00') == (1,)
    assert _struct.Struct('i').pack_into(bytearray(4), 0, 1) == None
    assert bytearray(b'\x01\x00\x00\x00') == bytearray(4)
    assert _struct.Struct('i').unpack_from(b'\x01\x00\x00\x00', 0) == (1,)
    assert _struct.Struct('i').iter_unpack(b'\x01\x00\x00\x00') == [(1,)]
    assert _struct.Struct('i').get_size() == 4
    assert _struct.Struct('i').format == '<i'
    assert _struct.Struct('!i').format
