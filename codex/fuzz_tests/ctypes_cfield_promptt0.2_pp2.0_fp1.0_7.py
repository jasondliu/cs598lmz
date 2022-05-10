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
w.e = 1
w.z.y.x.a = 2
w.z.y.x.b = 3
w.z.y.c = 4
w.z.d = 5

print w.e, w.z.y.x.a, w.z.y.x.b, w.z.y.c, w.z.d

w.e = 1
w.z.y.x.a
