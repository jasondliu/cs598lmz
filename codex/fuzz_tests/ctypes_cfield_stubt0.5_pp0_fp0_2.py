import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [(('y', ctypes.c_int), ('x', ctypes.c_int))]

class F(ctypes.Structure):
    _fields_ = [(('y', ctypes.c_int), ('x', ctypes.c_int)),
                (('a', ctypes.c_int), ('b', ctypes.c_int))]

class G(ctypes.Structure):
    _fields_ = [(('y', ctypes.c_int), ('x', ctypes.c_int)),
                (('a', ctypes.c_int), ('b', ctypes.c_int)),
                (('c', ctypes.c_int), ('d', ctypes.c_int))]

class H(ctypes.Structure):
    pass
