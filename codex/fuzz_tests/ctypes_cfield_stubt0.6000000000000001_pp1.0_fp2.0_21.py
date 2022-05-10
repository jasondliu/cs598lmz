import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

class D(C):
    _fields_ = [('a', ctypes.c_int), ('c', ctypes.c_int), ('b', ctypes.c_int)]

class E(C):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int), ('c', ctypes.c_int)]

c = C()
c.a = 1
c.b = 2

d = D()
d.a = 10
d.c = 20
d.b = 30

e = E()
e.a = 100
e.b = 200
e.c = 300

print(c.a, c.b)
print(d.a, d.b, d.c)
print(e.a, e.b, e.c)
