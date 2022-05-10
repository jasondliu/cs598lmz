import ctypes

class S(ctypes.Structure):
    x = 5
    _fields_ = [("a", ctypes.c_char_p), ("b", ctypes.c_char_p)]

assert S.x == 5
