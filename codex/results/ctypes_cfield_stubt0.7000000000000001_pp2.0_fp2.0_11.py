import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_float),
                ('z', ctypes.c_char_p)]

S._fields_ = [('x', ctypes.c_int),
              ('y', ctypes.c_float),
              ('z', ctypes.c_char_p)]

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_float),
                ('z', ctypes.c_char_p)]

S._fields_ = [('x', ctypes.c_int),
              ('y', ctypes.c_float),
              ('z', ctypes.c_char_p),
              ('zz', ctypes.c_int)]

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_float),
                ('z', ctypes
