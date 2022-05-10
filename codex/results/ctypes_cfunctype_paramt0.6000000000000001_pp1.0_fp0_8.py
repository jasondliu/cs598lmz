import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def call_c_function(c_function, value):
    return c_function(value)

def call_c_function_ptr(c_function_ptr, value):
    return c_function_ptr(value)

def call_c_function_funtype(c_function_ptr, value):
    c_function = FUNTYPE(c_function_ptr)
    return c_function(value)

# Use the C function.
x = 2.0
print(call_c_function(c_sin, x))
print(call_c_function(c_cos, x))

# Use the C function pointer.
print(call_c_function_ptr(c_sin, x))
print(call_c_function_ptr(c_cos, x))

# Use the C function pointer with FUNTYPE.
print(call_c_function_funtype(c_sin, x))
print(call_c_function_funtype(c_cos, x))

# Use the Python math module
