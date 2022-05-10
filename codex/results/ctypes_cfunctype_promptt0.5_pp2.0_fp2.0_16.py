import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function taking a callback as first argument
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print('callback called with', value)
    return value * 3

CALLBACKFUNC_CB = CALLBACKFUNC(callback)

lib.set_callback.argtypes = (CALLBACKFUNC, )

lib.set_callback(CALLBACKFUNC_CB)

lib.call_callback(42)

# a function taking a callback as first argument and a userdata pointer as
# second argument
CALLBACKFUNC_USERDATA = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int,
                                         ctypes.c_void_p)

def callback_userdata(value, userdata):
    print('callback_userdata called with', value, userdata)
    return value * 3

