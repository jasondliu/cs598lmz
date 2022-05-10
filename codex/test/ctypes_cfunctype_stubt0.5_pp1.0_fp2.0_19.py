import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()

# ctypes.py_object is not a valid return type for CFUNCTYPE

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
@FUNTYPE
def fun():
    return 42

fun()

# ctypes.c_int is not a valid return type for CFUNCTYPE

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)
@FUNTYPE
def fun(x):
    return 42

fun(1)

# ctypes.py_object is not a valid argument type for CFUNCTYPE

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
@FUNTYPE
def fun(x):
    return 42

fun(1)

# ctypes.c_int is not a valid argument type for CFUNCTYPE

import ctypes
