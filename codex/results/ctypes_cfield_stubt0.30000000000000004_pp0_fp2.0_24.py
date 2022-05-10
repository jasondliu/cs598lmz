import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

class Y(X):
    _fields_ = [('c', ctypes.c_int)]

class Z(Y):
    _fields_ = [('d', ctypes.c_int)]

class W(Z):
    _fields_ = [('e', ctypes.c_int)]

class V(W):
    _fields_ = [('f', ctypes.c_int)]

class U(V):
    _fields_ = [('g', ctypes.c_int)]

class T(U):
    _fields_ = [('h', ctypes.c_int)]

class S(T):
    _fields_ = [('i', ctypes.c_int)]

class R(S):
    _fields_ = [('j', ctypes.c_int)]

class Q(R):
    _fields_ = [('k', ctypes.c_int)]

