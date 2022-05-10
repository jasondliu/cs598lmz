import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

assert S.x is ctypes.c_int

class T(ctypes.Structure):
    x = ctypes.c_byte
    _fields_ = [("x", ctypes.c_int)]

