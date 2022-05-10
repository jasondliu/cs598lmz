import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def c_function(f):
    return FUNTYPE(f)

def c_function_ptr(f):
    return ctypes.cast(c_function(f), ctypes.c_void_p).value

def c_function_ptr_from_pyfunc(f):
    return ctypes.cast(c_function(f), ctypes.c_void_p).value

def c_function_ptr_from_cfunc(f):
    return ctypes.cast(f, ctypes.c_void_p).value

def c_function_ptr_from_cfunc_ptr(f):
    return ctypes.cast(f, ctypes.c_void_p).value

def c_function_ptr_from_cfunc_ptr_ptr(f):
    return ctypes.cast(f, ctypes.c_void_p).value

def c_function_ptr_from_cfunc_ptr_ptr_ptr(f):
    return ctypes.cast(f, ctypes.
