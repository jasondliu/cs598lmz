import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    y = ctypes.c_long
    z = 'y'
