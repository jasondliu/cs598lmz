import _struct
# Test _struct.Struct

def test_Struct():
    # Test _struct.Struct
    import struct

    # Test _struct.Struct
    s = _struct.Struct('i')
    assert s.size == struct.calcsize('i')
    assert s.format == 'i'

    # Test __new__
    s = _struct.Struct('i')
    t = _struct.Struct('i')
    assert s is not t
    assert s == t

    # Test __repr__
    assert repr(s) == "Struct('i')"
    assert repr(t) == "Struct('i')"

    # Test __eq__
    assert s == t
    assert not (s != t)
    assert s != _struct.Struct('h')
    assert not (s == _struct.Struct('h'))

    # Test pack
    assert s.pack(1) == struct.pack('i', 1)
    raises(struct.error, s.pack, 1, 2, 3)

    # Test pack_into
    buf = bytearray(s.size)
    s.pack
