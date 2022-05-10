import _struct
# Test _struct.Struct.

def test_struct(fmt, expected):
    s = _struct.Struct(fmt)
    assert s.size == s.size
    assert s.format == fmt
    assert s.unpack(s.pack(*expected)) == expected
    assert s.unpack_from(s.pack(*expected), 0) == expected
    assert s.unpack_from(s.pack(*expected), 0) == expected
    assert s.unpack_from(buffer(s.pack(*expected)), 0) == expected
    assert s.unpack_from(bytearray(s.pack(*expected)), 0) == expected
    assert s.unpack_from(memoryview(s.pack(*expected)), 0) == expected
    assert s.unpack_from(memoryview(bytearray(s.pack(*expected))), 0) == expected
    assert s.unpack_from(memoryview(buffer(s.pack(*expected))), 0) == expected
    assert s.unpack_from(memoryview(buffer(bytearray(s.pack(*expected)))), 0) == expected

