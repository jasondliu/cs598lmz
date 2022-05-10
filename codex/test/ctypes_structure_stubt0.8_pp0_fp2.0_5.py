import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S(x=5, y=6)
p = ctypes.pointer(s)

