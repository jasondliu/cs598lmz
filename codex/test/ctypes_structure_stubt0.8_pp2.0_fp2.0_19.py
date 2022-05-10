import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    p = ctypes.POINTER(x)

s = S()

s.x = 42
