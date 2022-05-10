import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print(args)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

_ctypes_test.set_callback(CALLBACK(func))

_ctypes_test.call_callback(1, 2)

# Test ctypes.WINFUNCTYPE

def func(*args):
    print(args)

CALLBACK = ctypes.WINFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

_ctypes_test.set_callback(CALLBACK(func))

_ctypes_test.call_callback(1, 2)

# Test ctypes.PYFUNCTYPE

def func(*args):
    print(args)

CALLBACK = ctypes.PYFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

_ctypes_test.set_callback(CALLBACK(func))

_
