import ctypes
# Test ctypes.CField
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int, 1)]

print X.a.bit_length
print X.a.offset
print X.a.size

class Y(Structure):
    _fields_ = [("x", X),
                ("b", c_int, 1)]

print Y.x.offset
print Y.b.offset

class Z(Structure):
    _fields_ = [("y", Y),
                ("c", c_int, 1)]

print Z.y.offset
print Z.c.offset
