import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(D.x)
print(E.x)

C.x = D.x
print(C.x)
print(D.x)
print(E.x)

C.x = E.x
print(C.x)
print(D.x)
print(E.x)

print(C.x.offset)
print(D.x.offset)
print(E.x.offset)

print(C.x.size)
print(D.x.size)
print(E.x.size)
