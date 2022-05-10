import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    y = ctypes.c_short
    z = ctypes.c_char

