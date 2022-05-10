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

class V(ctypes.Structure):
    _fields_ = [("w", W),
                ("v", ctypes.c_int)]

x = X(1, 2)
y = Y(x, 3)
z = Z(y, 4)
w = W(z, 5)
v = V(w, 6)

print v.w.z.y.x.a
print v.w.z.y.x.b
print v
