import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_ubyte, 2),
        ("b", ctypes.c_ubyte, 3),
        ("c", ctypes.c_ubyte, 2),
        ("d", ctypes.c_ubyte, 3),
        ]

class S2(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_ubyte, 2),
        ("b", ctypes.c_ubyte, 3),
        ("c", ctypes.c_ubyte, 2),
        ("d", ctypes.c_ubyte, 3),
        ("e", ctypes.c_ubyte, 8),
        ]

class S3(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_ubyte, 2),
        ("b", ctypes.c_ubyte, 3),
        ("c", ctypes.c_ubyte, 2),
       
