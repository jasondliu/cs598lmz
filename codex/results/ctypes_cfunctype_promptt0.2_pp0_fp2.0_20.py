import ctypes
# Test ctypes.CFUNCTYPE

# This test is for the CFUNCTYPE() function, which creates
# callable objects from C function pointers.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# A simple function

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(
    ("myfunc", lib),
    ((1, "x"),))

assert func(42) == 42

# A function with a pointer argument

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(
    ("myfunc_p", lib),
    ((1, "x"),))

assert func(42) == 42

# A function with a pointer argument, the pointer points to an integer

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))(
    ("myfunc_p", lib),
    ((1, "x"),))

x = ctypes
