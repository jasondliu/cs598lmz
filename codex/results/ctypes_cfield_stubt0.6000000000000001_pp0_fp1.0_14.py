import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# Test if we can create a new ctypes.Structure class
class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

assert type(S2) is type(S)

# Test if we can create a new ctypes.Union class
class U(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

assert type(U) is type(ctypes.Union)

# Test if we can create a new ctypes.POINTER(ctypes.c_int)
class P(ctypes.POINTER(ctypes.c_int)):
    pass

assert type(P) is type(ctypes.POINTER(ctypes.c_int))

# Test if we can create a new ctypes.c_int instance
class I(ctypes.c_int):
    def __new__(cls, *args, **kw):
        return ctypes.c_int.__new__(cls, *args, **kw)

assert type(I()) is
