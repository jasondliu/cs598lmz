import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __getattr__(self, name):
        return 42

class D(S):
    _fields_ = [('y', ctypes.c_int),
                ('z', ctypes.c_float)]

class E(S):
    _fields_ = [('y', ctypes.c_int),
                ('z', ctypes.c_float),
                ('o', ctypes.c_int)]

class F(S):
    _fields_ = [('y', ctypes.c_int),
                ('z', ctypes.c_float),
                ('o', ctypes.c_int),
                ('p', ctypes.c_int)]

class G(S):
    _fields_ = [('y', ctypes.c_int),
                ('z', ctypes.c_float),
                ('o', ctypes.c_int),
                ('p', ctypes.c_int),
                ('q', ctypes.c_int)]

class H(S):
    _fields_ = [('y', c
