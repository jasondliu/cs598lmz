import ctypes

class S(ctypes.Structure):
    x = 3
    _fields_ = [("_padding", ctypes.c_byte * (ctypes.sizeof(ctypes.c_void_p) - x))]


