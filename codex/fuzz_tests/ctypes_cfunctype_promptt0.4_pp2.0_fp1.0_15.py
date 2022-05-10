import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a struct parameter

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

lib.set_value.argtypes = ctypes.c_int, ctypes.POINTER(X)
lib.set_value.restype = ctypes.c_int

x = X()
x.a = 42

lib.set_value(1, x)
print x.a

# call a function with a struct return value

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

lib.point.restype = POINT

p = lib.point(1, 2)
print p.x, p.y

# call a function with a struct return value and a struct parameter

lib.point_add.argtypes = POINT, POINT
lib.point
