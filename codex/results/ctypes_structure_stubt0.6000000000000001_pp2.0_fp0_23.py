import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short

class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_short),
                ("y", ctypes.c_short)]

class S3(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short
    _pack_ = 4

class S4(ctypes.Structure):
    _fields_ = [("x", ctypes.c_short),
                ("y", ctypes.c_short)]
    _pack_ = 4

class S5(ctypes.Structure):
    _fields_ = [("x", ctypes.c_short),
                ("y", ctypes.c_short)]
    _pack_ = 4
    def __init__(self):
        self.x = self.y = 1

class S6(ctypes.Structure):
    _fields_ = [("x", ctypes.c_short),
                ("y", ctypes.c_short)]
   
