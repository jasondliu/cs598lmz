import ctypes
# Test ctypes.CFUNCTYPE and ctypes.Structure
from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

def add_point(p):
    return POINT(p.x + 1, p.y + 1)

