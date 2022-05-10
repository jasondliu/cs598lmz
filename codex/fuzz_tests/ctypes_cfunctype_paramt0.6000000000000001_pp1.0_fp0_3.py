import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def get_function(function_name):
    """Returns the function with the name 'function_name'"""
    try:
        return getattr(math, function_name)
    except AttributeError:
        return None

def get_function_ptr(function):
    """Returns a CFuntype function pointer for the function"""
    if function is None:
        return None
    return FUNTYPE(function)

def get_function_ptrs(function_names):
    """Returns a list of function pointers for the functions with the names in 'function_names'"""
    return [get_function_ptr(get_function(function_name)) for function_name in function_names]

def get_function_names(function_ptrs):
    """Returns a list of the names of the functions in 'function_ptrs'"""
    return [function.__name__ for function in function_ptrs]

def get_function_name(function_ptr):
    """Returns the name of the function in 'function_ptr'"""

