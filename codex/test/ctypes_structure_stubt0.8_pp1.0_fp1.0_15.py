import ctypes

class S(ctypes.Structure):
    x = ctypes.Structure
    y = ctypes.Structure
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
