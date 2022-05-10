import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(b'\0\0\0\1') == (1,)

def test_struct_unpack_buffer():
    s = _struct.Struct('i')
    b = buffer(b'\0\0\0\1')
    assert s.unpack(b) == (1,)

def test_struct_unpack_memoryview():
    s = _struct.Struct('i')
    b = memoryview(b'\0\0\0\1')
    assert s.unpack(b) == (1,)

def test_struct_unpack_bytearray():
    s = _struct.Struct('i')
    b = bytearray(b'\0\0\0\1')
    assert s.unpack(b) == (1,)

def test_struct_unpack_unicode():
    s = _struct.Struct('i')
