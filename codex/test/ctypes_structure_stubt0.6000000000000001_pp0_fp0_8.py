import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1)
    y = ctypes.c_double(2)
    z = ctypes.c_double(3)

class P(ctypes.Structure):
    _fields_ = [("a", ctypes.c_double),
                ("b", ctypes.c_double),
                ("c", ctypes.c_double)]

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double),
                ("p", P)]

class U(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double),
                ("p", P),
                ("t", T)]

