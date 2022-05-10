import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_double),
                ("b", ctypes.c_double),
                ("c", ctypes.c_double),
                ("d", ctypes.c_double),
                ("e", ctypes.c_double),
                ("f", ctypes.c_double),
                ("g", ctypes.c_double),
                ("h", ctypes.c_double),
                ("i", ctypes.c_double),
                ("j", ctypes.c_double),
                ("k", ctypes.c_double),
                ("l", ctypes.c_double),
                ("m", ctypes.c_double),
                ("n", ctypes.c_double),
                ("o", ctypes.c_double),
                ("p", ctypes.c_double),
                ("q", ctypes.c_double),
                ("r", ctypes.c
