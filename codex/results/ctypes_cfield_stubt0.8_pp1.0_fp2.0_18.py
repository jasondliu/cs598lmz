import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert issubclass(ctypes.CField, ctypes.Field)
    assert issubclass(ctypes.CField, ctypes.CFuncPtr)

def test_c_field():
    try:
        class S(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
            x = ctypes.c_double
    except TypeError:
        pass
    else:
        raise AssertionError

def test_c_field_subsubclass():
    class S1(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    class S2(S1):
        pass
    try:
        class S3(S1):
            x = ctypes.c_double
    except TypeError:
        pass
    else:
        raise AssertionError
    try:
        class S3(S2):
            x = ctypes.c_double
    except TypeError:
       
