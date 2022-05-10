import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

def _wrap_function(lib, func, restype=None, argtypes=()):
    """Simplify wrapping ctypes functions.
    Takes a library object, a string name of the function, its restype
    and argtypes.  Returns a wrapped function that can be called with
    Python types and is more friendly to the interactive interpreter.
    """
    func = lib.__getattr__(func)
    func.restype = restype
    func.argtypes = argtypes
    func.__name__ = func.__name__.replace('_', ' ')
    return func

def _wrap_functions(lib, funcs, restype=None, argtypes=()):
    """Wrap multiple functions from a ctypes library."""
    return [_wrap_function(lib, func, restype, argtypes) for func in funcs]

def _wrap_constants(lib, constants):
    """Wrap multiple constants from a ctypes library."""
    lib_dict = lib.__dict__
    return [(name, lib_dict
