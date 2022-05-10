import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(S):
    pass

ctypes.CField = type(S.x)

assert D(x=0)


class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(E.x)

assert E(x=0)
