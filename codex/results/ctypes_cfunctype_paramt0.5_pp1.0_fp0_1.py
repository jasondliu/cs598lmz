import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def f(x):
    return 2*x

f_cfunc = FUNTYPE(f)

print f_cfunc(3)

#-------------------------

import ctypes

lib = ctypes.cdll.LoadLibrary('./libfoo.so')

lib.foo(1,2)

#-------------------------

import ctypes

lib = ctypes.cdll.LoadLibrary('./libfoo.so')

lib.foo.argtypes = [ctypes.c_int, ctypes.c_int]
lib.foo.restype = ctypes.c_int

print lib.foo(1,2)

#-------------------------

import ctypes

class Foo(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

lib = ctypes.cdll.LoadLibrary('./libfoo.so')

lib.foo.argtypes = [ctypes.POINTER(F
