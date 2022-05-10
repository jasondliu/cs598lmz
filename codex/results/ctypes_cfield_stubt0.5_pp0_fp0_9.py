import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

s = S()
print(s.x)
s.x = 42
print(s.x)

print(S.x)
print(S.x.__class__)
print(S.x.__class__.__base__)
print(S.x.__class__.__bases__)

print(S.x.__class__.__bases__[0].__bases__)

print(S.x.__class__.__bases__[0].__bases__[0].__bases__)

print(S.x.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__)

print(S.x.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__[0].__bases__)

print(S.x.__class__.__
