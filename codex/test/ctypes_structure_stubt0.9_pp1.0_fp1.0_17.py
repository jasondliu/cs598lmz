import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32
    y = ctypes.c_int16
    z = ctypes.c_int8

class S3(ctypes.Structure):
    _fields_ = [("w", ctypes.c_int),
                ("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_byte)]


class S4(ctypes.Structure):
    _fields_ = [("w", ctypes.c_int),
                ("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int32)]


class S5(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int8),
                ("w", ctypes.c_byte * 24)]

