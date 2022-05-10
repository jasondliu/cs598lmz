import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_float()

s = S()

s.x = 3.0
s.y = 4.0

