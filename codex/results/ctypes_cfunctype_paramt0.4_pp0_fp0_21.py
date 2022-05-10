import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

# Define a function that takes a function pointer as an argument.
def call_func(fn):
    return fn()

# Wrap the function pointer in a function object.
func_obj = FUNTYPE(lambda: 1)

# Pass the function object to the calling function.
print(call_func(func_obj))
</code>

