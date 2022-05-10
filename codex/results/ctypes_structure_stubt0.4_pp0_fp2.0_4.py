import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class U(ctypes.Union):
    _fields_ = [("s", S), ("v", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("u", U), ("z", ctypes.c_int)]

t = T()
t.u.v = 4
print t.u.s.x
