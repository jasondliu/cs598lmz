import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(arg):
    return arg * 2

func.restype = ctypes.c_int

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)

def py_cmp_func(a, b):
    return cmp(a, b)

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("z", ctypes.c_int)]

def py_cmp_struct_func(a, b):
    x = ctypes.cast(a, c
