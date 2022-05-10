import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 1

ctypes.CInstance = type(C())

try:
    class C(object):
        __slots__ = ['x']
        def __init__(self):
            self.x = 1
    ctypes.CPointerInstance = type(C())
except TypeError:
    pass

ctypes.CArray = ctypes.c_int * 1

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CArrayInstance = X * 1

try:
    class C(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    ctypes.CPointerType = type(C.x)
except AttributeError:
    pass

try:
    class C(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    ctypes.CPointerInstance = type(C().x)
