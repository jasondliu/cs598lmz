import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

ctypes.CStructure = type(S)

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CStructure)]

ctypes.CArray = type(S * 2)

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.CArray)]

ctypes.CPointer = type(ctypes.POINTER(ctypes.c_int))

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.CPointer)]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.CFUNCTYPE(ctypes.c_int))]

ctypes.CUnion = type(ctypes.Union)

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.CUnion)]

class I(ctypes.Structure):
    _
