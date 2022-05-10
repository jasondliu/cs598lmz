import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is not exported by the dll, so using
# a function pointer is the only way to call it.
#
# Hm, cdecl calling convention is the default on Windows...
cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("_testfunc_callback", lib))

# This function is exported by the dll, so we can get a
# function pointer to it by simple name access.
func = lib.testfunc_callback

for func in cfunc, func:
    res = func(1)
    if res != 42:
        raise RuntimeError("callback failed")

################################################################

# Test ctypes.WINFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function is not exported by the dll, so using
# a function pointer is the only way to call it.
func = ctypes
