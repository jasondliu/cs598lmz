import _struct
# Test _struct.Struct

def test_struct():
    # Test _struct.Struct
    s = _struct.Struct("i")
    assert s.size == _struct.calcsize("i")
    assert s.pack(12345) == _struct.pack("i", 12345)
    assert s.unpack(_struct.pack("i", 54321)) == (54321,)
    assert s.unpack_from(_struct.pack("i", 1234), 0) == (1234,)
    assert s.unpack_from(_struct.pack("i", 1234) + _struct.pack("i", 5678), 0) == (1234,)
    assert s.unpack_from(_struct.pack("i", 1234) + _struct.pack("i", 5678), 4) == (5678,)
    assert s.unpack_from(_struct.pack("i", 1234) + _struct.pack("i", 5678), 0, 1) == (1234,)
    assert s.unpack_from(_struct.pack("i", 1234) + _struct.pack("i", 5678),
