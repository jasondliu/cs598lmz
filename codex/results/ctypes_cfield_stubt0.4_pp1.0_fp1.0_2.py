import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('f', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('f', ctypes.c_int)]

s = S()
c = C()
d = D()

print(c.f)
print(d.f)

c.f = s.x
d.f = s.x

print(c.f)
print(d.f)

print(type(c.f))
print(type(d.f))
