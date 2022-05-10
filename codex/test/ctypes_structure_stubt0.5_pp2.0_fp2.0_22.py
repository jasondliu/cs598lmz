import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
s.x = 5
print(s.x)
