import _struct
# Test _struct.Struct

def test_struct_unpack_from():
    s = _struct.Struct('i')
    buf = _buffer(b'\0\0\0\0\0\0\0\1')
    assert s.unpack_from(buf, 4) == (1,)

def test_struct_unpack_from_buffer():
    s = _struct.Struct('i')
    buf = _buffer(b'\0\0\0\0\0\0\0\1')
    assert s.unpack_from(buf, 4) == (1,)

def test_struct_unpack_from_unicode():
    s = _struct.Struct('i')
    buf = _buffer(b'\0\0\0\0\0\0\0\1')
    raises(TypeError, s.unpack_from, "not a buffer")

def test_struct_pack_into():
    s = _struct.Struct('i')
    buf = _buffer(b'\0' * 8)
