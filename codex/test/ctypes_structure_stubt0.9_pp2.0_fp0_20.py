import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint64

s = S()
print(ctypes.sizeof(s))
print(s.x)
