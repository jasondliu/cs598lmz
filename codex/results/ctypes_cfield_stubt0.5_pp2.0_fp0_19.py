import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', S.x)]

print(type(C.x))
print(type(C.x.__class__))
print(type(C.x.__class__.__class__))
print(type(C.x.__class__.__class__.__class__))
print(type(C.x.__class__.__class__.__class__.__class__))
print(type(C.x.__class__.__class__.__class__.__class__.__class__))
print(type(C.x.__class__.__class__.__class__.__class__.__class__.__class__))
print(type(C.x.__class__.__class__.__class__.__class__.__class__.__class__.__class__))
print(type(C.x.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__))
print(type
