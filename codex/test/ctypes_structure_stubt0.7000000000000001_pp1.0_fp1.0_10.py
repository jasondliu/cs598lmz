import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_short
    z = ctypes.c_char

s = S()
