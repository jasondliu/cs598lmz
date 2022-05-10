import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S(1, 2)
print(s.x)
print(s.y)

print()

class point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = point(1, 2)
print(p.x)
print(p.y)

print(point.x)
print(point.y)

print()

class point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = point(1, 2)
print(p.x)
print(p.y)

print()

class point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = point(1, 2)
print(p.x)
print(
