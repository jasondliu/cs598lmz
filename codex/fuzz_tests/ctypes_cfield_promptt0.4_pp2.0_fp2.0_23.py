import ctypes
# Test ctypes.CField

class StructWithCField(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int, 1),
                ("c", ctypes.c_int, 2),
                ("d", ctypes.c_int, 3),
                ("e", ctypes.c_int, 4),
                ("f", ctypes.c_int, 5),
                ("g", ctypes.c_int, 6),
                ("h", ctypes.c_int, 7),
                ("i", ctypes.c_int, 8),
                ("j", ctypes.c_int, 9),
                ("k", ctypes.c_int, 10),
                ("l", ctypes.c_int, 11),
                ("m", ctypes.c_int, 12),
                ("n", ctypes.c_int, 13),
                ("o", ctypes.c_int, 14),
                ("p", ctypes.c_int, 15),
                ("q", ctypes.c_int, 16),

