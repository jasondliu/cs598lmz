import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("x", ctypes.c_int)]

S.x = 2
