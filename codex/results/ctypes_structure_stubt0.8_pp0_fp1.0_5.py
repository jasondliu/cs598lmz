import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

print str(S.x)

print repr(S.x)
print repr(list(S.x))

class X(ctypes.Union):
    y = ctypes.c_int

print repr(X.y)
print repr(list(X.y))
