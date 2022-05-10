import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.c_int):
    pass

class E(ctypes.c_int):
    _fields_ = [('a', ctypes.c_int)]

class F(ctypes.c_int):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

class G(ctypes.c_int):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int), ('c', ctypes.c_int)]

class H(ctypes.c_int):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int), ('c', ctypes.c_int),
                ('d', ctypes.c_int)]

class I(ctypes.c_int):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int), ('c', ctypes.c_int),
                ('d', ctypes.c_int), ('
