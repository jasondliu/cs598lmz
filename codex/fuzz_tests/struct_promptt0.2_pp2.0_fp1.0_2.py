import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('abc')
    except TypeError:
        pass
    else:
        raise TestFailed, 'expected TypeError'

def test_struct_pack():
    s = _struct.Struct('i')
    try:
        s.pack(1, 2)
    except TypeError:
        pass
    else:
        raise TestFailed, 'expected TypeError'

def test_struct_unpack():
    s = _struct.Struct('i')
    try:
        s.unpack('abc')
    except TypeError:
        pass
    else:
        raise TestFailed, 'expected TypeError'

def test_struct_iter_unpack():
    s = _struct.Struct('i')
    try:
        s.iter_unpack('abc')
    except TypeError:
        pass
    else:
        raise TestFailed, 'expected TypeError'

def test_struct_iter_unpack_stopiteration():
    s = _struct.Struct('i')

