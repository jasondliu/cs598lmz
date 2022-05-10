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

class F(ctypes.Array):
    _type_ = ctypes.c_int
    _length_ = 10

ctypes.CArray = type(F)

class G(ctypes.POINTER(ctypes.c_int)):
    pass

ctypes.CPointer = type(G)

class H(ctypes.c_int):
    pass

ctypes.CBase = type(H)

class I(ctypes.c_int):
    pass

ctypes.CSubclass = type(I)

class J(
