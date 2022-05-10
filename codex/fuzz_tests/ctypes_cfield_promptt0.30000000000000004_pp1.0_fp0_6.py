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

class W(ctypes.Structure):
    _fields_ = [("z", Z),
                ("w", ctypes.c_int)]

x = X()
x.a = 1
x.b = 2

y = Y()
y.x = x
y.y = 3

z = Z()
z.y = y
z.z = 4

w = W()
w.z = z
w.w = 5

print w.z.y.x.a
print w.z.y.x.b
print w.z.y.y
print w.z.z
