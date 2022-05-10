import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()

s = S()
s.x = 0.5
s.y = 2.5

