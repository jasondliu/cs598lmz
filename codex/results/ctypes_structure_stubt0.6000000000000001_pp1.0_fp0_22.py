import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int8()

class S2(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int8)]

class S3(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int8(3))]

class S4(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int8(1))]

class S5(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int8(2))]

class S6(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int8(256))]

class S7(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int8(257))]

class S8(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int8(255))]

class S9(ctypes.Structure):
    _fields_ = [
