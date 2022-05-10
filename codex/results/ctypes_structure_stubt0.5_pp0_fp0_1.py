import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

s = S(1, 2)
print s.x, s.y
print s.x.__class__, s.y.__class__
s.x = 3
s.y = 4
print s.x, s.y
print s.x.__class__, s.y.__class__
