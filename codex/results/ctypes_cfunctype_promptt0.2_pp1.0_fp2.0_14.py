import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a simple function

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("myfunc", lib))
assert func(3) == 3

# a function with a pointer argument

func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))(("myfunc", lib))

i = ctypes.c_int(42)
assert func(i) == 42

# a function with a pointer argument, and a pointer return value

func = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))(("myfunc", lib))

i = ctypes.c_int(42)
assert func(i).value == 42

# a function with a pointer argument, and a pointer return value
# the pointer return value is the same as the pointer argument
