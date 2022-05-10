import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class S3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    def __init__(self, x):
        self.x = x

class S4(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    def __new__(self, x):
        return ctypes.Structure.__new__(self)

class S5(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    def __new__(self, x):
        return ctypes.Structure.__new__(self, x)

class S6(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    def __new__(self, x):
        return ctypes.Structure.__new__(self, x.value)


