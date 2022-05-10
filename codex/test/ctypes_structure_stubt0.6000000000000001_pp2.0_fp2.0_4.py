import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)

s = S()
s.x = 100
print(s.x)
