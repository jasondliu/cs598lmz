import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# The prototype is:
# int (__stdcall *func)(int)
func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("func", lib))

print func(42)

# The prototype is:
# int (__stdcall *func2)(int, int)
func2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(("func2", lib))

print func2(42, 43)

# The prototype is:
# int (__stdcall *func3)(int, int, int)
func3 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(("func3", lib))

print func3(42, 43, 44)

# The prototype is:
# int (__stdcall *func
