import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('array', ctypes.c_int * 4)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int * 2)]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 2),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int * 2)]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes
