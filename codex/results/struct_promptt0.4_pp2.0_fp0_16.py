import _struct
# Test _struct.Struct

def test_struct(fmt, expected):
    s = _struct.Struct(fmt)
    assert s.size == struct.calcsize(fmt)
    assert s.format == fmt
    s2 = _struct.Struct(s)
    assert s2.size == s.size
    assert s2.format == s.format
    assert s2.unpack(s.pack(*expected)) == expected
    assert s2.unpack_from(s.pack(*expected)) == expected
    assert s2.unpack_from(s.pack(*expected), 0) == expected
    assert s2.unpack_from(s.pack(*expected), 0) == expected
    assert s2.unpack_from(buffer(s.pack(*expected)), 0) == expected

def test_struct_unpack_from(fmt, expected):
    s = _struct.Struct(fmt)
    assert s.unpack_from(s.pack(*expected), 0) == expected
    assert s.unpack_from(s.pack(*expected), 1) == expected
    assert s
