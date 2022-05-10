import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(*args):
    return args

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

result = lib.set_callback(callback)
if result != (1, 2):
    raise RuntimeError("CFUNCTYPE callback failed")

# Test ctypes.WINFUNCTYPE

WINFUNCTYPE = ctypes.WINFUNCTYPE

def func(*args):
    return args

CALLBACK = WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

result = lib.set_callback(callback)
if result != (1, 2):
    raise RuntimeError("WINFUNCTYPE callback failed")

# Test ctypes.PYFUNCTYPE

PYFUNCTYPE
