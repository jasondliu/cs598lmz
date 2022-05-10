import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

class W(ctypes.Structure):
    _fields_ = [("y",ctypes.c_double),("z",ctypes.c_double),("x",ctypes.c_double)]

