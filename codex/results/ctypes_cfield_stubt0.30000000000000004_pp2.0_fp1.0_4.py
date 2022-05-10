import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.CField)]

print(C.y)
print(C.y.__class__)
print(C.y.__class__.__bases__)
print(C.y.__class__.__bases__[0].__bases__)
print(C.y.__class__.__bases__[0].__bases__[0].__bases__)
print(C.y.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__)
print(C.y.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__[0].__bases__)
print(C.y.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__[0].__bases__[0].__bases__)
print(C.y.__
