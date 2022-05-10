import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# define a callback function
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def py_cmp_func(a, b):
    print('py_cmp_func', a, b)
    return a - b

cmp_func = CMPFUNC(py_cmp_func)

# call a C function with a callback
lib.set_callback(cmp_func)
lib.call_callback(2, 3)

# call a C function with a callback, and pass some data

class DATA(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

d = DATA(4, 5)
lib.set_callback_data(cmp_func, ctypes.byref(d))
lib.call_callback(2, 3)

# try callbacks
