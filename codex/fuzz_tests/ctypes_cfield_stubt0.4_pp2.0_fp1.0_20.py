import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('f', ctypes.CField)]

print(C.f)
print(C.f.__class__)
print(C.f.__doc__)
print(C.f.__name__)
print(C.f.__module__)
