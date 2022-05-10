import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(*args):
    return args

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# call callback directly
res = CALLBACK(func)(1, 2)
if res != (1, 2):
    raise RuntimeError("wrong result")

# call callback via CFUNCTYPE.__call__
res = CALLBACK.__call__(func)(1, 2)
if res != (1, 2):
    raise RuntimeError("wrong result")

# call callback via CFUNCTYPE.__call__
res = CALLBACK.__call__(func, 1, 2)
if res != (1, 2):
    raise RuntimeError("wrong result")

# call callback via dll
res = lib.test_callback(CALLBACK(func), 1, 2)
if res != (1, 2):
    raise RuntimeError("wrong result")


