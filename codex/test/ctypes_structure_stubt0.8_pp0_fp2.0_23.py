import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    _fields_ = [("x", ctypes.c_short),
                ("pad", ctypes.c_char*6)]

s = S()
