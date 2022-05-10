import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    _anonymous_ = ["x"]
    _fields_ = [("y", ctypes.c_int),
                ("z", ctypes.c_int),
                ("w", ctypes.c_int),
                ("x", ctypes.c_int),
                ("x", ctypes.c_int),
                ("x", ctypes.c_int),
                ("x", ctypes.c_int),
                ("x", ctypes.c_int),
                ]

class S2(ctypes.Structure):
    _anonymous_ = ["x"]
    _fields_ = [("y", ctypes.c_int),
                ("z", ctypes.c_int),
                ("w", ctypes.c_int),
                ("x", ctypes.c_int),
                ("x", ctypes.c_int),
                ("x", ctypes.c_int),
                ("x", ctypes.c_int),
                ("x", ctypes.c_int),
                ]

class S3(ctypes
