import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Define a function that takes a function pointer as an argument
def call_func(func):
    return func(0.0)

# Define a function that takes a function pointer as an argument
def call_func_with_arg(func, arg):
    return func(arg)

# Define a function that takes a function pointer as an argument
def call_func_with_args(func, arg1, arg2):
    return func(arg1, arg2)

# Define a function that takes a function pointer as an argument
def call_func_with_args_and_ret(func, arg1, arg2):
    return func(arg1, arg2)

# Define a function that takes a function pointer as an argument
def call_func_with_args_and_ret_and_kwargs(func, arg1, arg2, kwarg1=1.0, kwarg2=2.0):
    return func(arg1, arg2, kwarg1, kwarg2)
