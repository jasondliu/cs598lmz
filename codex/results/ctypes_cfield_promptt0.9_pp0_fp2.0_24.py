import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("foo", ctypes.CField)]

import _ctypes_test
lib = ctypes.CDLL(_ctypes_test.__file__)
f = lib.func
f.restype = ctypes.c_char
print f()
f.restype = ctypes.c_int
print f.restype
