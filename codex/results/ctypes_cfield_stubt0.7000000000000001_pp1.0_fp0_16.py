import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
CInt = ctypes.c_int

class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class B(A):
    _fields_ = [('c', ctypes.c_int)]

class C(B):
    _fields_ = [('d', ctypes.c_int)]

class D(C):
    _fields_ = [('e', ctypes.c_int)]

class E(D):
    _fields_ = [('f', ctypes.c_int)]

class F(E):
    _fields_ = [('g', ctypes.c_int)]

class G(F):
    _fields_ = [('h', ctypes.c_int)]

class H(G):
    _fields_ = [('i', ctypes.c_int)]

class I(H):
    _fields_ = [('j', ctypes.c_int)]

class J(I):
    _fields_ =
