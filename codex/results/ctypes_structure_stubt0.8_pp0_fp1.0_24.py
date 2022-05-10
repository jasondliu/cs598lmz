import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('y', ctypes.c_int)]
    pass

s = S(1, 2)
print s.x, s.y
