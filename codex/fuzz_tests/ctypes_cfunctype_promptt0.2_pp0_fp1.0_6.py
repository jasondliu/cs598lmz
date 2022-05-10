import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call_function

def call_function(func, *args):
    func.restype = ctypes.c_int
    func.argtypes = [ctypes.c_int] * len(args)
    return func(*args)

# callback

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(arg):
    return arg + 1

CALLBACK_FUNC = CALLBACK(callback)

# test_call_function

def test_call_function():
    assert call_function(lib.add, 1, 2) == 3
    assert call_function(lib.sub, 1, 2) == -1
    assert call_function(lib.mul, 2, 3) == 6
    assert call_function(lib.div, 10, 2) == 5
    assert call_function(lib.mod, 10, 3) == 1
    assert call_function
