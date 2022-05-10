import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.c_int):
    _fields_ = [('x', ctypes.c_int)]

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class C2(ctypes.c_int):
    _fields_ = [('x', ctypes.CField)]

# tests that CField works in Structure and Structure subclasses
print(type(S._fields_[0][1]))
print(type(S2._fields_[0][1]))
####
s2 = S2()
print(type(s2.x))
c2 = C2()
print(type(c2.x))
