import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# test with a function
def func(arg):
    return arg + 42

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class Y(X):
    _fields_ = [("y", ctypes.c_int)]

def mycmp(a, b):
    return cmp(a[0].value, b[0].value)

def test_callback_in_struct(lib):
    # test a callback in a struct
    class S(ctypes.Structure):
        _fields_ = [("func", CMPFUNC)]

    s = S()
    s.func = C
