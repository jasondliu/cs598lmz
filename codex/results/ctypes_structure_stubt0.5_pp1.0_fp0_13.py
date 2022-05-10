import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class U(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

class V(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

s = S()
t = T()
u = U()
v = V()

print(s.x, s.y, t.a, t.b, u.x, u.y, v.a, v.b)

s.x = 1
s.y = 2
t.a = 3
t.b = 4
u.x = 5
u.y = 6
v.a = 7
v.b = 8

print(s.x, s.y, t.a, t.b
