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
print y.x.b
print y.y

y.x.a = 1
y.x.b = 2
y.y = 3
print y.x.a
print y.x.b
print y.y

# Test ctypes.CField.from_address
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

z = Z()
z.a = 1
z.b = 2

z2 = ctypes.CField.from_address(ctypes.addressof(z), Z, "a")
print z2.a
print z2.b

z2
