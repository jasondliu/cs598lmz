import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(42)) == (42,)

def test_struct_unpack_from():
    s = _struct.Struct('i')
    assert s.unpack_from(s.pack(42), 0) == (42,)

def test_struct_unpack_from_buffer():
    s = _struct.Struct('i')
    buf = buffer(s.pack(42))
    assert s.unpack_from(buf, 0) == (42,)

def test_struct_unpack_from_bytearray():
    s = _struct.Struct('i')
    buf = bytearray(s.pack(42))
    assert s.unpack_from(buf, 0) == (42,)

def test_struct_unpack_from_memoryview():
    s = _struct.Struct('i')
    buf = memoryview(s.pack(42))
