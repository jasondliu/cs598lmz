import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

y = Y()
y.x.a = 1
y.x.b = 2
y.y = 3

print y.x.a, y.x.b, y.y

# Test ctypes.CField.from_address
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

z = Z()
z.a = 1
z.b = 2

z_a = ctypes.c_int.from_address(ctypes.addressof(z))
z_b = ctypes.c_int.from_address(ctypes.addressof(z) + ctypes.sizeof(ctypes.c_int))

