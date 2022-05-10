import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(C)

class D(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(D)

class E(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(E)

class F(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(F)

class G(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(G)

class H(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(H)

class I(ctypes.Union):
    _fields_ = [('x
