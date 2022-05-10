import ctypes
# Test ctypes.CField()

from ctypes import *

class X(Structure):
    _fields_ = [
        ("a", c_int),
        ("b", c_int),
        ("c", c_int),
    ]

class Y(Structure):
    _fields_ = [
        (("x", X), ""),
        ("y", c_int),
        ("z", c_int),
    ]

class Z(Structure):
    _fields_ = [
        ("a", c_int),
        (("y", Y), ""),
        ("b", c_int),
    ]

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(Z.y.x.b)
        print(Z.y.y)
    else:
        print(Z.y.x.a)
        print(Z.y.z)
