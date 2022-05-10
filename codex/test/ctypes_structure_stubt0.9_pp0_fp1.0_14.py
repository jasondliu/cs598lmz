import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_int()

s = S()
