import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

ctypes.CFuncPtr = type(ctypes.CFuncPtr(lambda: None))

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.CFuncPtr)]

ctypes.CArray = type(ctypes.c_int * 1)

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.CArray)]

ctypes.CPointer = type(ctypes.pointer(ctypes.c_int()))

class P(ctypes.Structure):
    _fields_ = [('x', ctypes.CPointer)]

ctypes.CUnion = type(ctypes.Union)

class U(ctypes.Structure):
    _fields_ = [('x', ctypes.CUnion)]

ctypes.CStruct = type(ctypes.Structure)

class T(ctypes.Structure):
    _fields_ = [('x', c
