import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long)]

class U(ctypes.Union):
    _fields_ = [("x", ctypes.c_long)]

