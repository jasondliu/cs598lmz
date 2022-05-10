import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x, y):
    return x + y

CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
f = CFunc(func)

print(f(1, 2))
print(f(3, 4))

# Test ctypes.POINTER

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT(1, 2)
pp = ctypes.pointer(p)

print(pp.contents.x, pp.contents.y)

# Test ctypes.byref

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT(1, 2)
pp = ctypes.pointer(p)

print
