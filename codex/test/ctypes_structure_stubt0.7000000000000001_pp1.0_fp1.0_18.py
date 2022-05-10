import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.23)
    y = ctypes.c_float(4.56)

s = S()
