import _struct
# Test _struct.Struct

def test_struct():
    s = Struct('i')
    assert s.size == _struct.calcsize('i')
    assert s.format == 'i'
    assert s.pack(42) == _struct.pack('i', 42)
    assert s.unpack(_struct.pack('i', 42)) == (42,)

    s = Struct('ii')
    assert s.size == _struct.calcsize('ii')
    assert s.format == 'ii'
    assert s.pack(42, 47) == _struct.pack('ii', 42, 47)
    assert s.unpack(_struct.pack('ii', 42, 47)) == (42, 47)

    s = Struct('iif')
    assert s.size == _struct.calcsize('iif')
    assert s.format == 'iif'
    assert s.pack(42, 47, 3.14) == _struct.pack('iif', 42, 47, 3.14)
    assert s.unpack(_struct.pack('iif', 42, 47, 3.14)) == (42
