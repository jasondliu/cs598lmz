import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class Y(X):
    _fields_ = [('y', ctypes.c_int)]

class Z(X):
    _fields_ = [('z', ctypes.c_int)]

class A(Y, Z):
    _fields_ = [('a', ctypes.c_int)]

class B(Y, Z):
    _fields_ = [('b', ctypes.c_int)]

class C(A, B):
    _fields_ = [('c', ctypes.c_int)]

class D(Y, Z):
    _fields_ = [('d', ctypes.c_int)]

class E(D, C):
    _fields_ = [('e', ctypes.c_int)]

class F(E):
    _fields_ = [('f', ctypes.c_int)]

class G(F):
    _fields_ = [('g', ctypes.c_int)]

