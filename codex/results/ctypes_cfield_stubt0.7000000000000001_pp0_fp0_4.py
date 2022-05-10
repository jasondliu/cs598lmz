import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = C._fields_ + [('y', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class F(E):
    _fields_ = E._fields_ + [('c', ctypes.c_int)]

class G(E):
    _fields_ = E._fields_ + [('d', ctypes.c_int)]

class H(F, G):
    _fields_ = F._fields_ + G._fields_

class I(G, F):
    _fields_ = G._fields_ + F._fields_

class J(I):
    _fields_ = I._fields_ + [('e', ctypes.c_int)]

class K(I):
    _fields_ = I._fields_ + [('f', c
