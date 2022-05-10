import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

t = T()
t.x = 3
t.y = 4

print(t.x)

class U(ctypes.Union):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

u = U()
u.x = 5
print(u.x)
u.y = 6
print(u.x)

class V(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
    _pack_ = 1

v = V()
v.x = 7
v.y = 8

print(ctypes.sizeof(v))

class W(
