import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int), ("z", ctypes.CField)]

d = D(1, C(2))
v = d.z.x
print(v)
import ctypes
# Test ctypes.Structure with an alignment bigger than a pointer

class A(ctypes.Structure):
    _pack_ = 1

    _fields_ = [("x", ctypes.c_int)]

a = A(1)
print(a.x)
import ctypes

class A(ctypes.Structure):
    _pack_ = 1

    _fields_ = [("x", ctypes.c_int)]

class B(ctypes.Structure):
    _pack_ = 1

    _fields_ = [("a", A),
                ("y", ctypes.c_int)]

b = B()
b.a = A(1)

