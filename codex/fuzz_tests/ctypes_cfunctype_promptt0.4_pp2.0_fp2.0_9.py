import ctypes
# Test ctypes.CFUNCTYPE() with a function that returns a pointer to a struct
# and takes a pointer to a struct as an argument.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

S_p = ctypes.POINTER(S)

f = lib.return_S
f.restype = S_p
f.argtypes = [S_p]

s = S(1)

s2 = f(s)

print s2.contents.a

assert s2.contents.a == s.a
