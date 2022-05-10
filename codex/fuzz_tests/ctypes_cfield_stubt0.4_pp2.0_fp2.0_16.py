import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(C.x.__class__)
print(C.x.__class__.__name__)
print(C.x.__class__.__module__)
print(C.x.__class__.__bases__)
print(C.x.__class__.__dict__)
print(C.x.__class__.__doc__)
print(C.x.__class__.__base__)
print(C.x.__class__.__bases__)
print(C.x.__class__.__mro__)
print(C.x.__class__.__subclasses__())
print(C.x.__class__.__init__)
print(C.x.__class__.__new__)
print(C.x.__class__.__call__)
print(C.x.__class__.__getattribute__)
print(C.x.__class
