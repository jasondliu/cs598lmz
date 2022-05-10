import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_int():
    assert issubclass(ctypes.c_int, ctypes.c_long)
    assert issubclass(ctypes.c_int, ctypes.c_int)
    assert not issubclass(ctypes.c_int, ctypes.c_short)
    assert not issubclass(ctypes.c_int, ctypes.c_longlong)
    assert not issubclass(ctypes.c_int, ctypes.c_float)

def test_c_long():
    assert issubclass(ctypes.c_long, ctypes.c_long)
    assert not issubclass(ctypes.c_long, ctypes.c_short)
    assert not issubclass(ctypes.c_long, ctypes.c_longlong)
    assert not issubclass(ctypes.c_long, ctypes.c_float)

def test_c_short():
    assert issubclass(ctypes.c_short, ctypes.c_short)
    assert not issubclass(ctypes
