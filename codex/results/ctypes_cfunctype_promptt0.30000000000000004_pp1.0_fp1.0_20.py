import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is called with a function pointer as first argument.
# The function pointer is called with a pointer to a structure as
# first argument, and an integer as second argument.
# The function pointer must return an integer.
# The function must return the sum of the return values of the
# function pointer.

# The structure is defined as:

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

# The function is called with a pointer to a Point structure, and
# an integer.  It must return the sum of the x and y fields of the
# structure, and the integer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(Point), ctypes.c_int)

def func(x, y):
    return x.contents.x + x.contents.y + y

