import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Union):
    _fields_ = [('y', ctypes.c_int)]

ctypes.CUnion = type(D)

class E(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

ctypes.CStruct = type(E)

ctypes.CArrayType = type(ctypes.c_int * 2)

ctypes.CPointerType = type(ctypes.c_int_p)

class F(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

ctypes.CPointerType = type(ctypes.pointer(F()))

ctypes.CFunctionType = type(ctypes.CFUNCTYPE(ctypes.c_int))

ctypes.CString = type(ctypes.c_char_p("foo"))

ctypes.CEnum = type(ctypes.c_int)

ctypes.CInt = type(ctypes.c_int())

ctypes
