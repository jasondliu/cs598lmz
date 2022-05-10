import ctypes
# Test ctypes.CFUNCTYPE on a simple function.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

FuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

func = FuncPtr((b"myfunc", lib))

# call it
assert func(6, 7) == 42

# create a new function from it
func2 = FuncPtr(func)
assert func2(6, 7) == 42

# call the function from C
assert lib.call_func(func, 6, 7) == 42

# call the function from C using the second function
assert lib.call_func(func2, 6, 7) == 42
