import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Union):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

ctypes.CUnion = type(D.x)

class U(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

ctypes.CStruct = type(U.x)

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

ctypes.CArray = type(F.x)

class G(ctypes.Structure):
    pass

class H(G):
    pass

ctypes.CBase = type(H.x)

class I(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z
