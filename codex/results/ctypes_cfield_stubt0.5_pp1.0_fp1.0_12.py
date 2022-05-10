import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', S), ('y', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('x', C), ('y', ctypes.c_int)]

print(D.x)
print(D.x.x)
print(D.x.x.x)

print(D.x.x.x == C.x.x)
print(D.x.x.x == S.x)

# XXX: This is not a proper test:
#print(D.x.x.x == C.x)
#print(D.x.x.x == C)
