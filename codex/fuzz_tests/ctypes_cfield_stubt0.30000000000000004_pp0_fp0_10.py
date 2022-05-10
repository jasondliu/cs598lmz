import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(C.x.offset)
print(C.x.size)
print(C.x.name)
print(C.x.type)
print(C.x.__doc__)

print(C.x.__class__)
print(C.x.__class__.__bases__)
print(C.x.__class__.__mro__)
print(C.x.__class__.__dict__)
print(C.x.__class__.__name__)
print(C.x.__class__.__module__)
print(C.x.__class__.__doc__)

print(C.x.__class__.__dict__['offset'])
print(C.x.__class__.__dict__['size'])
print(C.x.__class__.__dict__['name'])
print(C.x.__class__.__dict__
