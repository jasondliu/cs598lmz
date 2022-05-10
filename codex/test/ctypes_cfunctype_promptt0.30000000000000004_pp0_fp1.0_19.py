import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# test calling a function pointer

Callable = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# call a function pointer
func = Callable(42)
assert func(1) == 42

# call a function pointer through a pointer
pfunc = ctypes.pointer(func)
assert pfunc[0](1) == 42

# call a function pointer through a pointer
# that was returned by a function
pfunc = lib.pointer_to_function(Callable(42))
assert pfunc[0](1) == 42

# call a function pointer through a pointer
# that was returned by a function
pfunc = lib.pointer_to_function(Callable(42))
assert pfunc[0](1) == 42

# call a function pointer through a pointer
# that was passed to a function
lib.call_through_ptr(Callable(42), 1) == 42

# call a function pointer through a
