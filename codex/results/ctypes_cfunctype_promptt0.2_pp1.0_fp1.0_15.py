import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)

print cmp_func(1, 2)

# Test ctypes.POINTER

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = POINT(1, 2)

p_point = ctypes.POINTER(POINT)(point)

print p_point.contents.x
print p_point.contents.y

# Test ctypes.pointer

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

point = POINT(1, 2)

p_
