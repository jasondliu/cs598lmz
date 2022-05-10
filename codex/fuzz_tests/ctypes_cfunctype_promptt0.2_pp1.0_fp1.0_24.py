import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function pointer
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib.spam_func)
assert f(5) == 5

# a function pointer in a structure
class X(ctypes.Structure):
    _fields_ = [("func", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))]
x = X()
x.func = f
assert x.func(6) == 6

# a function pointer in a union
class Y(ctypes.Union):
    _fields_ = [("func", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))]
y = Y()
y.func = f
assert y.func(7) == 7

# a function pointer in an array
array = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_
