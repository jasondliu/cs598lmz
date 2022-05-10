import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", ctypes.c_int)]

d = D()
d.d = 42
d.c.a = 10
d.c.b = 20

print d.d, d.c.a, d.c.b

# Test ctypes.CField.from_address

class E(ctypes.Structure):
    _fields_ = [("e", ctypes.c_int)]

e = E()
e.e = 10

f = E.from_address(ctypes.addressof(e))
print f.e

# Test ctypes.CField.from_buffer

class F(ctypes.Structure):
    _fields_ = [("f", ctypes.c_int)]

f = F()
f.f = 10

g = F
