import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(C.x)

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(D.x)

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CArray = type(E.x)

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CPointer = type(F.x)

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CSimpleType = type(G.x)

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CEnum = type(H.x
