import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

y = Y()
y.x.a = 1
y.x.b = 2
y.y = 3

print y.x.a
print y.x.b
print y.y

print y.x.a == 1
print y.x.b == 2
print y.y == 3

print y.x.a == y.y
print y.x.b == y.y
print y.y == y.x.a
print y.y == y.x.b

print y.x.a == y.x.b
print y.x.b == y.x.a

print y.y == y.x.a == y.x.b
print y.x.a == y.y == y.x.b
