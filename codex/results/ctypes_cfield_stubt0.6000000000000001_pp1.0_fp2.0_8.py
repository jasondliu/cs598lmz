import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Union(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(Union.x)

class Pointer(ctypes.POINTER(ctypes.c_int)):
    _type_ = ctypes.c_int

ctypes.CPointer = type(Pointer)

class Array(ctypes.c_int * 3):
    _type_ = ctypes.c_int

ctypes.CArray = type(Array)

class Structure(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(Structure)

class Union(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(Union)

class Function(ctypes.CFUNCTYPE(ctypes.c_int)):
    _argtypes_ = (ctypes.c_int,)
    _restype_ = ctypes.c_
