import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    # Check that the CField class is available
    assert issubclass(ctypes.CField, ctypes.Field)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert issubclass(ctypes.CField, ctypes.c_int)
    assert issubclass(ctypes.CField, ctypes.c_
