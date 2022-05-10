import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char*10
    y = ctypes.c_char*10
