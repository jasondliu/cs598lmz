import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test
lib = ctypes.CDLL(_ctypes_test.__file__)

# XXX We only test the CFUNCTYPE() form, not the @CFUNCTYPE
# decorator.  The decorator is only tested in test_decorators.py

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

def test_X_arg(functype):
    func = functype(("test_X_arg", lib), ((1, "x"),))
    assert isinstance(func, functype)

    func.restype = ctypes.c_int
    func.argtypes = (X,)
    x = X()
    x.a, x.b = 6, 7
   
