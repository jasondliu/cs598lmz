import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(*args):
    print(args)

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

_ctypes_test.set_callback(CALLBACK(func))
_ctypes_test.call_callback(1, 2)

# check that the callback is really called
try:
    _ctypes_test.call_callback(1, 2)
except RuntimeError:
    pass
else:
    raise RuntimeError("callback not called")

# check that the callback can be changed
def func2(*args):
    print(args)

_ctypes_test.set_callback(CALLBACK(func2))
_ctypes_test.call_callback(1, 2)

# check that the callback can be cleared
_ctypes_test.set_callback(CALLBACK(None))
_ctypes_test.call_callback(1, 2)

# check that the callback can be set again
_ctypes_
