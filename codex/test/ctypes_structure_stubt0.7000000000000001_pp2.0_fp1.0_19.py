import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_float
    z = ctypes.c_short

s = S()
