import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(x):
    print(x)

CFUNCTYPE(None, c_int)(func)(42)

# Test ctypes.POINTER

from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

p = POINT(1, 2)
print(p.x, p.y)

pp = pointer(p)
print(pp.contents.x, pp.contents.y)

# Test ctypes.byref

from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

p = POINT(1, 2)
print(p.x, p.y)

def func(p):
    p.contents.x = 3
    p.contents.y = 4

func(byref(p))
print(p.x, p.y)

# Test c
