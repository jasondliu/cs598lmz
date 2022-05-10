import ctypes
# Test ctypes.CFUNCTYPE

# Test ctypes.CFUNCTYPE(None)

import _ctypes_test

def func():
    pass

CALLBACK = ctypes.CFUNCTYPE(None)

# The callback is called, but the argument is ignored
res = _ctypes_test.test_callback(CALLBACK(func), 1)
if res != 0:
    raise RuntimeError("Wrong result")

# Test ctypes.CFUNCTYPE(ctypes.c_int)

def func(arg):
    return arg + 1

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int)

res = _ctypes_test.test_callback(CALLBACK(func), 1)
if res != 2:
    raise RuntimeError("Wrong result")

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(arg1, arg2):
    return arg1 + arg2

CALLBACK = ctypes.CFUNCTYPE(ctypes.
