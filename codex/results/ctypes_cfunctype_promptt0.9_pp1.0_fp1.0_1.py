import ctypes
# Test ctypes.CFUNCTYPE() by passing a callback which takes a callback and
# calls it immediately.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def func(cb):
    cb(42)

# cb pointer
CBTy1 = ctypes.CFUNCTYPE(None, ctypes.c_int)
CALLCB = CBTy1(func)

lib.pass_callback(CALLCB, ctypes.c_int(15))

# cb pointer & userdata
CBTy2 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_void_p)
CALLCB = CBTy2(func)
lib.pass_callback(CALLCB, ctypes.c_int(15))

# double cb pointer
CBTy3 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
CALLCB = CBTy3(lambda x, y: func(lambda z: func
