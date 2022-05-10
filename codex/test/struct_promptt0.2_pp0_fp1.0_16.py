import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('abc')
    except TypeError:
        pass
    else:
        raise TestFailed("expected TypeError")

def test_struct_pack():
    s = _struct.Struct('i')
    try:
        s.pack()
    except TypeError:
        pass
    else:
        raise TestFailed("expected TypeError")
    try:
        s.pack(1, 2)
    except TypeError:
        pass
    else:
        raise TestFailed("expected TypeError")
    try:
        s.pack(1.0)
    except TypeError:
        pass
    else:
        raise TestFailed("expected TypeError")
    try:
        s.pack(1, 2, 3)
    except TypeError:
        pass
    else:
        raise TestFailed("expected TypeError")

def test_struct_unpack():
    s = _struct.Struct('i')
