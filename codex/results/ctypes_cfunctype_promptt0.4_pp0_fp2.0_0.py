import ctypes
# Test ctypes.CFUNCTYPE and ctypes.Structure
from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

def add_point(p):
    return POINT(p.x + 1, p.y + 1)

AddPoint = CFUNCTYPE(POINT, POINT)(add_point)

p = POINT(1, 2)
p = AddPoint(p)
print p.x, p.y

# Test ctypes.byref and ctypes.pointer
from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

def add_point(p):
    p.x += 1
    p.y += 1
    return 0

AddPoint = CFUNCTYPE(c_int, POINTER(POINT))(add_point)

p = POINT(1, 2)
AddPoint(byref(p))
print p.x, p.y

