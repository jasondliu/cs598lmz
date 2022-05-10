import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(C)

class X(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(X)

class Y(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CArray = type(Y)

class Z(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CPointer = type(Z)

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CFunction = type(A)

class B(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CString = type(B)

class C(ctypes.Structure):
    _
