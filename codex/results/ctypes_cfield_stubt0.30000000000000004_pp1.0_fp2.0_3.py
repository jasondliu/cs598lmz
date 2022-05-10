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

ctypes.CArray = type(E)

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CPointer = type(F)

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CString = type(G)

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CFixedArray = type(H)

class I(ctypes.Structure):
   
