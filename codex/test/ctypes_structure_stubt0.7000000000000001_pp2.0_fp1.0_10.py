import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

print(S())

S.x = 3

print(S())
