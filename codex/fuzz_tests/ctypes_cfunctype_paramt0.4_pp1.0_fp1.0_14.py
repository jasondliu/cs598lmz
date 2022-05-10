import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

f = FUNTYPE(func)
print f(1)

#
#
#

from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

def func(p):
    p.x += 1
    return p.x

f = CFUNCTYPE(c_int, POINT)(func)
p = POINT(1, 1)
print f(p)
print p.x
