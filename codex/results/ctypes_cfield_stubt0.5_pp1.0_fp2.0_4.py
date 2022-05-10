import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('f', ctypes.c_int)]

class D(C):
    _fields_ = [('f', ctypes.c_int)]

class E(C):
    _fields_ = [('g', ctypes.c_int)]

class F(C):
    _fields_ = [('f', ctypes.c_int),
                ('g', ctypes.c_int)]

class G(C):
    _fields_ = [('g', ctypes.c_int),
                ('f', ctypes.c_int)]

class H(C):
    _fields_ = [('g', ctypes.c_int),
                ('f', ctypes.c_int),
                ('h', ctypes.c_int)]

class I(C):
    _fields_ = [('g', ctypes.c_int),
                ('f', ctypes.c_int),
                ('h', ctypes.c_int),
                ('i', ctypes.c_int
