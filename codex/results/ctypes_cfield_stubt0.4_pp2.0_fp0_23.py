import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(C)

class C(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(C)

class C(ctypes.Array):
    _type_ = ctypes.c_int
    _length_ = 1

ctypes.CArray = type(C)

class C(ctypes.PyCSimpleType):
    _type_ = "i"
    _length_ = 1

ctypes.CPyCSimpleType = type(C)

class C(ctypes.PyCArgObject):
    _type_ = "i"
    _length_ = 1

ctypes.CPyCArgObject = type(C)

class C(ctypes.PyCArrayType):
    _type_ = "i"
    _length_ = 1

ctypes.CPyCArrayType = type(C)
