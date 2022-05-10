import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    z = ctypes.CField()
class B(ctypes.Structure):
    _fields_ = [("a", A),
                ("b", ctypes.c_int)]
    c = ctypes.CField()
    d = ctypes.CField()

a = A()
a.x = 1
a.y = 2
a.z = 3

b = B()
b.a = a
b.b = 4
b.c = 5
b.d = 6

print b.a.x, b.a.y, b.a.z, b.b, b.c, b.d

# Test ctypes.Field
class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    z = ctypes.Field()
class D(ctypes.Structure):

