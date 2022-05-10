import ctypes

class S(ctypes.Structure):
    x = 1
    y = 2
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class S2(S):
    z = 3
    _fields_ = [("z", ctypes.c_int)]

class S3(S2):
    _fields_ = [("a", ctypes.c_int)]

