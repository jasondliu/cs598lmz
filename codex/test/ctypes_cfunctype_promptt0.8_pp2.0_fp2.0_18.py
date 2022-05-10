import ctypes
# Test ctypes.CFUNCTYPE()
# python_obj = ctypes.CFUNCTYPE(result, arg1, arg...)
# result is one of [void, int, float, double, POINTER(c_int), POINTER(c_float)]
# arg is one of [int, float, double, POINTER(c_int), POINTER(c_float)]

# int function(int)
test_int_int = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# float function(float)
test_float_float = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float)

# double function(double)
test_double_double = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# int function(float)
test_int_float = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float)

# int function(double)
