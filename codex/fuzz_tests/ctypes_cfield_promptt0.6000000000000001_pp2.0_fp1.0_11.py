import ctypes
# Test ctypes.CField
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int, 2),
                ("c", c_int, 4),
                ("d", c_int, 1)]

class Y(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int, 2),
                ("c", c_int, 1),
                ("d", c_int, 1)]

class Z(Union):
    _fields_ = [("a", c_int),
                ("b", c_int, 2),
                ("c", c_int, 1),
                ("d", c_int, 1)]

class W(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int, 2),
                ("c", c_int, 1),
                ("d", c_int, 1),
                ("e", c_int, 1)]

class V(Structure):
    _fields_ = [("a", c_
