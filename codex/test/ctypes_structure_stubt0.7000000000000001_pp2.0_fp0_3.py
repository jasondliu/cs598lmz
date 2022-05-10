import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(3)


s = S()
