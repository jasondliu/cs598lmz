import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

S.x = C.x

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

C.x = D.x

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

D.x = E.x

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

E.x = F.x

for i in range(100):
    F.x = ctypes.c_int

for i in range(100):
    E.x = ctypes.c_int

for i in range(100):
    D.x = ctypes.c_int

for i in range(100):
    C.x = ctypes.c_int

for i in range(100):
    S.x = ctypes.c_int


