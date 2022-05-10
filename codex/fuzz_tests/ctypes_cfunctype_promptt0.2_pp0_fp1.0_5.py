import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function pointer type, it can be used to create
# function pointers.
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is a function pointer, it can be called.
func = FUNC(("_testfunc_callback", lib), ((1,),))

# Calling the function pointer should cause the callback
# function to be called.
assert func(3) == 3

# This is a function pointer type, it can be used to create
# function pointers.
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is a function pointer, it can be called.
func = FUNC(("_testfunc_callback", lib), ((1,),))

# Calling the function pointer should cause the callback
# function to be called.
assert func(3) == 3

# This is a function pointer type, it can
