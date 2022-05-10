import ctypes

class S(ctypes.Structure):
    x = None
    _fields_ = [("x", ctypes.POINTER(ctypes.c_int32))]

