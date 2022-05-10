import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print cmp_func(1, 2)

# Test ctypes.byref

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = POINT(1, 2)

print point.x, point.y

ctypes.byref(point).contents.x = 3
ctypes.byref(point).contents.y = 4

print point.x, point.y

# Test ctypes.cast

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]


