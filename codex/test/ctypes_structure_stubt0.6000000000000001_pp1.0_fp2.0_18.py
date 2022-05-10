import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_char_p
    z = ctypes.c_ulong

s = S()
