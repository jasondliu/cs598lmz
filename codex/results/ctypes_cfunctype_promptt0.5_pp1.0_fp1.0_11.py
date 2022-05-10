import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

# ctypes.c_int, c_float, c_double all have the same size and alignment
# on all platforms, so we can use them to test CFUNCTYPE.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_float)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_double),
                ("b", ctypes.c_int)]

def compare_structs(x, y):
    if x.a < y.a:
        return -1
    if x.a > y.a:
        return 1
    return 0

def compare_ints(x, y):
    x = ctypes.cast(x, ctypes.POINTER(ctypes.c_int))

