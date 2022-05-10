import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

s = S(1, 2)
print(s.x)
print(s.y)

s.x = 3
s.y = 4
print(s.x)
print(s.y)
