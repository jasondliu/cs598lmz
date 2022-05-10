import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test():
    class C(ctypes.Structure):
        _fields_ = [('a', ctypes.c_int),
                    ('b', ctypes.c_int)]

    class CSubclass(C):
        _fields_ = [('c', ctypes.c_int),
                    ('d', ctypes.c_int),
                    ('e', ctypes.c_int),
                    ('f', ctypes.c_int),
                    ('g', ctypes.c_int),
                    ('h', ctypes.c_int)]

    x = CSubclass.a
    assert isinstance(x, ctypes.CField)
    assert x.__name__ == 'a'
    assert x.offset == 0
    x = CSubclass.b
    assert isinstance(x, ctypes.CField)
    assert x.__name__ == 'b'
    assert x.offset == ctypes.sizeof(ctypes.c_int)
    x = CSubclass.c
    assert isinstance(x, ctypes.CField)
    assert
