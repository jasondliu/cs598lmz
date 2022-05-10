import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float
    y = ctypes.c_float

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)
