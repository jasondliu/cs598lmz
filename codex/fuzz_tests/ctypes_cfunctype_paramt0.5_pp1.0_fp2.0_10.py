import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def c_function(py_function):
    """
    Create a ctypes version of the python function.
    """
    def c_function_caller(x):
        return py_function(x)
    return FUNTYPE(c_function_caller)

# now we can use c_function as a decorator
@c_function
def py_function(x):
    return x**2
</code>

