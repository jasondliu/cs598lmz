import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int8()

class S2(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int8)]

