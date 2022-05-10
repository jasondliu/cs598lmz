import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(C)

class D(C):
    _fields_ = [('y', ctypes.c_float)]

ctypes.CUnion = type(ctypes.Union)

class E(ctypes.Union):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_float)]

ctypes.CArray = type(ctypes.c_int * 3)

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

ctypes.CPointer = type(ctypes.pointer(F()))

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

ctypes.CFunctionType = type(ctypes.CFUNCTYPE(ctypes.c
