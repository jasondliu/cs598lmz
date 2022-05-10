import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test a simple function call
#

# int func(int)
func = lib.func
func.argtypes = ctypes.c_int,
func.restype = ctypes.c_int

print func(42)

#
# Test a function call with a structure
#

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

# int func2(Point)
func2 = lib.func2
func2.argtypes = Point,
func2.restype = ctypes.c_int

print func2(Point(42, 1729))

#
# Test a function call with a pointer to a structure
#

# int func3(Point *)
func3 = lib.func3
func3.argtypes = ctypes.POINTER(Point),
func3.restype = ctypes.c_int


