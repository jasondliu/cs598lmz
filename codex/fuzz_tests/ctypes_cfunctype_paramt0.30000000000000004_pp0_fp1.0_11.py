import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def c_function(func):
    cfunc = FUNTYPE(func)
    return cfunc

def c_function_pointer(func):
    cfunc = FUNTYPE(func)
    return ctypes.cast(cfunc, ctypes.c_void_p).value

def c_function_pointer_from_object(obj, funcname):
    func = getattr(obj, funcname)
    cfunc = FUNTYPE(func)
    return ctypes.cast(cfunc, ctypes.c_void_p).value

def c_function_pointer_from_class(cls, funcname):
    func = getattr(cls, funcname)
    cfunc = FUNTYPE(func)
    return ctypes.cast(cfunc, ctypes.c_void_p).value

def c_function_pointer_from_module(module, funcname):
    func = getattr(module, funcname)
    cfunc = FUNTYPE(func)
    return ctypes.cast(cfunc,
