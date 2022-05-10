import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double))

def _extend_signature(func, nargout):
    """Extend signature of function to have nargout return values"""
    def newfunc(*args, **kwargs):
        nargs = len(args)
        if nargs > nargout:
            raise TypeError('%s() takes at most %d argument%s (%d given)' % (func.__name__, nargout,
                                                                             's' if nargout != 1 else '', nargs))
        return func(*args, **kwargs)
    newfunc.__name__ = func.__name__
    newfunc.__doc__ = func.__doc__
    return newfunc

def _make_function(name, nargout):
    """Create a function that can be called with any number of arguments up to
    nargout, and return a tuple of values.

    For example, calling the returned function with one argument will return a
    tuple of length nargout. Calling the returned function with more
