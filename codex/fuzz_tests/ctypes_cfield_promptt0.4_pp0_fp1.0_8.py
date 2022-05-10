import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

    def __init__(self):
        self.x.a = 1
        self.x.b = 2

y = Y()
print y.x.a, y.x.b, y.y

y.x.a = 3
y.x.b = 4
y.y = 5

print y.x.a, y.x.b, y.y

print Y.x.a
print Y.x.b
print Y.y

try:
    print Y.x
except AttributeError, e:
    print e

print Y.x.in_dll(y, "x")
print Y.x.in_dll(y, "y")

try:
    print Y.x.in_dll(y,
