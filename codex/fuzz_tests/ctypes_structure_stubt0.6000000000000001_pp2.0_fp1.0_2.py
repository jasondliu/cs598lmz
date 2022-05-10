import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

S._fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

print S.x
print S.y

s = S()

print s.x
print s.y
