import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

class D(S):
    y = ctypes.c_int

class E(D):
    pass

print S.x, S.y
print D.x, D.y
print E.x, E.y
print

s = S(1, 2)
print s.x, s.y
d = D(1, 2)
print d.x, d.y
e = E(1, 2)
print e.x, e.y
print

S.x = ctypes.c_int * 2
S.y = ctypes.c_int * 2
print S.x, S.y
print D.x, D.y
print E.x, E.y
print

s = S(1, 2)
print s.x, s.y
d = D(1, 2)
print d.x, d.y
e = E(1, 2)
print e.x,
