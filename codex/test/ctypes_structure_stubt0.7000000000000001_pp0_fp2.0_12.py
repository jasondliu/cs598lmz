import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [
        ("y", ctypes.c_char_p),
        ("z", ctypes.c_void_p),
        ("u", ctypes.c_ulong),
    ]

S()
