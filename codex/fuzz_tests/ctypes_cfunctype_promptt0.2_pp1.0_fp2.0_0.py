import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function pointer type, it should be callable
# and should have a restype attribute.

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib._testfunc_p_p)

print func(5)

# This is a pointer to a function pointer type, it should be
# callable and should have a restype attribute.

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib._testfunc_pp_p)

print func(5)

# This is a pointer to a function pointer type, it should be
# callable and should have a restype attribute.

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib._testfunc_pp_p)

print func(5)

# This is a pointer to a function pointer type, it should be
#
