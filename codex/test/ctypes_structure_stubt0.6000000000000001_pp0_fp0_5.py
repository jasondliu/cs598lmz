import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    array = ctypes.c_int * 4

