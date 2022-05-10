import ctypes
# Test ctypes.CFUNCTYPE

# This is how you declare the prototype of a function that returns a
# pointer to a function that returns an integer.

int_func = ctypes.CFUNCTYPE(ctypes.c_int)

# This is how you declare a function that returns a pointer to a
# function that returns an integer.

prototype = ctypes.CFUNCTYPE(int_func)

# This is how you declare a function that takes a pointer to a function
# that returns an integer.

prototype2 = ctypes.CFUNCTYPE(None, int_func)

# This is how you call the function.

result = prototype()

# This is how you call the function that returns the pointer to a
# function.

result2 = result()

# This is how you call the function that returns the pointer to a
# function, and then call the function.

result3 = result()(42)

# This is how you call the function that takes a pointer to a function
# as an argument.

result4 = prototype2(result)

# This is how you call
