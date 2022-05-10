import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 4

class S1(ctypes.Structure):
    _fields_ = [("x", S), ("y", ctypes.c_uint32)]


s = S1()
