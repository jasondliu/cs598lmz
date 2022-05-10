import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

a = S()
a.x = 3
