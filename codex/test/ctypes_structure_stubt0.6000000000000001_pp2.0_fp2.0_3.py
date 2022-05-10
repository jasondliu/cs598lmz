import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

A = S()

A.x = 1
A.y = 2
A.z = 3

