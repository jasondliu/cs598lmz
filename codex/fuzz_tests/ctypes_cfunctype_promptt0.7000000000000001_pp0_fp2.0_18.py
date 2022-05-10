import ctypes
# Test ctypes.CFUNCTYPE() and ctypes.byref()

from ctypes import *

def test(f):
    print("Function type:", f)
    print("Calling the function with argument 42")
    print("Returned", f(42))

# First with a builtin function:
test(abs)
print("")

# Now with a simple callback function:
CALLBACK = CFUNCTYPE(c_int, c_int)

def py_callback_func(arg):
    print("py_callback_func() was called with argument", arg)
    return -arg

cb = CALLBACK(py_callback_func)
print("callback type:", type(cb))

test(cb)
print("")

# Now with a callback function that uses a global variable.
# This function must be defined in the module namespace, otherwise
# the closure will not work.
some_global = 5

def py_callback_func_global():
    print("py_callback_func_global() was called")
    return some_global

cb = CALLBACK(py_callback_func_
