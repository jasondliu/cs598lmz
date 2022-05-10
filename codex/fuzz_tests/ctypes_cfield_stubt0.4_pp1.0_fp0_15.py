import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('s', S)]

s = S()
s.x = 42
c = C()
c.s = s

print(c.s.x)

c.s.x = 43
print(s.x)
