import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass

C._fields_ = [('x', ctypes.c_char)]

ctypes.CStructOrUnion = type(C)

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CArray = type(D.x)

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.c_int))]

ctypes.CPointer = type(E.x)

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

ctypes.CUnion = type(F)

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CEnum = type(G.x)

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.
