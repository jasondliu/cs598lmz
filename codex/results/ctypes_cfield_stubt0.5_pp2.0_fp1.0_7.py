import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

c = C(1, 2)
print(c.a)
print(c.b)
print(C.a)
print(C.b)
print(C.a.offset)
print(C.b.offset)
print(C.a.size)
print(C.b.size)
print(C.a.__dict__)
print(C.b.__dict__)
print(C.a.__dict__ == C.b.__dict__)
print(C.a.__dict__ is C.b.__dict__)
print(C.a.__dict__ is C.a.__dict__)
print(C.a.__dict__ is C.b.__dict__)
print(type(C.a))
print(type(C.b))
print(type(C.a) == type(C.b))
print(type(C.a) is type
