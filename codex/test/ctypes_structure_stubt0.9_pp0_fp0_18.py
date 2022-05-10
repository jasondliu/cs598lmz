import ctypes

class S(ctypes.Structure):
    x = 1
    _pack_ = 1

S.x = ctypes.c_ulonglong(10)
