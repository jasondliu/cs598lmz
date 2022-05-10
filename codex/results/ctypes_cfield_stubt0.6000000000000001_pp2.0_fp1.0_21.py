import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', D)]

class F(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', E)]

class G(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', F)]

class H(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', G)]

class I(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', H)]

class J(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', I)]

class K(ctypes.Structure):
    _fields_ = [('
