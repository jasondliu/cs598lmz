import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

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

def _unwrap_function(function):
    """
    Unwrap a function so that it can be called from Python.
    """
    return function

def _unwrap_function_pointer(function_pointer):
    """
    Unwrap a function pointer so that it can be called from Python.
    """
    return function_pointer

def _wrap_function_pointer_array(function_pointer_array):
    """
    Wrap a function pointer array so that it can be called from C.
    """
    return (FUNTYPE * len(function_pointer_array))(*function_pointer_array)

def _unwrap_function_pointer_array(function_pointer_array):
    """
   
