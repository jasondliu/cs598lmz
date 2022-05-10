import ctypes

class S(ctypes.Structure):
    x = 3
    _fields_ = [("y", ctypes.POINTER(S))]

lib.foo(S())

print("******** array")

class A(ctypes.Array):
    x = 3

lib.foo(A(()))


a = A(())
for i in range(1000):
    a = A((1, 2, 3))

lib.foo(a)
print("******** array")


def g(x):
    return x + 3

class X(ctypes.Array):
    x = 3

class Y(ctypes.Array):
    x = 4

class C(ctypes.Structure):
    _fields_ = [("x", X), ("y", Y)]
    x = 10

class D(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", C)]

b = D(x=1)
b.y.x[g(2)] = 1

lib.foo(b.y)

print("******** recursive")

class R(
