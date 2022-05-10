import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Union):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_double)]

ctypes.CUnion = type(D)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_double),
                ('z', ctypes.c_double),
                ('a', ctypes.c_double),
                ('b', ctypes.c_double),
                ('d', ctypes.c_double),
                ('e', ctypes.c_double),
                ('f', ctypes.c_double),
                ('g', ctypes.c_double),
                ('h', ctypes.c_void_p),
                ('i', ctypes.c_void_p),
                ('j', ctypes.c_int),
                ('k', ctypes.c_int),
                ('l', ctypes.c_int),
                ('m', ctypes.c_int),
                ('n
