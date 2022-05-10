import _struct
# Test _struct.Struct.

def test_struct_module():
    import _struct
    f = _struct.Struct("i")
    assert f.size == 4
    assert f.format == "i"
    assert f.pack(12345) == "\x39\x30\x00\x00"
    assert f.unpack("\x39\x30\x00\x00") == (12345,)
    raises(TypeError, f.unpack, "123")
    raises(TypeError, f.unpack, "12345")
    raises(TypeError, f.unpack, "1234567")
    raises(TypeError, f.unpack, "12345678")

    f = _struct.Struct("ii")
    assert f.size == 8
    assert f.format == "ii"
    assert f.pack(1, 2) == "\x01\x00\x00\x00\x02\x00\x00\x00"
    assert f.unpack("\x01\x00\x00\x00\x02\x00\x00\x
