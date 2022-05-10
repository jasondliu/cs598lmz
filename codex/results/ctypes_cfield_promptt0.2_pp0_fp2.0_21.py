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
d.a = 1
d.b = 2
d.c.a = 3
d.c.b = 4
print d.a, d.b, d.c.a, d.c.b

# Test ctypes.CField.from_param
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField)]

e = E()
e.a = 1
e.b = 2
e.c.a = 3
e.c.b = 4

def test_param(x):
    print x.
