import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("x", ctypes.CField(X)),
                ("y", ctypes.c_int)]

y = Y()
z = Z()

y.x.a = 1
y.x.b = 2
y.y = 3

z.x.a = 1
z.x.b = 2
z.y = 3

print y.x.a, y.x.b, y.y
print z.x.a, z.x.b, z.y

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.St
