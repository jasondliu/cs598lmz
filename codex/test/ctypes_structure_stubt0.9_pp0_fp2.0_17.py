import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("a", ctypes.c_byte, 4), 
                ("b", ctypes.c_byte, 2),
                ("c", ctypes.c_byte, 2)]
