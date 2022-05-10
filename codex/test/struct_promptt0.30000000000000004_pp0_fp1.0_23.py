import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('abc')
    except TypeError:
        pass
    else:
        print('TypeError expected')

def test_struct_unpack():
    s = _struct.Struct('i')
    data = s.pack(12345)
    assert s.unpack(data) == (12345,)

def test_struct_unpack_from():
    s = _struct.Struct('i')
    data = s.pack(12345)
    assert s.unpack_from(data) == (12345,)

def test_struct_pack_into():
    s = _struct.Struct('i')
    buffer = bytearray(s.size)
    s.pack_into(buffer, 0, 12345)
    assert s.unpack_from(buffer) == (12345,)

def test_struct_iter_unpack():
    s = _struct.Struct('i')
    data = s.pack(12345)
    assert list(s.iter_unpack(data))
