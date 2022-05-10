import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class T(ctypes.Structure):
    _fields_ = [("u", ctypes.c_int),
                ("v", ctypes.c_int),
                ("w", ctypes.c_int)]

class U(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

class V(ctypes.Structure):
    _fields_ = [("u", ctypes.c_int),
                ("v", ctypes.c_int),
                ("w", ctypes.c_int)]

class W(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

