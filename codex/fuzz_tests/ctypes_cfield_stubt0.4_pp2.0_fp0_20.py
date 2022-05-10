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
print(type(C.x) is ctypes.Field)
print(isinstance(C.x, ctypes.CField))
print(isinstance(C.x, ctypes.Field))
print(isinstance(C.x, ctypes.Field))
print(C.x.__class__ is ctypes.CField)
print(C.x.__class__ is ctypes.Field)
print(C.x.__class__ is ctypes.Field)

print(C.x.offset)
print(C.x.size)
print(C.x.index)
print(C.x.name)
print(C.x.ctype)
print(C.x.type)
print(
