import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 3
    y = ctypes.c_int * 3

s = S()

