import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

ctypes.CStructure = type(C)

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CStructure)]

ctypes.CUnion = type(ctypes.Union)

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.CUnion)]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.CStructure), ('y', ctypes.CUnion)]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.CUnion), ('y', ctypes.CStructure)]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.CUnion), ('y', ctypes.CUnion)]

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.CStructure), ('y', ctypes.C
