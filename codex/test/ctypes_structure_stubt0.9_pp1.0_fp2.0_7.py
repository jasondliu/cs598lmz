import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

    _pack_ = 1
