import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    b = s.pack(1)
    assert s.unpack(b) == (1,)

def test_struct_unpack_from():
    s = _struct.Struct('i')
    b = s.pack(1)
    assert s.unpack_from(b) == (1,)

def test_struct_unpack_from_offset():
    s = _struct.Struct('ii')
    b = s.pack(1, 2)
    assert s.unpack_from(b, 4) == (2,)

def test_struct_unpack_from_buffer():
    s = _struct.Struct('i')
    b = s.pack(1)
    assert s.unpack_from(buffer(b)) == (1,)

def test_struct_unpack_from_bytearray():
    s = _struct.Struct('i')
    b = s.pack(1)
    assert s.unpack_from(bytearray(b
