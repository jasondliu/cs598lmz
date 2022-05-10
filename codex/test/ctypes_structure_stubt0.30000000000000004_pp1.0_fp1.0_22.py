import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32()
    y = ctypes.c_int32()

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int32),
                ("y", ctypes.c_int32)]

class U(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int32),
                ("y", ctypes.c_int32),
                ("z", ctypes.c_int32)]

class V(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int32),
                ("y", ctypes.c_int32),
                ("z", ctypes.c_int32),
                ("w", ctypes.c_int32)]

