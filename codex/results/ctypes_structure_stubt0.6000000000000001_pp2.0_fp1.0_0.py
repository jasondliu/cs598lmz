import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32
    z = ctypes.c_uint64

class S2(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32
    z = ctypes.c_uint32

class S3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_uint32),
                ("y", ctypes.c_uint32),
                ("z", ctypes.c_uint64)]

class S4(ctypes.Structure):
    _fields_ = [("x", ctypes.c_uint32),
                ("y", ctypes.c_uint32),
                ("z", ctypes.c_uint32)]

class S5(ctypes.Structure):
    _fields_ = [("x", ctypes.c_uint32),
                ("y", ctypes.c_uint32),
                ("z", ctypes.c_uint32)]
    _pack_ = 1

class S6(
