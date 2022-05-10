import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Structure):
    _fields_ = [("a", S),
                ("b", S)]

t = T()
t.a.x = 1
t.a.y = 2
t.b.x = 3
t.b.y = 4

print t.a.x, t.a.y, t.b.x, t.b.y

t.a = t.b

print t.a.x, t.a.y, t.b.x, t.b.y

t.a.x = 5

print t.a.x, t.a.y, t.b.x, t.b.y
