import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Test if a CFUNCTYPE(c_int) can be called with a Python int argument
# and returns a Python int.

Callable = ctypes.CFUNCTYPE(ctypes.c_int)

func = Callable(lib.square)
assert func(5) == 25

# Test if a CFUNCTYPE(c_int) can be called with a c_int argument
# and returns a c_int.

func = Callable(lib.square)
assert func(ctypes.c_int(5)) == 25

# Test if a CFUNCTYPE(c_int) can be called with a Python int argument
# and returns a c_int.

func = Callable(lib.square)
assert func(5).value == 25

# Test if a CFUNCTYPE(c_int) can be called with a c_int argument
# and returns a Python int.

func = Callable(lib.square
