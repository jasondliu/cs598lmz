import ctypes
# Test ctypes.CField

import ctypes

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    _anonymous_ = ["b"]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("x", X)]
    _anonymous_ = ["x"]

class Z(ctypes.Structure):
    _fields_ = [("x", X), ("y", Y)]
    _anonymous_ = ["x", "y"]

class XX(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    _anonymous_ = ["b"]

class YY(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("x", XX)]
    _anonymous_ = ["x"]

class ZZ(ctypes.Structure):
    _fields_ = [("x", XX), ("y",
