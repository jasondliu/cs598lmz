import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(D):
    _fields_ = [('z', ctypes.c_int)]

class F(ctypes.Structure):
    pass

F._fields_ = [('x', ctypes.c_int)]

class G(ctypes.Structure):
    pass

G._fields_ = [('x', ctypes.c_int)]

class H(G):
    _fields_ = [('y', ctypes.c_int)]

class I(H):
    _fields_ = [('z', ctypes.c_int)]

class J(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

J._fields_ = [('x', ctypes.c_int)]

class K(ctypes.Structure):
    _fields_ = [('x',
