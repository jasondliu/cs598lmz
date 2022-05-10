import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [("x", ctypes.c_int)]

print(S.x)
print(S.x.offset)
print(S.x.size)
