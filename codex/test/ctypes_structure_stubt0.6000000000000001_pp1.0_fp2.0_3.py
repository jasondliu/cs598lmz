import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    _fields_ = [("y", ctypes.c_int)]

