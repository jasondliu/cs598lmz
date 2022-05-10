import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x)
print(C.x.__class__)

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField), ('y', ctypes.c_int)]

print(D.x)
print(D.x.__class__)
print(D.y)
print(D.y.__class__)

print(D().x)
print(D().x.__class__)
print(D().y)
print(D().y.__class__)

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.CField)]

print(E.x)
print(E.x.__class__)
print(E.y)
print(E.y.__class__)

print(E().x)
print(E().x.__class__)
print(E().
