import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_void_p
    z = ctypes.c_void_p

s = S()
