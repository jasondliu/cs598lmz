import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
print(type(s.x))
print(type(ctypes.c_int))
