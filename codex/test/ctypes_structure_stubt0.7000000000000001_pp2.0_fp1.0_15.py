import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char
    _fields_ = [("x", x), ("y", ctypes.c_int)]

ctypes.sizeof(S())
