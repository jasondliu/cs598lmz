import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('abc')
    except TypeError:
        pass
    else:
        raise TestFailed("didn't raise TypeError")

def test_struct_pack():
    s = _struct.Struct('i')
    try:
        s.pack(1, 2)
    except TypeError:
        pass
    else:
        raise TestFailed("didn't raise TypeError")
    try:
        s.pack()
    except TypeError:
        pass
    else:
        raise TestFailed("didn't raise TypeError")

def test_struct_unpack():
    s = _struct.Struct('i')
    try:
        s.unpack('abc')
    except TypeError:
        pass
    else:
        raise TestFailed("didn't raise TypeError")
    try:
        s.unpack('a')
    except TypeError:
        pass
    else:
        raise TestFailed("didn't raise TypeError")
    try:
        s.unpack('ab')
