import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

# This works...
s = S()
s.x = 1
