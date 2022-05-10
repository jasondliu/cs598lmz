import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class A(ctypes.Union):
    _fields_ = [('x', ctypes.c_int),
                ('y', Y),
                ('z', Z)]

class B(ctypes.Structure):
    _fields_ = [('a', A),
                ('x', ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [('b', B),
                ('x', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('c', C),
                ('x', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('d', D),
               
