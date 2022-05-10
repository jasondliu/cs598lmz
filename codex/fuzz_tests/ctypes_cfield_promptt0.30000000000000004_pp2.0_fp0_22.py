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
w.z.y.x.a = 2
w.z.y.x.b = 3
w.z.y.y = 4
w.z.z = 5
w.w = 6

print(w.z.y.x.a, w.z.y.x.b, w.z.y.y, w.z.z, w.w)

# Test ctypes.CArray
class X(ctypes.
