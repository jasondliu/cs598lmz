import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int64(1)
    _fields_ = [("x", ctypes.c_int64, 63),
                ("y", ctypes.c_int64, 1)]

s = S()
print(s.x)
print(s.y)

s.y = 1
print(s.x)
print(s.y)
