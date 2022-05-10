import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_char
    z = ctypes.c_int
    w = ctypes.c_char

