import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

S._fields_ = [('x', ctypes.c_int),
              ('y', ctypes.c_int)]

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

S._fields_ = [('x', ctypes.c_int),
              ('y', ctypes.c_int),
              ('z', ctypes.c_int)]

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

S._fields_ = [('x', ctypes.c_int),
              ('y', ctypes.c_int),
              ('z', ctypes.c_int),
              ('w', ctypes.c_int)]

class S(ctypes.St
