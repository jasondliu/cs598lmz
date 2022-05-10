import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [("x", ctypes.c_int)]

print(S.x)
print(S.x.offset)
print(S.x.size)
print(S.x.__dict__)

s = S()
print(s.x)
s.x = 42
print(s.x)

class D(ctypes.Union):
    x = ctypes.c_int()
    _fields_ = [("x", ctypes.c_int)]

print(D.x)
print(D.x.offset)
print(D.x.size)
print(D.x.__dict__)

d = D()
print(d.x)
d.x = 42
print(d.x)

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    print(X.x)
    print(X.x.offset)
    print(X.x.size)
    print(X.x.__dict__
