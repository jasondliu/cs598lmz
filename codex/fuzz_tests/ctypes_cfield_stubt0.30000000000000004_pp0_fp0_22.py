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

ctypes.CArray = type(E * 1)

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CPointer = type(ctypes.pointer(F()))

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CString = type(ctypes.c_char_p("abc"))

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CFunction = type
