import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# this function is declared as:
# void call_int_callback(int (*func)(int))

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_callback(arg):
    print("py_callback", arg)
    return arg + 42

cb = CALLBACK(py_callback)
lib.call_int_callback(cb)

# call a function with a function pointer argument
# this function is declared as:
# void call_void_callback(void (*func)(void))

CALLBACK = ctypes.CFUNCTYPE(None)

def py_callback():
    print("py_callback")

cb = CALLBACK(py_callback)
lib.call_void_callback(cb)

# call a function with a function pointer argument
# this function is declared as:
# void call_void_callback(void (*
