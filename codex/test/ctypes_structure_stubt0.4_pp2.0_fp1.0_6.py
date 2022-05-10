import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 2
    y = ctypes.c_char * 2

s = S()
