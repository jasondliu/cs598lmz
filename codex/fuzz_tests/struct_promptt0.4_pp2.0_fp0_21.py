import _struct
# Test _struct.Struct, _struct.pack, _struct.unpack

def test_struct():
    # Test _struct.Struct object
    import _struct
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.format == 'i'
    assert s.unpack(s.pack(1924)) == (1924,)
    raises(struct.error, s.pack, 'hi')
    raises(struct.error, s.pack, 0, 0)
    raises(struct.error, s.unpack, 'hi')
    raises(struct.error, s.unpack, 'i')
    raises(struct.error, s.unpack, 'ii')
    raises(struct.error, s.unpack, 'iii')
    raises(struct.error, s.unpack, 'iiii')
    s = _struct.Struct('P')
    assert s.size == _struct.calcsize('P')
    assert s.unpack(s.pack(1924)) == (1924,)
    raises(struct.error, s.pack, 'hi')

