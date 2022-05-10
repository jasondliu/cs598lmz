import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

assert type(S.x) is ctypes.CField

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

assert type(S.x) is ctypes.CField

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

assert type(S().x) is ctypes.c_int

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

assert type(S().x) is ctypes.c_int

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

assert S().x == 0

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

assert S().x == 0

class S(ctypes.St
