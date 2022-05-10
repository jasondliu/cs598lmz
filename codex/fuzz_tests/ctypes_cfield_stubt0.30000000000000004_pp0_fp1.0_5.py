import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', C)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(D))]

s = S()
c = C()
d = D()
e = E()

s.x = 42
c.x = s
d.x = c
e.x = d

print e.x.x.x.value
