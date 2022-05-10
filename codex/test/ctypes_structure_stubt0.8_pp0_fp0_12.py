import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_float
    z = ctypes.c_int

s = S()
s.z = -1
s.x = 1.0
s.y = 2.0

