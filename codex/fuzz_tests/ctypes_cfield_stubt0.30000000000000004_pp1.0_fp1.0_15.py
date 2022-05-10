import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.c_int):
    pass

class Y(ctypes.c_int):
    pass

class Z(ctypes.c_int):
    pass

class S2(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z)]

class S3(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z),
                ('w', ctypes.c_int)]

class S4(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z),
                ('w', ctypes.c_int),
                ('u', ctypes.c_int)]

class S5(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', Y),
                ('z', Z),
                ('w', ctypes.c_int),
                ('u', ctypes.c_
