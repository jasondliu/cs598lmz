import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(0)
    y = ctypes.c_long(0)
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_c_int),
        ]

s = S()
assert s.x.real is 0
assert s.y.real is 0
