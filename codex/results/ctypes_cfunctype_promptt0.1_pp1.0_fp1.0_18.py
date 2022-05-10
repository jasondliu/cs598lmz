import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function pointer type, it can be used to create
# function pointers.
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is a function pointer instance.
func = FUNC(lib._testfunc_p_p)

# This is a function pointer instance.
func2 = FUNC(lib._testfunc_p_p)

# This is a function pointer instance.
func3 = FUNC(lib._testfunc_p_p)

# This is a function pointer instance.
func4 = FUNC(lib._testfunc_p_p)

# This is a function pointer instance.
func5 = FUNC(lib._testfunc_p_p)

# This is a function pointer instance.
func6 = FUNC(lib._testfunc_p_p)

# This is a function pointer instance.
func7 = FUNC(lib._testfunc_p_p
