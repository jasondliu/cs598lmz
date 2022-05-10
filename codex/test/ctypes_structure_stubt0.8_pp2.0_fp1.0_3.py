import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short()
    y = ctypes.c_int()

s = S()
