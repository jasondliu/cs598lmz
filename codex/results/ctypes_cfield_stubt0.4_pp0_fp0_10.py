import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class G(E, F):
    pass

class H(E, F):
    _fields_ = [('c', ctypes.c_int)]

class I(E, F):
    _fields_ = [('c', ctypes.c_int),
                ('d', ctypes.c_int)]

class J(E, F):
    _fields_ = [('c', ctypes.c_int),
                ('d', ctypes.c_int),
                ('e', ctypes.c_
