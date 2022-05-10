import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

def c_function(f):
    return FUNTYPE(f)

def c_function_pointer(f):
    return ctypes.cast(c_function(f), ctypes.c_void_p).value

def c_function_pointer_from_pyfunc(f):
    return ctypes.cast(c_function(f), ctypes.c_void_p).value

def c_function_pointer_from_cfunc(f):
    return ctypes.cast(f, ctypes.c_void_p).value

def c_function_pointer_to_pyfunc(f):
    return ctypes.cast(ctypes.c_void_p(f), FUNTYPE)

def c_function_pointer_to_cfunc(f):
    return ctypes.cast(ctypes.c_void_p(f), FUNTYPE)


def c_function_pointer_to_cfunc_pointer(f):
    return ctypes.cast(ctypes.c_void_p(f),
