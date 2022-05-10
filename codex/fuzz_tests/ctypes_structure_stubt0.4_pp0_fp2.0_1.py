import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    _anonymous_ = ["x"]

class S2(S):
    _fields_ = [("z", ctypes.c_int)]

class S3(S2):
    _fields_ = [("a", ctypes.c_int)]

class S4(S3):
    _fields_ = [("b", ctypes.c_int)]
    _anonymous_ = ["a"]

class S5(S4):
    _fields_ = [("c", ctypes.c_int)]

class S6(S5):
    _fields_ = [("d", ctypes.c_int)]
    _anonymous_ = ["c"]

class S7(S6):
    _fields_ = [("e", ctypes.c_int)]

class S8(S7):
    _fields_ = [("f", ctypes.c_int)]
    _anonymous_ = ["e
