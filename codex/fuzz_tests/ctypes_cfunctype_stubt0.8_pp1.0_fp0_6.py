import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
fun()

import ctypes
def foo(x):
    return x*2
cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(foo)
cfunc(3)


import ctypes
def foo(x):
    return x*2
cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(foo)
cfunc(3)

import ctypes
def foo(x):
    return x*2
cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(foo)
cfunc.restype = ctypes.c_float
cfunc(3)

import ctypes
def foo(x):
    return x*2
cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))(foo)
cfunc.restype = ctypes.c_float
cfunc(ctypes.pointer(ctypes.c_
