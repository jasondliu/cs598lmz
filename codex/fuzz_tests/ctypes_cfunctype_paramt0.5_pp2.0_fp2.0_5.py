import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def make_func(func):
    return FUNTYPE(func)

def make_func_c(func):
    return ctypes.cast(make_func(func),ctypes.c_void_p)

def make_func_c_ptr(func):
    return ctypes.POINTER(ctypes.c_void_p)(make_func_c(func))

def call_func(func,arg):
    return func(arg)

def call_func_c(func,arg):
    return call_func(ctypes.cast(func,FUNTYPE),arg)

def call_func_c_ptr(func,arg):
    return call_func(ctypes.cast(func,FUNTYPE),arg)

def func_ptr(funcs):
    return ctypes.cast(funcs,ctypes.c_void_p)

def func_ptr_ptr(funcs):
    return ctypes.cast(ctypes.pointer(funcs),ctypes.c_void_p)
