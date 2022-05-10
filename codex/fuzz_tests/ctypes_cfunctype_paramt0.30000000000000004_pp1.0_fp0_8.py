import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

def _wrap_func(func, argtypes, restype):
    """
    Wrap a function so that it can be called as if it were a Python function.
    """
    cfunc = FUNTYPE(func, argtypes, restype)
    def func_wrapper(*args):
        return cfunc(*args)
    func_wrapper.__name__ = func.__name__
    return func_wrapper

def _wrap_funcs(module, funcs, argtypes, restype):
    """
    Wrap a set of functions so that they can be called as if they were Python
    functions.
    """
    for func in funcs:
        setattr(module, func.__name__, _wrap_func(func, argtypes, restype))

def _wrap_class(cls, argtypes, restype):
    """
    Wrap a class so that its methods can be called as if they were Python
    functions.
    """
    for name, func in cls.__dict__.items():
        if callable(func):
            set
