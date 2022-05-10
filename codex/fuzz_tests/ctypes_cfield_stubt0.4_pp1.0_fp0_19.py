import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(D):
    _fields_ = [('z', ctypes.c_int)]

print(D.x)
print(E.x)
print(E.y)
print(E.z)

print(D.x.offset)
print(E.x.offset)
print(E.y.offset)
print(E.z.offset)

print(E._fields_)

print(E.x.type)
print(E.y.type)
print(E.z.type)

print(E.x.name)
print(E.y.name)
print(E.z.name)

print(E.x.__dict__)
print(E.y.__dict__)
print(E.z.__dict__)
