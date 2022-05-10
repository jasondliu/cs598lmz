import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function that takes an int and returns an int
func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("myfunc", lib), ((1, "a"),))
assert func(3) == 3

# a function that takes an int and a pointer to an int, and returns
# a pointer to a function taking an int and returning an int
func2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))(("myfunc2", lib), ((1, "a"), (2, "b")))
a = ctypes.c_int(5)
assert func2(3, ctypes.byref(a))(5) == 8
assert a.value == 8

# a function that takes an int and a pointer to an int, and returns
# a pointer to a function taking an int and returning an int
func3 =
