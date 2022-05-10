import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype a function with a function pointer argument
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define a function with a function pointer argument
def py_callback(n):
    print 'py_callback(%d)' % n
    return n * 2

# convert the Python function into a C function pointer
cb = prototype(py_callback)

# call a C function with the C function pointer
res = lib.call_function_pointer(cb, 5)
print 'got:', res

# call a C function with a C function pointer
res = lib.call_function_pointer(cb, 6)
print 'got:', res

# call a C function with a C function pointer
res = lib.call_function_pointer(cb, 7)
print 'got:', res

# call a C function with a C function pointer
res = lib.call_
