import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

dll = ctypes.CDLL(_ctypes_test.__file__)

# call a simple function
func = dll._testfunc_p_p
func.restype = ctypes.c_void_p
func.argtypes = (ctypes.c_void_p,)

# call a function which returns a pointer to a function
func2 = dll._testfunc_p_p
func2.restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
func2.argtypes = (ctypes.c_void_p,)

# call a function which returns a pointer to a function
func3 = dll._testfunc_p_p
func3.restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
func3.argtypes = (ctypes.c_void_p,)

# call a function which returns a pointer to a function
func4 = dll._testfunc_p_p
func4.restype =
