import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_double),
                ('c', ctypes.c_char),
                ('d', ctypes.c_char_p),
                ('e', S),
                ('f', ctypes.c_int * 5)]

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_double)]

class F(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_double),
                ('c', ctypes.c_double)]

class G(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.
