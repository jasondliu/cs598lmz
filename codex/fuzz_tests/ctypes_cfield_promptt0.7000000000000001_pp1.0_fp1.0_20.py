import ctypes
# Test ctypes.CField and ctypes.Field

import ctypes

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
    ]

class X2(ctypes.Structure):
    _fields_ = [
        (ctypes.CField("a"), ctypes.c_int),
        (ctypes.CField("b"), ctypes.c_int),
    ]

class X3(ctypes.Structure):
    _fields_ = [
        (ctypes.Field("a", ctypes.c_int), ctypes.c_int),
        (ctypes.Field("b", ctypes.c_int), ctypes.c_int),
    ]

class X4(ctypes.Structure):
    _fields_ = [
        (ctypes.CField("a"), ctypes.Field("b", ctypes.c_int)),
    ]

class X5(ctypes.Structure):
    _fields_ = [
        (ctypes.C
