import ctypes

class S(ctypes.Structure):
    x = 123
    _fields_ = [('x', ctypes.c_int)]

S._pack_ = 4
