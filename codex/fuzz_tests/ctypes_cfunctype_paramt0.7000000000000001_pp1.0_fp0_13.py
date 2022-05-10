import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)


def c_func_to_py(cfunc, argtypes=None):
    """
    Convert a ctypes function to a python function.
    """
    return FUNTYPE((argtypes or []), cfunc)


def c_func_name(cfunc):
    return cfunc.__name__

#------------------------------------------------------------------------
# Utilities for manipulating function signatures
#------------------------------------------------------------------------


def unpack_signature(f):
    """
    Return a tuple (name, args, vararg, kwarg) of the signature of a
    function.

    If the function is a Numba function, then the signature of the
    function's underlying PyCFunction is returned.
    """
    if is_cfunc(f):
        return (f.__name__, f.argtypes, f.restype, False)
    elif is_objmode_function(f):
        return (f.__name__, f.argtypes, f.restype, f.kwargs)
    elif is_cython_function(f):
        return (f
