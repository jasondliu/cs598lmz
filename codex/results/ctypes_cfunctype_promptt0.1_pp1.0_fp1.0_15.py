import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

def callback(x, y):
    print("callback", x, y)
    return x + y

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

lib.set_callback(CALLBACK(callback))

lib.call_callback(1, 2)

# call a function with a callback argument, and pass None

lib.set_callback(CALLBACK(None))

try:
    lib.call_callback(1, 2)
except ValueError:
    print("ValueError")

# call a function with a callback argument, and pass a callback
# function that raises an exception

def callback_exception(x, y):
    print("callback_exception", x, y)
    raise ValueError

lib.set_callback(CALLBACK(callback_exception))

try:
   
