import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def get_args(func, narg=None, **kwargs):
    """
    Get the arguments for the function.

    If narg is given, then it is the number of required arguments.
    If narg is None, then the function is called and the number of
    required arguments is determined from the function.

    All other keyword arguments are passed to the function.
    """
    if narg is None:
        args = [None]*func.__code__.co_argcount
        func(*args)
        args = [x for x in args if x is not None]
        return tuple(args)
    else:
        return tuple(kwargs.get('x%s' % (i+1), 0) for i in range(narg))

def get_func(code, namespace):
    """
    Return a function corresponding to the code object.
    """
    return eval(code, namespace)

class TestRoutine(object):
    """
    TestRoutine(code, [narg=None],
