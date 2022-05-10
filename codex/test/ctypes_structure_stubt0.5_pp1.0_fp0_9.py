import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Structure):
    _fields_ = [("s", S),
                ("a", ctypes.c_char_p),
                ("b", ctypes.c_char_p)]

t = T()
