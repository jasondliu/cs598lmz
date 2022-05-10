import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

ctypes.CFuncPtr = type(ctypes.CFuncPtr)

class CF(ctypes.Structure):
    _fields_ = [('x', ctypes.CFuncPtr)]

class P(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(ctypes.c_int))]

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 4)]

class U(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(U)

class CU(ctypes.Structure):
    _fields_ = [('x', ctypes.CUnion)]

class O(ctypes.Structure):
    _fields_ = [('x', object)]

class CString(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char
