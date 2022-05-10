import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

s = S()
c = C()
d = D()
e = E()

print(c.x)
print(d.x)
print(e.x)

c.x = s
d.x = s

print(c.x)
print(d.x)
print(e.x)
