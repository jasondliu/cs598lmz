import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

# Create a function pointer
func_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

# Call the function pointer
print(func_ptr(1, 2))

# Test ctypes.WINFUNCTYPE
def func(a, b):
    return a + b

# Create a function pointer
