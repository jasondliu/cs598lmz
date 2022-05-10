import ctypes
# Test ctypes.CField.

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

print Y.x.a
print Y.x.b
print Y.c

print Y().x.a
print Y().x.b
print Y().c

print Y(x=X(a=3, b=4), c=5).x.a
print Y(x=X(a=3, b=4), c=5).x.b
print Y(x=X(a=3, b=4), c=5).c

print Y(x=X(a=3, b=4), c=5)[0].a
print Y(x=X(a=3, b=4), c=5)[0].b
print Y(x=X(a=3, b=4), c=5)[1]

print
