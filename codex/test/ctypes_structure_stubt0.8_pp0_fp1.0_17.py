import ctypes

class S(ctypes.Structure):
    x = 1
    y = 2
    _fields_ = [("x", ctypes.c_int)]

print(S().x)
print(S().y)
