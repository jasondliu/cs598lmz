import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a simple function

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("func", lib))
assert func(3) == 3

# a function with a struct parameter

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

PointPtr = ctypes.POINTER(Point)

func = ctypes.CFUNCTYPE(ctypes.c_int, PointPtr)(("func", lib))
p = Point(3, 4)
assert func(p) == 7

# a function with a struct parameter and a struct result

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

PointPtr = ctypes.POINTER(Point)

func = ctypes.CFUN
