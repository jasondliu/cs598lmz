import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

s = S()
