import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(D)

class E(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CUnion = type(E)

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CArray = type(F)

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CPointer = type(G)

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CFunction = type(H)

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CString = type(I)

class J(ctypes.Structure):
    _
