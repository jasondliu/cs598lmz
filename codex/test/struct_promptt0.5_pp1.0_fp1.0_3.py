import _struct
# Test _struct.Struct

def test_pack_unpack():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(10) == b'\n\x00\x00\x00'
    assert s.unpack(b'\n\x00\x00\x00') == (10,)
    raises(struct.error, s.pack, 1, 2)
    raises(struct.error, s.unpack, b'abc')
    raises(struct.error, s.unpack, b'\x00\x00\x00\x00')

def test_iter_unpack():
    s = _struct.Struct('iii')
    assert s.size == 12
    data = b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
    assert list(s.iter_unpack(data)) == [(1, 2, 3)]
