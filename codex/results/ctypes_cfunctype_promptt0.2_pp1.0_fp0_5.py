import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_cmp_func(a, b):
    print 'py_cmp_func', a, b
    return a - b

cmp_func = CMPFUNC(py_cmp_func)

lib.call_cmp_func(cmp_func, 1, 2)

# call a function with a callback, and pass a structure

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

def py_point_func(p):
    print 'py_point_func', p.x, p.y
    return p.x + p.y

POINTFUNC = ctypes.CFUNCTYPE(ctypes.c_
