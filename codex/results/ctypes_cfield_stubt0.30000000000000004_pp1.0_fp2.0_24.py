import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(C)

class D(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(D)

class E(ctypes.Array):
    _type_ = ctypes.c_int
    _length_ = 5

ctypes.CArray = type(E)

class F(ctypes.PyCSimpleType):
    _type_ = "i"

ctypes.CPyCSimpleType = type(F)

class G(ctypes.PyCArgObject):
    _type_ = "i"

ctypes.CPyCArgObject = type(G)

class H(ctypes.PyCArrayType):
    _type_ = "i"
    _length_ = 5

ctypes.CPyCArrayType = type(H)

class I(ctypes.PyCStructType):

