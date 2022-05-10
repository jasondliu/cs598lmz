import ctypes
# Test ctypes.CFUNCTYPE()

def func(x):
	return x + 1

# Create a function pointer type
func_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Create a function pointer
func_ptr_obj = func_ptr(func)

# Call the function pointer
print(func_ptr_obj(1))
