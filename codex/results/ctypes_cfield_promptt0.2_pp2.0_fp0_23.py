import ctypes
# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_int),
                ("f", ctypes.c_int),
                ("g", ctypes.c_int),
                ("h", ctypes.c_int),
                ("i", ctypes.c_int),
                ("j", ctypes.c_int),
                ("k", ctypes.c_int),
                ("l", ctypes.c_int),
                ("m", ctypes.c_int),
                ("n", ctypes.c_int),
                ("o", ctypes.c_int),
                ("p", ctypes.c_int),
                ("q", ctypes.c
