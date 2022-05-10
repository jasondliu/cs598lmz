import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ]

s = S(3, 4)
s.x = 1
s.y = 2
s.z = 3
s.w = 4
s.a = 5
print(s.x, s.y, s.z, s.w, s.a)
