import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.0)

s = S()
s.x = 2.0
