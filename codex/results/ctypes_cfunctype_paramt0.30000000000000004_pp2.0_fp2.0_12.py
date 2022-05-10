import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def _wrap_function(function):
    """
    Wrap a function so that it can be called from C.
    """
    return FUNTYPE(function)

def _wrap_function_pointer(function_pointer):
    """
    Wrap a function pointer so that it can be called from C.
    """
    return FUNTYPE(function_pointer)

def _wrap_function_pointer_array(function_pointer_array):
    """
    Wrap a function pointer array so that it can be called from C.
    """
    return (FUNTYPE * len(function_pointer_array))(*function_pointer_array)

def _wrap_function_pointer_array_2d(function_pointer_array_2d):
    """
    Wrap a function pointer array so that it can be called from C.
    """
    return (FUNTYPE * len(function_pointer_array_2d) * len(function_pointer_array_2d[0]))(*function_pointer_array_2d)

def _wrap_function
