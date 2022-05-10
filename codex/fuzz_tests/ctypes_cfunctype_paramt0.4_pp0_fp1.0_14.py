import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

def get_func_ptr(func):
    cfunc = FUNTYPE(func)
    return ctypes.cast(cfunc, ctypes.c_void_p).value

def get_func_from_ptr(ptr):
    return ctypes.cast(ptr, FUNTYPE).value

def func_ptr_to_py(ptr):
    return get_func_from_ptr(ptr)

def py_to_func_ptr(func):
    return get_func_ptr(func)

def func_ptr_to_c(ptr):
    return ctypes.cast(ptr, FUNTYPE)

def c_to_func_ptr(cfunc):
    return ctypes.cast(cfunc, ctypes.c_void_p).value
</code>

