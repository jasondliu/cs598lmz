import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def cfunc(func):
    return FUNTYPE(func)

def cfunc_wrapper(func):
    def _func(*args):
        return func(*args)
    return cfunc(_func)

def cfunc_with_cfunc_arg(func):
    def _func(arg):
        return func(cfunc(arg))
    return cfunc(_func)

class CClass(ctypes.Structure):
    _fields_ = [('data', ctypes.c_int)]

CClass_p = ctypes.POINTER(CClass)

def cfunc_with_CClass_arg(func):
    def _func(arg):
        return func(CClass_p(arg))
    return cfunc(_func)

def cfunc_with_cfunc_arg_and_CClass_arg(func):
    def _func(arg1, arg2):
        return func(cfunc(arg1), CClass_p(arg2))
    return cfunc(_func)


