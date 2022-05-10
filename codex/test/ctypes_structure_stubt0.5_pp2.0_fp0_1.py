import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint(1)
    y = ctypes.c_uint(2)
    z = ctypes.c_uint(3)

s = S()
