import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Structure):
    pass

D._fields_ = [('x', ctypes.c_int),
              ('y', ctypes.c_int),
              ('z', ctypes.c_int),
              ('u', ctypes.c_int),
              ('v', ctypes.c_int),
              ('w', ctypes.c_int),
              ('a', ctypes.c_int),
              ('b', ctypes.c_int),
              ('c', ctypes.c_int),
              ('d', ctypes.c_int),
              ('e', ctypes.c_int),
              ('f', ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int
