import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(a, b):
    return a + b

CFuncType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cfunc = CFuncType(func)

print(cfunc(1, 2))

# Test ctypes.POINTER

import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = Point(1, 2)

print(p.x, p.y)

pp = ctypes.POINTER(Point)

p2 = pp(p)

print(p2.contents.x, p2.contents.y)

# Test ctypes.byref

import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

