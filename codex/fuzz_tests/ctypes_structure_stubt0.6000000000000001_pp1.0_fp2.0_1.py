import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_double()

class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_double)]

class S3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_double),
                ("z", ctypes.c_int),
                ("w", ctypes.c_double),
                ("array", ctypes.c_int * 3)]

class S4(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_double),
                ("z", ctypes.c_int),
                ("w", ctypes.c_double),
                ("array2", ctypes.c_int * 3),
                ("array3", ctypes.c_int * 2 * 3)]

class S5(ctypes.Structure):
    _fields_ = [("
