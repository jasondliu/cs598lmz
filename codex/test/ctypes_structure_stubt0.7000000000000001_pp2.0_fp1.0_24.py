import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte()
    _fields_ = [("x", ctypes.c_ubyte)]
