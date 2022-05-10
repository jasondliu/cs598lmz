import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('abc')
    except TypeError:
        pass
    else:
        print('_struct.Struct did not raise TypeError')

def test_struct_unpack():
    s = _struct.Struct('i')
    data = s.pack(1)
    assert s.unpack(data) == (1,)

def test_struct_unpack_from():
    s = _struct.Struct('i')
    data = s.pack(1)
    assert s.unpack_from(data, 0) == (1,)

def test_struct_unpack_from_buffer():
    s = _struct.Struct('i')
    data = s.pack(1)
    assert s.unpack_from(data, 0) == (1,)

def test_struct_pack():
    s = _struct.Struct('i')
    assert s.pack(1) == b'\x01\x00\x00\x00'

def test_struct_pack_into():
   
