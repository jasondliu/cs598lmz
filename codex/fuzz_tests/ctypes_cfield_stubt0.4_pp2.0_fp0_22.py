import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

ctypes.CStructure = type(C)

class D(ctypes.CStructure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(ctypes.Union)

class E(ctypes.CUnion):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CArray = type(ctypes.c_int * 1)

class F(ctypes.CArray):
    _type_ = ctypes.c_int

ctypes.CPointer = type(ctypes.POINTER(ctypes.c_int))

class G(ctypes.CPointer):
    _type_ = ctypes.c_int

ctypes.CFunction = type(ctypes.CFUNCTYPE(ctypes.c_int))

class H(ctypes.CFunction):
    _argtypes_ = [ctypes.c_int]

