import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)

s = S()
s.x = 1.0

