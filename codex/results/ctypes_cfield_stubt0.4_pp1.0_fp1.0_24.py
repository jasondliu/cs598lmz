import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('f', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('f', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('f', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('f', ctypes.c_int)]

s = S(42)
c = C(s.x)
d = D(s.x)
e = E(s.x)
f = F(s.x)

print(c.f)
print(d.f)
print(e.f)
print(f.f)
