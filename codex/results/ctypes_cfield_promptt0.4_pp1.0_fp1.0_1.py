import ctypes
# Test ctypes.CField

class CField(ctypes.Structure):
    _fields_ = [
        ("c", ctypes.c_char),
        ("i", ctypes.c_int),
        ("f", ctypes.c_float),
        ("d", ctypes.c_double),
        ("b", ctypes.c_byte),
        ("s", ctypes.c_short),
        ("l", ctypes.c_long),
        ("p", ctypes.c_void_p),
        ("u", ctypes.c_ulong),
        ("h", ctypes.c_ushort),
        ("q", ctypes.c_ubyte),
        ("o", ctypes.c_ulonglong),
        ("x", ctypes.c_longlong),
    ]

class CField2(ctypes.Structure):
    _fields_ = [
        ("c", ctypes.c_char),
        ("i", ctypes.c_int),
        ("f", ctypes.c_float),
        ("d", ctypes.c_double),

