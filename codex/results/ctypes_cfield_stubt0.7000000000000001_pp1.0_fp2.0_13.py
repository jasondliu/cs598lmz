import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('f', ctypes.CField)]

s = S()
c = C()
c.f = s.x
s.x = 4
print(s.x, c.f)
s.x = 6
print(s.x, c.f)
