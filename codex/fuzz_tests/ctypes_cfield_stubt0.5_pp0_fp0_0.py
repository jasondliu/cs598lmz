import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int),
                ('z', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.CField),
                ('b', ctypes.CField)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.CField)]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.CField)]

class G(ctypes.Structure):
    _fields_ = [('x', ctypes.CField),
                ('y', ctypes.CField),
                ('z', ctypes.CField)]

class H(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int
