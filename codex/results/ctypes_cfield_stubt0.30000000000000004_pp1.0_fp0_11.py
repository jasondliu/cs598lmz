import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(C.x.__class__)
print(C.x.__class__.__base__)
print(C.x.__class__.__base__.__base__)
print(C.x.__class__.__base__.__base__.__base__)
print(C.x.__class__.__base__.__base__.__base__.__base__)
print(C.x.__class__.__base__.__base__.__base__.__base__.__base__)
print(C.x.__class__.__base__.__base__.__base__.__base__.__base__.__base__)
print(C.x.__class__.__base__.__base__.__base__.__base__.__base__.__base__.__base__)
print(C.x.__class__.__base__.__base__.__
