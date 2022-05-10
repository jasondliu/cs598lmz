import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_double

s = S()
a = ctypes.byref(s)
