import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def my_c_func(x):
    return x**2

my_c_func_p = FUNTYPE(my_c_func)

def my_func(x):
    return my_c_func_p(x)

my_func(2)

# The following is equivalent to the above, but a bit more efficient

my_c_func_p = ctypes.cast(my_c_func, FUNTYPE)

def my_func(x):
    return my_c_func_p(x)

my_func(2)
</code>

