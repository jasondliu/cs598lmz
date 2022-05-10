import _struct
# Test _struct.Struct

def test_struct_int():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.iter_unpack(b'*\x00\x00\x00') == [(42,)]
    assert s.iter_unpack(b'*\x00\x00\x00'*2) == [(42,), (42,)]
    assert s.unpack_from(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'*\x00\x00\x00'*2, 4) == (42,)
    raises(struct.error, s.pack, 'foo')
    raises(struct.error, s.pack, 1.2)
    raises(struct.error, s.unpack, b'*\x00\x00')
