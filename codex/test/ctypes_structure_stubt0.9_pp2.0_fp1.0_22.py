import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    foo = ctypes.c_void_p()

