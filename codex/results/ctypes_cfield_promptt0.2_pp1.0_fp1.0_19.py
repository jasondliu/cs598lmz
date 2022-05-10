import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField)]

d = D()
print d.a, d.b, d.c.a, d.c.b
d.a = 1
d.b = 2
d.c.a = 3
d.c.b = 4
print d.a, d.b, d.c.a, d.c.b

# Test ctypes.CField.from_address
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField.from_address(ctypes.addressof(d)))]

e = E()
print e.a, e
