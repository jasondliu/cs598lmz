import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# define the callback function
def my_function(x):
    return x * x * x

# convert the function to a C pointer
my_function_ptr = FUNTYPE(my_function)

# call the function pointer
print(my_function_ptr(2.0))
print(my_function_ptr(3.0))

def my_function(x):
    return x * x * x

def my_function_ptr(x):
    return x * x * x

print(my_function(2.0))
print(my_function_ptr(2.0))
