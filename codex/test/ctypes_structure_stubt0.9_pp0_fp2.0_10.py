import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.)
    y = ctypes.c_float(2.)
    z = ctypes.c_float(3.)

s = S()
