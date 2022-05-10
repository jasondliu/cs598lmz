import _struct
# Test _struct.Struct
def test_Struct():
    f = _struct.Struct("<h")
    assert f.size == 2
    raises(struct.error, f.pack, 1, 2)
    raises(TypeError, f.pack, 1, 2, 3, 4)
    assert f.pack(1) == "\x01\x00"
    raises(struct.error, f.pack)
    raises(struct.error, f.pack, ())
    raises(struct.error, f.pack, (1, 2))
    raises(struct.error, f.pack, 0, 1)
    assert f.unpack("\x00\x01") == (256,)
    assert f.unpack_from(buffer("\x00\x01"), 0) == (256,)
    raises(struct.error, f.unpack_from, buffer("\x01\x00"), 1)
    raises(struct.error, f.unpack_from, buffer("\x01"))
    raises(struct.error, f.unpack_from, "abcdef")
