import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", X),
                ("z", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

x = X()
y = Y()
z = Z()

print x.a
print y.x.a
print z.y.x.a

x.a = 42
y.x.a = 42
z.y.x.a = 42

print x.a
print y.x.a
print z.y.x.a

x.b = 24
y.x.b = 24
z.y.x.b = 24

print x.b
print y.x.b
print z.y.x.b

x.a = 24
