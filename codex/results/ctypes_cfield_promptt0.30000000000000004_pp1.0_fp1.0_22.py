import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(X):
    _fields_ = [("c", ctypes.c_int)]

class Z(Y):
    _fields_ = [("d", ctypes.c_int)]

class A(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y),
                ("z", Z)]

a = A()
a.x.a = 1
a.x.b = 2
a.y.a = 3
a.y.b = 4
a.y.c = 5
a.z.a = 6
a.z.b = 7
a.z.c = 8
a.z.d = 9

assert a.x.a == 1
assert a.x.b == 2
assert a.y.a == 3
assert a.y.b == 4
assert a.y.c == 5
assert a.z.a
