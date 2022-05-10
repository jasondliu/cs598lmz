import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    _anonymous_ = [('y', ctypes.c_int)]

ctypes.CField = type(T.x)

class U(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    _anonymous_ = ['x']

ctypes.CField = type(U.x)
