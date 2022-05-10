import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class T(S):
    pass

ctypes.CFieldType = type(T.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_float)]

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_float),
                ('next', ctypes.POINTER(S3))]

S3Ptr = ctypes.POINTER(S3)
S3PtrPtr = ctypes.POINTER(S3Ptr)

class S4(ctypes.Structure):
    _fields_ = [('next', ctypes.POINTER(S4))]

S4Ptr = ctypes.POINTER(S4)

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]


class Y(X):
    _fields_ = [('
