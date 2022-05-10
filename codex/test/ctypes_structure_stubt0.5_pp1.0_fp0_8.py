import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_char * 2

class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_char * 2)]

class S3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    y = ctypes.c_char * 2

class S4(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_char * 2)]
    z = ctypes.c_char * 2

class S5(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_char * 2)]
    _fields_ += [("z", ctypes.c_char * 2)]

