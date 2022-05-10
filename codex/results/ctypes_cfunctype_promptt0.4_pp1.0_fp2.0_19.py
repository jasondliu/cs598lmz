import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

restype = ctypes.c_int
argtypes = (ctypes.c_int, ctypes.c_int)

f = lib.bar
f.restype = restype
f.argtypes = argtypes

f = ctypes.CFUNCTYPE(restype, argtypes)(f)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

f = lib.bar2
f.restype = restype
f.argtypes = (ctypes.POINTER(X),)

f = ctypes.CFUNCTYPE(restype, ctypes.POINTER(X))(f)

# Test ctypes.CFUNCTYPE with callbacks

f = lib.foo
f.argtypes = (ctypes.c_int, ctypes.c_int)
f.restype = ctypes.c_int
