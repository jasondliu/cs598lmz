import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyType(ctypes.CField):
    pass

ctypes.CField.__module__ = __name__
ctypes.CField.__name__ = 'CField'
