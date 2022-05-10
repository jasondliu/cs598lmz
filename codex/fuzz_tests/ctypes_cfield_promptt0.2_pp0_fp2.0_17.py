import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(C, "a", "b"))]

d = D()
d.a = 1
d.b = 2
print d.a, d.b

# Test ctypes.CField.from_address
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(C, "a", "b"))]

e = E()
e.a = 1
e.b = 2
print e.a, e.b

e = E.from_address(ctypes.addressof(d))
print e.a, e.b

# Test ctypes.CField.from_buffer
class F(ctypes.Structure):
    _fields
