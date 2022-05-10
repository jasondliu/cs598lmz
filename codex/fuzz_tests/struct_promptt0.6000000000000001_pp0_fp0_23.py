import _struct
# Test _struct.Struct.


def test_struct():
    import _struct
    assert _struct.Struct(b'i').size == 4
    assert _struct.Struct(b'ii').size == 8
    assert _struct.Struct(b'ii').pack(1, 2) == b'\x01\x00\x00\x00\x02\x00\x00\x00'
    assert _struct.Struct(b'ii').unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00') == (1, 2)
    assert _struct.Struct(b'ii').unpack_from(b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00') == (1, 2)
    assert _struct.Struct(b'ii').iter_unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00') == [(1, 2)]
    raises(TypeError,
