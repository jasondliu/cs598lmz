import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y)]

class W(ctypes.Structure):
    _fields_ = [("z", Z)]

w = W()
w.z.y.x.a = 1
w.z.y.x.b = 2
print(w.z.y.x.a, w.z.y.x.b)

# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y
