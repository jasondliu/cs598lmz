import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class D(C):
    _fields_ = [('z', ctypes.c_int)]

class E(D):
    _fields_ = [('w', ctypes.c_int)]

class F(D):
    _fields_ = [('w', ctypes.c_int)]
    _anonymous_ = ('x', 'y')

class G(E):
    _fields_ = [('w', ctypes.c_int)]

class H(E):
    _fields_ = [('w', ctypes.c_int)]
    _anonymous_ = ('x', 'y')

class I(E):
    _fields_ = [('w', ctypes.c_int)]
    _anonymous_ = ('z',)

class J(E):
    _fields_ = [('w', ctypes.c_int)]
    _anonymous_ = ('z',
