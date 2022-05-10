import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.POINTER(S)

s = S()
