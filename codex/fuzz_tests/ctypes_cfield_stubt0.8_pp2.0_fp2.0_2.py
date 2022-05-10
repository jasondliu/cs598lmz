import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass
C._fields_ = [('s', S)]

C.s = C.s.in_dll(ctypes.pythonapi, 's')

print(C.s.x)
print(C().s.x)
