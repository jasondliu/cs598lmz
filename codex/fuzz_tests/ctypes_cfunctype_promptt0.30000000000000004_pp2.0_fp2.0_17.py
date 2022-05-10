import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function pointer
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib.spam_func)
assert f(5) == 5

# a function pointer in a structure
class X(ctypes.Structure):
    _fields_ = [("fp", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))]

x = X.in_dll(lib, "x")
assert x.fp(6) == 6

# a function pointer in a union
class Y(ctypes.Union):
    _fields_ = [("fp", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))]

y = Y.in_dll(lib, "y")
assert y.fp(7) == 7

# a function pointer as a function argument
f = ctypes.CFUNCTYPE(ctypes.c
