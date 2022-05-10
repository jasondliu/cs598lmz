import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

# This is a bug:
s = S()
