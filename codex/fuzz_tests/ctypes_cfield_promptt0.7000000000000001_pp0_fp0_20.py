import ctypes
# Test ctypes.CField class

# Import all fields from the ctypes.test module
from ctypes import *

class X(Structure):
    _fields_ = [
        ("a", c_int),
        ("b", c_double),
        ("c", c_int),
        ("d", c_double),
    ]

print X.a.offset
print X.b.offset
print X.c.offset
print X.d.offset

class Y(Structure):
    _fields_ = [
        ("a", c_int),
        ("b", c_double),
        ("n", c_int),
        ("c", c_int * 1),
        ("d", c_double),
    ]

print Y.a.offset
print Y.b.offset
print Y.n.offset
print Y.c.offset
print Y.d.offset

class Z(Structure):
    _fields_ = [
        ("a", c_int),
        ("b", c_double),
        ("n", c_int),
        ("c", c_int * 4
