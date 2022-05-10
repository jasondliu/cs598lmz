import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

# A function that takes a function as argument
def call_func(fn, *args):
    return fn(*args)

# A function that takes a function as argument, and calls it
# with a pointer as argument
def call_func_ptr(fn, ptr, *args):
    return fn(ptr, *args)

# A function that takes a function as argument, and calls it
# with a pointer as argument
def call_func_ptr_ptr(fn, ptr, *args):
    return fn(ptr, *args)

# A function that takes a function as argument, and calls it
# with a pointer as argument
def call_func_ptr_ptr_ptr(fn, ptr, *args):
    return fn(ptr, ptr, *args)

# A function that takes a function as argument, and calls it
# with a pointer as argument
def call_func_ptr_ptr_ptr_ptr(fn, ptr, *args):
    return fn(ptr, ptr, ptr, *args)

# A function that takes a function as argument, and
