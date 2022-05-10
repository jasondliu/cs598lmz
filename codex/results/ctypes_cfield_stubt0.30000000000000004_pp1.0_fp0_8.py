import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class D(C):
    _fields_ = [('z', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

class F(C):
    _fields_ = [('z', ctypes.c_int),
                ('w', ctypes.c_int)]

class G(C):
    _fields_ = [('w', ctypes.c_int),
                ('z', ctypes.c_int)]

class H(C):
    _fields_ = [('w', ctypes.c_int),
                ('z', ctypes.c_int),
                ('a', ctypes.c_int)]

class I(C):
    _fields_ = [('a', ctypes
