import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    pass

C._pack_ = 4
C._fields_ = [('a', ctypes.c_int),
              ('b', ctypes.c_int),
              ('c', ctypes.c_int),
              ('d', ctypes.c_int),
              ('e', ctypes.c_int),
              ('f', ctypes.c_int),
              ('g', ctypes.c_int),
              ('h', ctypes.c_int),
              ('i', ctypes.c_int),
              ('j', ctypes.c_int),
              ('k', ctypes.c_int),
              ('l', ctypes.c_int)]

class D(ctypes.Structure):
    pass

D._pack_ = 4
D._fields_ = [('a', ctypes.c_int),
              ('b', ctypes.c_int),
              ('c', ctypes.c_int),
              ('d', ctypes.c_int),
              ('e', ctypes.c
