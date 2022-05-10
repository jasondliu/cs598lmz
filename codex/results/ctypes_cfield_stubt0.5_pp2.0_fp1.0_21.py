import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class U(T):
    _fields_ = [('y', ctypes.c_int)]

class V(U):
    _fields_ = [('z', ctypes.c_int)]

class W(V):
    _fields_ = [('a', ctypes.c_int)]

class X(W):
    _fields_ = [('b', ctypes.c_int)]

class Y(X):
    _fields_ = [('c', ctypes.c_int)]

class Z(Y):
    _fields_ = [('d', ctypes.c_int)]

class AA(Z):
    _fields_ = [('e', ctypes.c_int)]

class BB(AA):
    _fields_ = [('f', ctypes.c_int)]

class CC(BB):
    _fields_ = [('g', ctypes.c_int)]

class DD(CC):
    _fields
