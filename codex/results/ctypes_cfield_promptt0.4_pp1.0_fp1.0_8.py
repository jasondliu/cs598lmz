import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char * 2)]

class Y(ctypes.Structure):
    _fields_ = [("b", X)]

class Z(ctypes.Structure):
    _fields_ = [("c", Y)]

class A(ctypes.Structure):
    _fields_ = [("d", Z)]

a = A()
a.d.c.b.a = b"ab"
print(a.d.c.b.a)

a.d.c.b.a = b"abc"
print(a.d.c.b.a)
