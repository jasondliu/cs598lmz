import ctypes
# Test ctypes.CFUNCTYPE

# We can call a C function with a callback that is a builtin Python
# function, but we must specify the argument and return types.

def py_func(i):
    print i
    return i*2

CFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
CALLBACK = CFUNC(py_func)

import _ctypes_test
_ctypes_test.set_callback(CALLBACK)
_ctypes_test.call_callback(42)

# Now we try the same with a class method.  The class method must not
# be an instance method, so we define it outside the class.

def py_method(i):
    print i
    return i*3

class C:
    pass
C.method = py_method

CALLBACK = CFUNC(C.method)
_ctypes_test.set_callback(CALLBACK)
_ctypes_test.call_callback(42)

# Now we try the same with an instance method.  This
