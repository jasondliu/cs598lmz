import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 3
    _fields_ = [('x', ctypes.c_char * 3)]

s = S()
