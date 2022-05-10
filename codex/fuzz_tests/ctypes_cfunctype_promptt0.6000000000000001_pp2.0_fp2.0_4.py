import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

def func(x):
    print('func', x)
    return x + 1

CALLBACK = CFUNCTYPE(c_int, c_int)

class X(Structure):
    _fields_ = [('a', c_int),
                ('b', c_double),
                ('fp', CALLBACK)]

x = X(1, 2.5, CALLBACK(func))

lib.pass_struct(x)

if x.a != 1 or x.b != 2.5 or x.fp(2) != 3:
    raise Exception("unexpected values")
