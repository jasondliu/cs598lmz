import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

s = S()
print(s.x)
print(s.y)
