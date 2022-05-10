import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'
fun()

# example 2
from ctypes import *
FUNTYPE = CFUNCTYPE(c_char_p)
@FUNTYPE
def fun():
    return 'hello'
fun()

# example 3
from ctypes import *
FUNTYPE = CFUNCTYPE(c_char_p)
@FUNTYPE
def fun():
    return 'hello'
fun.restype = c_char_p
fun()

# example 4
from ctypes import *
FUNTYPE = CFUNCTYPE(c_char_p,c_int,c_int)
@FUNTYPE
def fun(a,b):
    return 'hello'
fun.argtypes = [c_int,c_int]
fun(1,2)

# example 5
from ctypes import *
FUNTYPE = CFUNCTYPE(c_char_p,c_int,c_int)
@FUNTYPE
def fun(a,b):
    return 'hello'
fun.argtypes = [c_int,c_int]
fun.restype
