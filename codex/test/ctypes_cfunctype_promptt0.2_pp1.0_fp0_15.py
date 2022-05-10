import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
from ctypes import *

def func(a, b, c):
    print(a, b, c)

CFUNCTYPE(None, c_int, c_int, c_int)(func)(1, 2, 3)

# Test ctypes.byref

import ctypes
from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

pt = POINT(1, 2)
print(pt.x, pt.y)

pt.x = 3
pt.y = 4
print(pt.x, pt.y)

pt = POINT(5, 6)
print(pt.x, pt.y)

pt.x = 7
pt.y = 8
print(pt.x, pt.y)

# Test ctypes.cast

import ctypes
from ctypes import *

