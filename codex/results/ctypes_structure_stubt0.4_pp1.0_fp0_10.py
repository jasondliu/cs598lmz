import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class T(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class U(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class V(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    def __init__(self):
        self.x = 1

class W(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    def __init__(self, x):
        self.x = x

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    def __init__(self, x, y):
        self.x = x
        self.
