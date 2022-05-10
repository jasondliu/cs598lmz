import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

ctypes.CStructure = type(C)

class X(ctypes.Union):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

ctypes.CUnion = type(X)

class MyInt(ctypes.c_int):
    pass

ctypes.CIntType = type(MyInt)

class MyIntPtr(ctypes.POINTER(MyInt)):
    pass

ctypes.CPointerType = type(MyIntPtr)

class MyIntArray(ctypes.c_int * 1):
    pass

ctypes.CArrayType = type(MyIntArray)

ctypes.CFunctionType = type(ctypes.CFUNCTYPE(ctypes.c_int))

class MyFunction(ctypes.CFUNCTYPE(ctypes.c_int)):

