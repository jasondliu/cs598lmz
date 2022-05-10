import ctypes
# Test ctypes.CFUNCTYPE()
# define a callback function to be used with CFUNCTYPE
@ctypes.CFUNCTYPE(None)
def hello_func():
    print("Hello, World!")

# obtain a function pointer to the callback
hello_func_ptr = hello_func.ctypes.data

# set the function pointer on the ctypes objects
hello_func.ctypes.data = None
assert hello_func is None

# recover the function pointer from the ctypes object
hello_func = ctypes.CFUNCTYPE(None).from_address(hello_func_ptr)
assert hello_func is not None
