import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test1():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int),
                    ('y', ctypes.c_int),
                    ('z', ctypes.c_int)]

    assert type(S.x) is ctypes.CField
    assert type(S.y) is ctypes.CField
    assert type(S.z) is ctypes.CField

    s = S(0, 1, 2)
    assert type(s.x) is int
    assert type(s.y) is int
    assert type(s.z) is int

def test2():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int),
                    ('y', ctypes.c_int),
                    ('z', ctypes.c_int)]

    assert type(S.x) is ctypes.CField
    assert type(S.y) is ctypes.CField
    assert type(S.z) is ctypes.CField

    s =
