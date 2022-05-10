import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

y = Y()
print y.x.a
y.x.a = 42
print y.x.a

# Test ctypes.CField.from_address
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

z = Z()
z.a = 42
z.b = 24

z2 = Z.from_address(ctypes.addressof(z))
print z2.a, z2.b

# Test ctypes.CField.from_param
class W(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

