import ctypes

class S(ctypes.Structure):
    x = 42
    y = (1, 2)
    z = {'a': 3, 'b': 4}

class S2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class S3(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class S5(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p),
                ("b", ctypes.c_int)]

class S6(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char * 5)]

class X(ctypes.Union):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_short)]

