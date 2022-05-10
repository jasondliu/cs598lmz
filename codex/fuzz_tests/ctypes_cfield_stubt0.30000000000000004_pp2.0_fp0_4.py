import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = C._fields_ + [('y', ctypes.c_int)]

class E(D):
    _fields_ = D._fields_ + [('z', ctypes.c_int)]

class F(E):
    _fields_ = E._fields_ + [('w', ctypes.c_int)]

class G(F):
    _fields_ = F._fields_ + [('v', ctypes.c_int)]

class H(G):
    _fields_ = G._fields_ + [('u', ctypes.c_int)]

class I(H):
    _fields_ = H._fields_ + [('t', ctypes.c_int)]

class J(I):
    _fields_ = I._fields_ + [('s', ctypes.c_int)]

class K(J):
    _fields_ = J._fields_ + [('r', ctypes
