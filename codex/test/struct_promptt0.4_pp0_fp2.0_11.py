import _struct
# Test _struct.Struct.
def test_struct():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.pack_into(b'12345678', 4, 42) == None
    assert b'1234*\x00\x00\x0078' == b'12345678'
    assert s.unpack_from(b'1234*\x00\x00\x0078', 4) == (42,)
    raises(struct.error, s.pack)
    raises(struct.error, s.pack, 'foo')
    raises(struct.error, s.pack, 1, 2, 3)
    raises(struct.error, s.unpack, b'123')
    raises(struct.error, s.unpack_from, b'123', 1)
