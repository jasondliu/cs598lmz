import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float

s = S()
s.x = 3
s.y = 4.5

