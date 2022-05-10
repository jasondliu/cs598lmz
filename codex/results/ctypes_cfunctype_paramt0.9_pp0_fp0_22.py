import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

def register(name, func):
    """Register a Python function as a fn (fascinating name, isn't it?)"""
    fun = FUNTYPE(func)
    lib.fn_register(name.encode('utf-8'), fun)
    return fun

def get(name):
    """Get a (C-defined) fn by name"""
    return lib.fn_get(name.encode('utf-8'))

def _get_body(fn):
    if isinstance(fn, str):
        return fn
    elif callable(fn):
        return fn.__globals__[fn.__name__]
    elif isinstance(fn, tuple):
        return fn[-1]
    else:
        return ""

def arity(fn):
    """Get the arity of a fn"""
    return int(lib.fn_arity(_get_body(fn)))

def apply(fn, *args):
    """Apply a fn with the given args"""
    return lib.fn_apply(_get_body
