import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
    ]

class Y(ctypes.Structure):
    _fields_ = [
        ("x", X),
        ("d", ctypes.c_int),
        ("e", ctypes.c_int),
    ]

class Z(ctypes.Structure):
    _fields_ = [
        ("y", Y),
        ("f", ctypes.c_int),
        ("g", ctypes.c_int),
    ]

class A(ctypes.Structure):
    _fields_ = [
        ("z", Z),
        ("h", ctypes.c_int),
        ("i", ctypes.c_int),
    ]

class B(ctypes.Structure):
    _fields_ = [
        ("a", A),
        ("j", ctypes.c_int),
        ("k", c
