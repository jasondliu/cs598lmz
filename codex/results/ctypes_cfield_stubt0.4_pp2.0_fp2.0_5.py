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

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructSequence = type(E())

# XXX: ctypes.POINTER(ctypes.c_int) is not a class, but a ctypes.PyCSimpleType
ctypes.CPointerType = type(ctypes.POINTER(ctypes.c_int))

ctypes.CArrayType = type(ctypes.c_int * 1)

ctypes.CFuncPtrType = type(ctypes.WINFUNCTYPE(ctypes.c_int))

ctypes.CStringType = type(ctypes.c_char_p(""))

ctypes.CBytes
