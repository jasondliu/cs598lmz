import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

S2 = ctypes.Structure
S2._fields_ = [('x', ctypes.c_int)]

class C2(ctypes.Structure):
    pass
C2._fields_ = [('x', ctypes.c_int)]

class D2(C2):
    pass
D2._fields_ = [('y', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class F(E):
    _fields_ = [('y', ctypes.c_int)]

class G(F):
    pass
G._fields_ = [('z', ctypes.c_int)]

class H(G):
    pass

class I(H):
    _fields_ = [('w', ctypes.c_int
