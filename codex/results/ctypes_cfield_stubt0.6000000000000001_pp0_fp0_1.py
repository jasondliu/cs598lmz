import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField2 = type(S2.x)

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField3 = type(S3.x)

class S4(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 4)]

ctypes.CField4 = type(S4.x)

class S5(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 4)]

ctypes.CField5 = type(S5.x)
