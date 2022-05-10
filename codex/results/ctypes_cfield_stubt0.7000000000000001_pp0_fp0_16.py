import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_int():
    assert issubclass(ctypes.c_int, ctypes.CField)
    assert issubclass(ctypes.c_int, ctypes.c_int)
    assert issubclass(ctypes.c_int, ctypes.c_long)
    assert not issubclass(ctypes.c_int, ctypes.py_object)

def test_c_long():
    assert issubclass(ctypes.c_long, ctypes.CField)
    assert issubclass(ctypes.c_long, ctypes.c_int)
    assert issubclass(ctypes.c_long, ctypes.c_long)
    assert not issubclass(ctypes.c_long, ctypes.py_object)

def test_c_void_p():
    assert issubclass(ctypes.c_void_p, ctypes.CField)
    assert not issubclass(ctypes.c_void_p, ctypes.c_int)
    assert not issubclass(ctypes.c
