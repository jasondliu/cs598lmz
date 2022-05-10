import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def my_callback(a, b):
    print(a, b)
    return a+b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# test the callback as a function
_ctypes_test.set_callback(CMPFUNC(my_callback))
print(_ctypes_test.call_callback(3, 4))

# test the callback as an object
cb = CMPFUNC(my_callback)
_ctypes_test.set_callback(cb)
print(_ctypes_test.call_callback(3, 4))

# test the callback as a class
class Callback:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        return self.func(*args)

cb = Callback(my_callback)
_ctypes_test.set_callback(CMPFUNC(cb))
print(_ctypes_test.
