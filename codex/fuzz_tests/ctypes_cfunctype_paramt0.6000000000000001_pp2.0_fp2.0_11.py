import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

def my_function(x):
    return x

my_function_pointer = FUNTYPE(my_function)

print(my_function_pointer(5))
