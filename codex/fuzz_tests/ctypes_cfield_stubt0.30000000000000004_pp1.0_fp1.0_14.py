import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [('a', A),
                ('z', ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [('b', B),
                ('w', ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('c', C),
                ('v', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('d', D),
                ('u', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('e', E),
                ('t', ctypes.c_int)]

class G(ctypes.Structure):
    _fields_ = [('f', F),
                ('s', ctypes.c_int)]

class H(
