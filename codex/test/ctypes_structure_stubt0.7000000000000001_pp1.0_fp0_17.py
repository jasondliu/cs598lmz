import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)
    y = ctypes.c_long(2)
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]


s = S()
