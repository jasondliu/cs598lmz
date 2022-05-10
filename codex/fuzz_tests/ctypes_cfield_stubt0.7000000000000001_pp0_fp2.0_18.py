import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass

C._fields_ = [('f', ctypes.CField)]

print(C.f)

print(ctypes.CField)

print(isinstance(C.f, ctypes.CField))
