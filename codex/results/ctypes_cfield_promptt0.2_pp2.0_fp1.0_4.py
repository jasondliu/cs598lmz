import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", X)]

y = Y()
y.x.a = 1
y.x.b = 2
y.y.a = 3
y.y.b = 4

print y.x.a, y.x.b, y.y.a, y.y.b

# Test ctypes.CField.from_address
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

z = Z()
z.a = 1
z.b = 2

z2 = ctypes.CField.from_address(ctypes.addressof(z), Z, "z2")
z2.a = 3
z2.b = 4

print z.a, z.
