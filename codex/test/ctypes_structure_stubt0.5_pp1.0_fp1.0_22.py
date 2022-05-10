import ctypes

class S(ctypes.Structure):
    x = ctypes.c_bool

s = S()
s.x = True
