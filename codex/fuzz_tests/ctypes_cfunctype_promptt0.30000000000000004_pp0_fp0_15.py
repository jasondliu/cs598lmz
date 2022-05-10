import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# A simple function

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("myfunc", lib))
func.restype = ctypes.c_int
func.argtypes = (ctypes.c_int,)

print func(42)

# A function with a structure as parameter

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

func = ctypes.CFUNCTYPE(ctypes.c_int, Point)(("myfunc2", lib))
func.restype = ctypes.c_int
func.argtypes = (Point,)

print func(Point(1, 2))

# A function with a structure as parameter and result

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y",
