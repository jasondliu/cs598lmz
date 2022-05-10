import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

assert S.x is ctypes.c_int

class T(ctypes.Structure):
    x = ctypes.c_byte
    _fields_ = [("x", ctypes.c_int)]

assert T.x is ctypes.c_int

## the following raises a TypeError like the ctypes manual documents in the
## Defining Structures section, but perhaps it would be nice if a more
## specific exception could be raised?
class U(ctypes.Structure):
    x = ctypes.c_byte
    ctypes._setattribute_check(x._flags_, 1)
    _fields_ = [("x", ctypes.c_int)]

assert U.x is ctypes.c_int
