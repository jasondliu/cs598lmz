import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short
    z = ctypes.c_short
    w = ctypes.c_short

S._fields_ = [
    ("x", ctypes.c_short * 4),
    ("y", ctypes.c_short * 4),
    ("z", ctypes.c_short * 4),
    ("w", ctypes.c_short * 4),
]

s = S()
