import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.0)
    _fields_ = [('x', ctypes.c_float)]

s = S()
