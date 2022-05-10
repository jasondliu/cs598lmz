import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(ctypes.c_int)

s = S()
