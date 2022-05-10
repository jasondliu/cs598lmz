import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    pass

def instance(cls, *args):
    if isinstance(cls, type):
        return cls(*args)
    else:
        return cl
