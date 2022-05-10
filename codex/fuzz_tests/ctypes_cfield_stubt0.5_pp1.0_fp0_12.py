import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

S.x = C.y

class D(ctypes.Structure):
    _fields_ = [('z', ctypes.c_int)]

S.x = D.z

print(type(S.x))
print(S.x)
print(type(C.y))
print(C.y)
print(type(D.z))
print(D.z)
