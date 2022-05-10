import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.unpack(s.pack(42)) == (42,)

def test_struct_unpack_iter():
    s = _struct.Struct('ii')
    assert tuple(s.iter_unpack(s.pack(42, 47))) == ((42, 47),)

def test_struct_unpack_iter_bytes():
    s = _struct.Struct('ii')
    assert tuple(s.iter_unpack(b'abcd')) == ((1684234849, 1768842612),)

def test_struct_unpack_iter_buffer():
    import array
    s = _struct.Struct('ii')
    assert tuple(s.iter_unpack(array.array('B', b'abcd'))) == ((1684234849, 1768842612),)

def test_struct_unpack_iter_memoryview():
    s = _struct.Struct('ii')
    assert tuple(s.iter_unpack(memoryview(
