import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong(1)
    _pack_ = True

