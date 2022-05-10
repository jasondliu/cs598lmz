import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(ctypes.c_int)

s = S()

s.x = (ctypes.c_int * 3)(0, 1, 2)

print(s.x)
