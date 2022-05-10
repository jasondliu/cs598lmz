import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
        ("d", ctypes.c_int),
        ("f", ctypes.CField(ctypes.c_int, 0, 2)),
        ("g", ctypes.CField(ctypes.c_int, 2, 2)),
        ("h", ctypes.CField(ctypes.c_int, 4, 2)),
        ("i", ctypes.CField(ctypes.c_int, 6, 2)),
        ("j", ctypes.CField(ctypes.c_int, 0, 3)),
        ("k", ctypes.CField(ctypes.c_int, 3, 3)),
        ("l", ctypes.CField(ctypes.c_int, 6, 3)),
        ("m", ctypes.CField(ctypes.c_int, 1, 3)),
        ("n", ctypes.CField(ctypes.
