import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("c", C),
                ("d", ctypes.c_int)]

d = D()
d.c.a = 1
d.c.b = 2
d.d = 3

print d.c.a, d.c.b, d.d

# Test ctypes.CField.from_address

class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

e = E()
e.a = 1
e.b = 2

f = E.from_address(ctypes.addressof(e))
f.a = 3
f.b = 4

print e.a, e.b

# Test ctypes.CField.from_buffer

class F(ctypes.Structure
