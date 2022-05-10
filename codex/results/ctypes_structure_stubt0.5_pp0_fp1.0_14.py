import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 2
    y = ctypes.c_char * 2
    z = ctypes.c_char * 2

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_char * 2),
                ("y", ctypes.c_char * 2)]

class U(ctypes.Structure):
    _fields_ = [("x", ctypes.c_char * 2),
                ("y", ctypes.c_char * 2),
                ("z", ctypes.c_char * 2)]

class V(ctypes.Structure):
    _fields_ = [("x", ctypes.c_char * 2),
                ("y", ctypes.c_char * 2),
                ("z", ctypes.c_char * 2)]
    _anonymous_ = ["z"]

class W(ctypes.Structure):
    x = ctypes.c_char * 2
    y = ctypes.c_char * 2
    z = ctypes.c_char * 2
    _anonymous_
