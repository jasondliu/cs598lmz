import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(C.b))]

d = D()
d.a = 1
d.b = 2

print d.a, d.b
print C.from_address(ctypes.addressof(d)).b

# Test ctypes.CField on a pointer

class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(ctypes.POINTER(C).b))]

e = E()
e.a = 1
e.b = 2

print e.a, e.b
print C.from_address(ctypes.addressof(e)).b

# Test ctypes.CField on a pointer to a pointer

class
