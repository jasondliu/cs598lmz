import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(C):
    _fields_ = [("c", ctypes.c_int)]

d = D()
d.a = 1
d.b = 2
d.c = 3
print d.a, d.b, d.c
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(C):
    _fields_ = [("c", ctypes.c_int)]

class E(D):
    _fields_ = [("d", ctypes.c_int)]

e = E()
e.a = 1
e.b = 2
e.c = 3
e.d = 4
print e.a, e.b, e.c, e.d
# Test ctypes.CField

class C
