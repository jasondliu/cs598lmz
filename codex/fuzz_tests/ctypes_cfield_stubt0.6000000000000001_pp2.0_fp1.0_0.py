import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int),
                ('z', ctypes.c_void_p)]

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.Structure),
                ('z', ctypes.c_int)]
F.y._fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class G(ctypes.Structure):
    _fields_ = [('y', ctypes.Structure),
                ('z', ctypes.c_int)]
G.y._fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class H(ct
