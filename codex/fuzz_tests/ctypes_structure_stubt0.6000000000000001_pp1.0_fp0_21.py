import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p

s = S()
print(s.x)
