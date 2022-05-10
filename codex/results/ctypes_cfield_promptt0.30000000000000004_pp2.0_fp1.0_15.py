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

print(Z.y.x.a)
print(Z.y.x.b)
print(Z.y.y)
print(Z.z)

print(Z.y.x.a.offset)
print(Z.y.x.b.offset)
print(Z.y.y.offset)
print(Z.z.offset)

print(Z.y.x.a.size)
print(Z.y.x.b.size)
print(Z.y.y.size)
print(Z.z.size)

print(Z.y.x.a.__
