import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

S.x = 3
print(S.x)
print(S().x)
