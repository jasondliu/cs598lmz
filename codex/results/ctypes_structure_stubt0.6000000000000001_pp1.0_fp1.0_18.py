import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
    ]

class A(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", S),
    ]

a = A()
a.a = 1
a.b = 2
a.c.x = 3
a.c.y = 4

print(a.a, a.b, a.c.x, a.c.y)
print(a.a, a.b, a.c.x, a.c.y)
print(a.a, a.b, a.c.x, a.c.y)

a.c = S(5, 6)
print(a.c.x, a.c.y)
print(a.c.x, a.c.y)
print(a.c.
