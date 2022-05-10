import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class D(C):
    _fields_ = [('b', ctypes.c_int)]

class E(C):
    _fields_ = [('c', ctypes.c_int)]

class F(D, E):
    _fields_ = [('d', ctypes.c_int)]

class G(D, E):
    _fields_ = [('e', ctypes.c_int)]

class H(F, G):
    _fields_ = [('f', ctypes.c_int)]

# XXX This should be a test, but it crashes the interpreter
#print H.a, H.b, H.c, H.d, H.e, H.f

class I(H):
    _fields_ = [('g', ctypes.c_int)]

# XXX This should be a test, but it crashes the interpreter
#print I.a, I.b, I.c, I.d, I.
