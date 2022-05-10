import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16(1)
    y = ctypes.c_int16(2)

s = S()
