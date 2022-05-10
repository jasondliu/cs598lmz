import ctypes
# Test ctypes.CFUNCTYPE and ctypes.c_void_p
# For example, declare a function and pass it to another function
# as an argument

# declare a function with ctypes.CFUNCTYPE
# it takes one parameter of type c_void_p and returns a c_void_p
CFUNCTYPE_FUNC = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

# function to be passed as argument, takes a c_void_p and
# returns a c_void_p
def func_to_pass(obj):
    print("func_to_pass is called on ", obj)
    return obj

# wrap func_to_pass with CFUNCTYPE
# and pass it as an argument to another function
func_ptr = CFUNCTYPE_FUNC(func_to_pass)

# another function that takes a function pointer
def call_func(func, obj):
    print("call_func is called with ", obj)
    return func(obj)

# call the function with func_ptr as argument
