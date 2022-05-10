import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int, x),
        ('z', ctypes.c_int, x),
    ]

class S2(ctypes.Structure):
    x = ctypes.c_int(1)
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int, x),
        ('z', ctypes.c_int, x),
        ('w', ctypes.c_int, x),
    ]

class S3(ctypes.Structure):
    x = ctypes.c_int(1)
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int, x),
        ('z', ctypes.c_int, x),
        ('w', ctypes.c_int, x),
        ('a', ctypes.c_int, x),
    ]

class S
