import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print s.y
s.y = 5
print s.y
