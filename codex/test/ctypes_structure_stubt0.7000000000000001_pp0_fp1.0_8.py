import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 4
    _fields_ = [('x', x)]

