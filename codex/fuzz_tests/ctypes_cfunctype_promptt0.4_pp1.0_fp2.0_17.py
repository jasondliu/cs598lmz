import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# callback function prototype
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# callback function
@CALLBACKFUNC
def callback(a, b):
    print('callback called')
    return a + b

# register callback function
lib.set_callback(callback)

# call callback function
print(lib.call_callback(1, 2))

# Test ctypes.CFUNCTYPE with a structure

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('b', ctypes.c_int)]

@CALLBACKFUNC
def callback2(x, y):
    print('callback2 called')
    return x.a + y.b

lib.set_callback2(callback2)
