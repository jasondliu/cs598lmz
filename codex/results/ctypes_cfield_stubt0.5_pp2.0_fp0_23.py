import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('s', S)]

class D(ctypes.Structure):
    _fields_ = [('s', S)]

class E(ctypes.Structure):
    _fields_ = [('s', S)]

class F(ctypes.Structure):
    _fields_ = [('s', S)]

c = C()
d = D()
e = E()
f = F()

print(c.s.x)

c.s.x = 1
d.s.x = 2
e.s.x = 3
f.s.x = 4

print(c.s.x)
print(d.s.x)
print(e.s.x)
print(f.s.x)

print(C.s.offset)
print(D.s.offset)
print(E.s.offset)
print(F.s.offset)

print(C.s.size)
print(D.s.size)
print(E.s
