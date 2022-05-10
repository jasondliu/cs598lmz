import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    y = ctypes.c_int(0)

class T(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

