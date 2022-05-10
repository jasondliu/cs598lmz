import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

class S3(ctypes.Structure):
    _fields_ = [('x', S2), ('y', ctypes.c_int)]

class S4(ctypes.Structure):
    _fields_ = [('x', S2), ('y', S2)]

class S5(ctypes.Structure):
    _fields_ = [('x', S4), ('y', S4)]

class S6(ctypes.Structure):
    _fields_ = [('x', S5), ('y', S5)]

class S7(ctypes.Structure):
    _fields_ = [('x', S6), ('y', S6)]

class S8(ctypes.Structure):
    _fields_ = [('x', S7), ('y', S7)]

class S9(ctypes.Structure):
    _fields_ = [('x', S8), ('
