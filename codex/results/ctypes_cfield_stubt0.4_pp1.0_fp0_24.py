import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

C.y = ctypes.CField(C.x)
C.z = ctypes.CField(C.y)

D.y = ctypes.CField(D.x)
D.z = ctypes.CField(D.y)

E.y = ctypes.CField(E.x)
E.z = ctypes.CField(E.y)

for cls in [C, D, E]:
    print(cls.x)
    print(cls.y)
    print(cls.z)
    print(cls.__dict__)

print(C.x == D.x)
print(C.y == D.y)
print(C
