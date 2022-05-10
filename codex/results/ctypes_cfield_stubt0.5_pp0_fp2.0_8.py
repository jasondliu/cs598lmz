import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class B(A):
    _fields_ = [('b', ctypes.c_int)]

class C(B):
    _fields_ = [('c', ctypes.c_int)]

ctypes.CField = type(A.a)

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class E(D):
    _fields_ = [('b', ctypes.c_int)]

class F(E):
    _fields_ = [('c', ctypes.c_int)]

ctypes.CField = type(D.a)

class G(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class H(G):
    _fields_ = [('a', ctypes.c_int)]

class I(H):
    _fields_ = [('a', ctypes.c_int
