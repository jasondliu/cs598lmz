import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class B(A):
    _fields_ = [('b', ctypes.c_int)]

class C(A):
    _fields_ = [('c', ctypes.c_int)]

class D(B, C):
    _fields_ = [('d', ctypes.c_int)]

class E(C, B):
    _fields_ = [('e', ctypes.c_int)]

print(D.__mro__)
print(E.__mro__)
print(D.a)
print(D.b)
print(D.c)
print(D.d)
print(E.a)
print(E.b)
print(E.c)
print(E.e)

# check that D and E have the same layout

d = D()
e = E()

d.a = 1
d.b = 2
d.c = 3
d.d = 4


