import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

class D(C):
    pass

class E(C):
    _fields_ = [('a', ctypes.c_int)]

class F(C):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class G(C):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int),
                ('t', ctypes.c_int)]

class H(C):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int),
                ('t', ctypes.c_int),
                ('u', ctypes.c_int)]

