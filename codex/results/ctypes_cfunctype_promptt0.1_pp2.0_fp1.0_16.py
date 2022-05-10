import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function pointer
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib.spam_func)
assert f(1) == 2

# a function pointer in a structure
class X(ctypes.Structure):
    _fields_ = [("fp", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))]

x = X()
x.fp = f
assert x.fp(1) == 2

# a function pointer in a union
class Y(ctypes.Union):
    _fields_ = [("fp", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))]

y = Y()
y.fp = f
assert y.fp(1) == 2

# a function pointer in an array
class Z(ctypes.Structure):
    _fields_ = [("fp", ctypes.
