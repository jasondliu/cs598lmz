import ctypes

class S(ctypes.Structure):
    x = ()

class E(ctypes.Union):
    x = ()

class X(ctypes.Structure):
    _fields_ = [("e", E)]

class T(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("a", ctypes.c_byte),
        ("b", ctypes.c_byte),
        ("x", X)
        ]

class U(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_byte),
        ("b", ctypes.c_byte),
        ("e", E)
        ]

class V(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_byte),
        ("b", ctypes.c_byte),
        ("c", ctypes.c_byte),
        ("d", ctypes.c_byte),
        ]

try:
    class W(ctypes.Structure):
        _pack_ = 2
        _fields_ = [
            ("a", ctypes
