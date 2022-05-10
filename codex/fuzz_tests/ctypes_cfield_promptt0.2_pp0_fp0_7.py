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

w = W()
w.z.y.x.a = 1
w.z.y.x.b = 2
w.z.y.y = 3
w.z.z = 4
w.w = 5

print w.z.y.x.a, w.z.y.x.b, w.z.y.y, w.z.z, w.w

w.z.y.x.a = 6
w.z
