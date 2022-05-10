import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
    ]
    _anonymous_ = ["b"]

class D(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
    ]
    _anonymous_ = ["b", "c"]

class E(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
        ("d", ctypes.c_int),
    ]
    _anonymous_ = ["b", "c", "d"]

class F(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c",
