import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def get_name(e):
    return e.__name__

def test_get_name():
    f = get_name(ctypes.CFUNCTYPE(ctypes.c_int))
    assert f is get_name(ctypes.CFUNCTYPE(ctypes.c_int, None))
    assert f is get_name(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,
                                          ctypes.c_double))
    assert f is get_name(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(S),
                                          ctypes.POINTER(S), ctypes.c_double))
    f = get_name(ctypes.POINTER(ctypes.c_int))
    assert f is get_name(ctypes.POINTER(ctypes.c_float))
    assert f is get_name(ctypes.POINTER(ctypes.c_char))
    assert f is get_name(ctypes.POINTER(S))

