import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

class B(A):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]

class C(B):
    _fields_ = [('d', ctypes.c_int),
                ('e', ctypes.c_int),
                ('f', ctypes.c_int)]

class D(A):
    _fields_ = [('g', ctypes.c_int)]

class E(B):
    _fields_ = [('h', ctypes.c_int)]

class F(C):
    _fields_ = [('i', ctypes.c_int)]

class G(D, F):
    _fields_ = [('j', ctypes.c_int)]

class H(E, F):
