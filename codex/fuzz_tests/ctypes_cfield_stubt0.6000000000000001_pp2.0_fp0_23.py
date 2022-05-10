import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Array):
    _type_ = ctypes.c_int
    _length_ = 5

ctypes.CArray = type(A)

class U(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(U)

class P(ctypes.POINTER):
    _type_ = ctypes.c_int

ctypes.CPointer = type(P)

class F(ctypes.CFUNCTYPE):
    _argtypes_ = [ctypes.c_int]
    _restype_ = ctypes.c_int

ctypes.CFunctionType = type(F)

class M(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(M)

class C(ctypes.c_int):
    pass

ctypes.CBase = type(C)

ctypes.CArgObject = (ctypes.c_int
