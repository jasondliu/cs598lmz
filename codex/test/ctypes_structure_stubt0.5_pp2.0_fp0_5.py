import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int * 2
    y = ctypes.c_int * 2

s = S()
