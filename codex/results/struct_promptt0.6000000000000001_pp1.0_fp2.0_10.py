import _struct
# Test _struct.Struct.
def test_struct():
    import array
    s = _struct.Struct('i')
    # Test __repr__.
    assert repr(s) == 'Struct(format="i")'
    # Test __eq__.
    assert s == _struct.Struct('i')
    assert not s == _struct.Struct('b')
    # Test format.
    assert s.format == 'i'
    raises(AttributeError, "s.format = 'b'")
    # Test size.
    assert s.size == 4
    # Test pack.
    assert s.pack(7 ** 2) == b'\x00\x00\x00\x49'
    # Test pack_into.
    a = array.array('b', [0, 0, 0, 0])
    s.pack_into(a, 0, 7 ** 3)
    assert bytes(a) == b'\x00\x00\x01\xC1'
    raises(struct.error, s.pack, True)
    raises(struct.error, s.pack, 7.5)
