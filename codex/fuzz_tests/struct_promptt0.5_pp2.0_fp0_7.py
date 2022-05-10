import _struct
# Test _struct.Struct

def test_struct(format, expected, *values):
    s = _struct.Struct(format)
    assert s.size == struct.calcsize(format)
    assert s.format == format
    assert s.pack(*values) == struct.pack(format, *values)
    assert s.unpack(s.pack(*values)) == struct.unpack(format, s.pack(*values))
    assert s.iter_unpack(s.pack(*values)) == struct.iter_unpack(format,
                                                                s.pack(*values))
    assert s.unpack_from(s.pack(*values)) == struct.unpack_from(format,
                                                                 s.pack(*values))
    assert s.iter_unpack_from(s.pack(*values)) == struct.iter_unpack_from(format,
                                                                          s.pack(*values))
    assert s.unpack_from(memoryview(s.pack(*values))) == struct.unpack_from(format,
                                                                            s.pack(*values))
    assert s
