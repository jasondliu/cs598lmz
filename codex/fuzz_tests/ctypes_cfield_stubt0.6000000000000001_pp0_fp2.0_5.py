import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

class D(C):
    _fields_ = [('c', ctypes.c_int)]

class E(D):
    pass

class F(ctypes.Structure):
    pass

class G(F):
    _fields_ = [('a', ctypes.c_int)]

class H(G):
    pass

class I(ctypes.Structure):
    pass

class J(I):
    pass

class K(J):
    _fields_ = [('a', ctypes.c_int)]

class Base(ctypes.Structure):
    pass

class Derived(Base):
    pass

class U(ctypes.Union):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

class V(ctypes.Structure):
    _fields_ = [('a', ctypes.c
