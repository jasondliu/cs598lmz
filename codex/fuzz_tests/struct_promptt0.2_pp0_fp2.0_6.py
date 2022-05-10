import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('abc')
    except TypeError:
        pass
    else:
        raise TestFailed, '_struct.Struct() did not raise TypeError'

def test_struct_unpack():
    s = _struct.Struct('i')
    data = s.pack(12345)
    if s.unpack(data) != (12345,):
        raise TestFailed, '_struct.Struct(i).unpack()'

def test_struct_unpack_from():
    s = _struct.Struct('i')
    data = s.pack(12345)
    if s.unpack_from(data) != (12345,):
        raise TestFailed, '_struct.Struct(i).unpack_from()'

def test_struct_pack():
    s = _struct.Struct('i')
    data = s.pack(12345)
    if data != '\x39\x30\x00\x00':
        raise TestFailed, '_struct.Struct
