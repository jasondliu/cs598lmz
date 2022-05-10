import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

print(C.x)
print(C.x.__class__)
print(C.x.__class__.__name__)
print(C.x.__class__ is ctypes.CField)
print()

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int, 2)]

print(C.x)
print(C.x.__class__)
print(C.x.__class__.__name__)
print(C.x.__class__ is ctypes.CField)
print()

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int, (2, 3))]

print(C.x)
print(C.x.__class__)
print(C.x.__class__.__name__)
print(C.x.__class__ is ctypes.CField)
print()

