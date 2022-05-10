import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("s", S)]

