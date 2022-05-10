import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    pass

s = S()

s.x = 10

print(s.x)
