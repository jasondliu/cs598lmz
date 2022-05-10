import ctypes

class S(ctypes.Structure):
    x = ctypes.sizeof(ctypes.c_char_p)
    y = ctypes.sizeof(ctypes.c_void_p)

