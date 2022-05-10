import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int


s = S()

s.x = "bad"
print(s.x)
