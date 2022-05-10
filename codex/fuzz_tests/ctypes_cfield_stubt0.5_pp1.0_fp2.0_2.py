import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('s', S)]

c = C()
print c.s.x
c.s.x = 2
print c.s.x

c.s = S()
print c.s.x
c.s.x = 3
print c.s.x

c = C(s = S(x = 4))
print c.s.x

c = C(s = S())
print c.s.x

c = C(s = S(x = 5))
print c.s.x

c = C(s = S())
print c.s.x

c = C(s = S(x = 6))
print c.s.x
