import ctypes
# Test ctypes.CField:
from ctypes import *
class X(Structure):
    _fields_ = [
        ("a", c_int),
        ("b", c_int),
        ("c", c_int),
        ("d", c_int),
        ("e", c_int),
        ("f", c_int),
        ("g", c_int),
    ]
    _fields = [
        ("a", c_int, 2),
        ("b", c_int, 2),
        ("c", c_int, 2),
        ("d", c_int, 2),
        ("e", c_int, 2),
        ("f", c_int, 2),
        ("g", c_int, 2),
    ]

# Test ctypes.Union
class Y(Union):
    _fields_ = [
        ("a", c_int),
        ("b", c_int),
        ("c", c_int),
        ("d", c_int),
        ("e", c_int),
        ("f", c_int),
        ("g", c_int
