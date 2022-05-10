import ctypes
# Test ctypes.CFUNCTYPE for a function that takes a function pointer
# as an argument.

# This is a callback function
def funcptr_callback(arg):
    print('funcptr_callback called with', arg)
    return arg + 1

# This is the function that takes a function pointer as an argument
def funcptr_func(funcptr):
    print('funcptr_func calling callback with 42')
    return funcptr(42)

# This is the type of the function that takes a function pointer as an argument
funcptr_func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the type of the callback function
funcptr_callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function pointer
funcptr = funcptr_callback_type(funcptr_callback)

# This is the function that takes a function pointer as an argument
funcptr_func = funcptr_func_type(funcptr_func)

# This is the call
