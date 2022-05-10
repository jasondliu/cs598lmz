import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("_x", ctypes.c_int),
                ("_y", ctypes.c_int)]

s = S()
s.x = 10
