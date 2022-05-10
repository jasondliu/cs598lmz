import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(C.x.__class__)
print(C.x.__class__.__bases__)

print(C.x.__class__.__bases__[0].__subclasses__())

print(C.x.__class__.__bases__[0].__subclasses__()[0].__subclasses__())

print(C.x.__class__.__bases__[0].__subclasses__()[0].__subclasses__()[0])

print(C.x.__class__.__bases__[0].__subclasses__()[0].__subclasses__()[0].__subclasses__())

print(C.x.__class__.__bases__[0].__subclasses__()[0].__subclasses__()[0].__subclasses__()[0])

print(C.x.__class__.__bases__[0].
