import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

# Create some functions

def func(x):
    return x*5

def func_var(x, y):
    return x*y

def func_void():
    print "Hello, World!"

def func_float(x):
    return x*2.0

def func_string(x):
    return "Hello, " + x + "!"

def func_unicode(x):
    return "Hello, " + x + "!"

def func_int(x):
    return x*2

def func_long(x):
    return x*2

def func_longlong(x):
    return x*2

def func_c_int(x):
    return x*2

def func_c_long(x):
    return x*2

def func_c_longlong(x):
    return x*2

def func_c_uint(x):
    return x*2

def func_c_ulong(x):
    return x*2

def func
