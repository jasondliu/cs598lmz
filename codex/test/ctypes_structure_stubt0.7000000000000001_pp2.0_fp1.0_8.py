import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int)]

def test_as_ctypes_type():
    assert S.as_ctypes_type() is ctypes.Structure
    assert S.as_ctypes_type(x=ctypes.c_char) is ctypes.Structure
    assert S.as_ctypes_type(x=ctypes.c_char, a=ctypes.c_char) is ctypes.Structure

def test_as_ctypes_type_union():
    class U(ctypes.Union):
        x = ctypes.c_int
        _fields_ = [('a', ctypes.c_int),
                    ('b', ctypes.c_int)]

    assert U.as_ctypes_type() is ctypes.Union
    assert U.as_ctypes_type(x=ctypes.c_char) is c
