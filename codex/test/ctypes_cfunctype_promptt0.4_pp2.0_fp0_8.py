import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Callback function prototype
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    print("callback", a, b)
    return a + b

# CallbackTestA
CALLBACKFUNCPA = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

def callbackpa(a):
    print("callbackpa", a[0])
    return a[0]

# CallbackTestW
CALLBACKFUNCPW = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_wchar))

def callbackpw(a):
    print("callbackpw", a[0])
    return a[0]

# CallbackTestWA
