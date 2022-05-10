import ctypes
# Test ctypes.CField

class A(ctypes.Structure):
    _fields_ = [("one", ctypes.c_int),
                ("two", ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [("field", ctypes.c_int),
                ("a", A),
                ("three", ctypes.c_int),
                ("four", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("b", B)]

class D(ctypes.Structure):
    _fields_ = [("c", C)]

class E(ctypes.Structure):
    _fields_ = [("d", D)]

e = E()
e.d.c.b.a.one = 42

print(e.d.c.b.a.one)
print(e.d.c.b.field)
print(e.d.c.b.two)
print(e.d.c.b.three)
print(e.d.c.b.four)
