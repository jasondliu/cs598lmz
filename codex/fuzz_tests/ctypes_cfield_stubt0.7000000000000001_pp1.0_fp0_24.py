import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A:
    pass

A.c_field = ctypes.CField('c_field', A, ctypes.c_int, 0)
