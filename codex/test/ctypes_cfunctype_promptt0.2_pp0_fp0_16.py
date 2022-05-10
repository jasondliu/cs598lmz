import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(a, b):
    return a + b

CFunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

f = CFunc(func)
print(f(1, 2))

# Test ctypes.POINTER

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT(1, 2)
print(p.x, p.y)

pp = ctypes.POINTER(POINT)
ppp = pp(p)
print(ppp.contents.x, ppp.contents.y)

# Test ctypes.byref

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

