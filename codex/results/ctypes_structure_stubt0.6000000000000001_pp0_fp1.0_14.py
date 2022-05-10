import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
S._pack_ = 4

class S2(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
S2._pack_ = 4

class S3(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
S3._pack_ = 4

class S4(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    a = ctypes.c_int
S4._pack_ = 4

class S5(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    a = ctypes.c_int
    b = ctypes.c_int
S5._pack_ = 4

class S6(ctypes.Structure):
    x = ctypes.c_int
