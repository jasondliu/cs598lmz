import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("c", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("d", ctypes.c_int)]

class W(ctypes.Structure):
    _fields_ = [("z", Z),
                ("e", ctypes.c_int)]

w = W()
w.z.y.x.a = 1
w.z.y.x.b = 2
w.z.y.c = 3
w.z.d = 4
w.e = 5

print w.z.y.x.a
print w.z.y.x.b
print w.z.y.c
print w.z.d
print w.e

print w.z.y.x.a ==
