import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

x = X()
x.a = 1
x.b = 2

y = Y()
y.x = x
y.y = 3

z = Z()
z.y = y
z.z = 4

print z.y.x.a
print z.y.x.b
print z.y.y
print z.z

print z.y.x.a == 1
print z.y.x.b == 2
print z.y.y == 3
print z.z == 4

print z.y.x.a == z.y.x.b
print z.
