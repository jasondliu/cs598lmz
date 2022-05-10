import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

x = X()
y = Y()

x.a = 1
x.b = 2
y.x = x
y.y = 3

print y.x.a, y.x.b, y.y

y.x.a = 4
y.x.b = 5
y.y = 6

print x.a, x.b, y.y

x.a = 7
x.b = 8
y.y = 9

print y.x.a, y.x.b, y.y

print ctypes.sizeof(X), ctypes.sizeof(Y)

# Test ctypes.CArray

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c
