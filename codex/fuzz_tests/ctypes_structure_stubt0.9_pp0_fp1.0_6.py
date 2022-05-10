import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

print(S.x)
