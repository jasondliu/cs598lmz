import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    pass

C.c_field = ctypes.CField('x', ctypes.c_int, 0, 1)

class D(C):
    pass

print D.c_field
