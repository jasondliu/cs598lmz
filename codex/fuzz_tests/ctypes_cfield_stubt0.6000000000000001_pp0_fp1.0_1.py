import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CArray = type(S.x * 2)

class X(ctypes.Structure):
    _fields_ = [('f1', ctypes.c_int), ('f2', ctypes.c_int)]

class Y(X):
    pass

class Z(ctypes.Structure):
    _fields_ = [('x', X),
                ('y', ctypes.c_int)]

class Q(ctypes.Structure):
    _fields_ = [('x', ctypes.POINTER(X)),
                ('y', ctypes.c_int)]

class R(ctypes.Structure):
    _fields_ = [('x', ctypes.c_void_p),
                ('y', ctypes.c_int)]

class S(ctypes.Structure):
    pass

class T(ctypes.Structure):
    _fields_ = [('x', S),
                ('y', ctypes.c_int)]

class U(ctypes.Structure):
    _fields_ = [('x', ctypes
