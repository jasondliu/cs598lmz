import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 2

assert fun() == 2
print(fun())

def fun():
    return 'hello'

fun = FUNTYPE(fun)
assert fun() == 'hello'
print(fun())

import pdb
pdb.set_trace()

import ctypes

# function prototype of C function
# double fun(double a, double b)
prototype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

# C function
def fun(a, b):
    return a + b

# convert to C function pointer
fun = prototype(fun)
print(fun(1, 2))

import ctypes

# function prototype of C function
# double fun(double a, double b)
prototype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

# C function
def fun(a, b):
    return a + b

# convert to C function pointer
fun = prototype(fun)

#
