import ctypes
# Test ctypes.CFUNCTYPE

# This is the prototype of the function we will call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the actual function we will call
def my_function(a, b):
    return a + b

# This is the function we will call
my_function_ptr = prototype(my_function)

# Call the function
print(my_function_ptr(1, 2))

# Test ctypes.WINFUNCTYPE

# This is the prototype of the function we will call
