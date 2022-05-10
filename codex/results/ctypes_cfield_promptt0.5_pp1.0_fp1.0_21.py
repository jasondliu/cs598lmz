import ctypes
# Test ctypes.CField()

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
    ]

class Y(ctypes.Structure):
    _fields_ = [
        ("x", X),
        ("c", ctypes.c_int),
    ]

class Z(ctypes.Structure):
    _fields_ = [
        ("y", Y),
        ("d", ctypes.c_int),
    ]

class W(ctypes.Structure):
    _fields_ = [
        ("z", Z),
        ("e", ctypes.c_int),
    ]

print(Z.x.a)
print(Z.y.x.a)
print(W.z.y.x.a)
