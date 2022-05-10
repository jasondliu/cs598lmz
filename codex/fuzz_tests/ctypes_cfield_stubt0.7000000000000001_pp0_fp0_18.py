import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class U(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(U.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(C))]

ctypes.CPointer = type(D.p)

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 2)]

ctypes.CArray = type(E.x)

# XXX: 'restype' and 'argtypes' are defined as C functions, but
# there's no way to create a C function in Python

# XXX: ctypes.POINTER(ctypes.CFUNCTYPE(...)) is a type, but it is
# not easy to create an instance of it in Python

class X(ctypes.Structure):
    _fields_ = [('x', c
