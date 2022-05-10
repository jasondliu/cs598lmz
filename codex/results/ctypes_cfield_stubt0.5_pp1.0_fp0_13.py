import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(ctypes.c_int))]

ctypes.CFieldPtr = type(C.p)

class D(ctypes.Structure):
    _fields_ = [('s', S)]

ctypes.CFieldStruct = type(D.s)

class E(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int * 3)]

ctypes.CFieldArray = type(E.a)

class F(ctypes.Structure):
    _fields_ = [('c', ctypes.c_char)]

ctypes.CFieldChar = type(F.c)

class G(ctypes.Union):
    _fields_ = [('c', ctypes.c_char)]

ctypes.CFieldUnion = type(G.c)


class H(ctypes.Structure):
    _fields_ = [('c', ctypes.c_char)]

ctypes.CFieldChar =
