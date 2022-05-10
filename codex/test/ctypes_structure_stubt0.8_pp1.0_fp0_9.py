import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    _anonymous_ = ["x"]
