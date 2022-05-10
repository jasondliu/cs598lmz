import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16
    y = ctypes.c_uint16

s = S()
