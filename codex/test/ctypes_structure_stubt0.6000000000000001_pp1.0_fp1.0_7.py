import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float
    y = ctypes.c_float

p = ctypes.POINTER(S)

