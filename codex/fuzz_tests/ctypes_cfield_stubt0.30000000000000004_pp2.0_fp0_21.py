import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(C.x.__class__)
print(type(C.x))
print(type(C.x) is ctypes.CField)
print(type(C.x) is ctypes.Field)
print(type(C.x) is ctypes.CField)
print(type(C.x) is ctypes.CField)
print(type(C.x) is ctypes.CField)
print(type(C.x) is ctypes.CField)
print(type(C.x) is ctypes.CField)
print(type(C.x) is ctypes.CField)
print(type(C.x) is ctypes.CField)
print(type(C.x) is ctypes.CField)
print(type(C.x) is ctypes.CField)
print(type(C.x) is ctypes.CField)
print(type(C.x)
