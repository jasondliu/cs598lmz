import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

s = S(1, 2)
print s.x
print s.y
