import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

print S.x
print S.y
print S().x
print S().y
