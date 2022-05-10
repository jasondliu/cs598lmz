import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(ctypes.CField)

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

print(A.x)
print(A.x.__class__)

class B(ctypes.Structure):
    _fields_ = [(('x', ctypes.c_int),)]

print(B.x)
print(B.x.__class__)

class C(ctypes.Structure):
    _fields_ = [((('x', ctypes.c_int),))]

print(C.x)
print(C.x.__class__)

class D(ctypes.Structure):
    _fields_ = [(((('x', ctypes.c_int),),))]

print(D.x)
print(D.x.__class__)
