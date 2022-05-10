import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Simple function call

# Callback function prototype
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Callback function
def func(a, b):
    print 'func', a, b
    return a + b

# Callback function as argument
lib.use_callback(CALLBACKFUNC(func))

# Callback function as value
lib.use_callback(CALLBACKFUNC(func))

# Callback function as global variable
CALLBACK = CALLBACKFUNC(func)
lib.use_callback(CALLBACK)

# Callback function as attribute of a local variable
class X(object):
    pass
x = X()
x.CALLBACK = CALLBACKFUNC(func)
lib.use_callback(x.CALLBACK)

# Callback function as attribute of a global variable
class Y(object):
