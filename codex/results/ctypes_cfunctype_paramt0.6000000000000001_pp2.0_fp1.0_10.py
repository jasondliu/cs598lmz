import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

# Create a constant function pointer
const_func_ptr = FUNTYPE(0)

# Create a callback function
def callback_func(arg):
    print(arg)
    return 0

# Create a callback function pointer
callback_func_ptr = FUNTYPE(callback_func)

# Create a variable function pointer
var_func_ptr = FUNTYPE(None)

# Assign function to variable function pointer
var_func_ptr = callback_func_ptr

# Call variable function pointer
var_func_ptr('Hi!')

# Call constant function pointer
const_func_ptr('Hi!')

# Call callback function pointer
callback_func_ptr('Hi!')
</code>

