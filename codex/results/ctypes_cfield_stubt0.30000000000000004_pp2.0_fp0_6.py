import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(C)

class D(C):
    _fields_ = [('y', ctypes.c_int)]

ctypes.CUnion = type(ctypes.Union)

class E(ctypes.Union):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

ctypes.CArray = type(ctypes.c_int * 1)

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 1)]

ctypes.CPointer = type(ctypes.POINTER(ctypes.c_int))

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.c_int))]

ctypes.CFunctionType = type(ctypes.CFUNCTYPE(ctypes.c_int))

class
