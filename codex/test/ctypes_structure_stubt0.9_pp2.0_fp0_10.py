import ctypes

class S(ctypes.Structure):
    x = 10
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int),
                ]

