import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int),
                ('w', ctypes.c_int)]

ctypes.CField = type(C.x)

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int),
                ('w', ctypes.c_int)]

ctypes.CField = type(D.x)

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int),
                ('w', ctypes.c_int)]

ctypes.CField = type(E.x)

class F(ctypes.Structure):
    _fields_ = [('x',
