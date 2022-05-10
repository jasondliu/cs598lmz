import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def vectorize_function(pyfunc, otypes=None, doc=None, excluded=None, cache=False, signature=None):
    """
    Generalized function class.
    Can be used to vectorize a scalar function (i.e., make it apply to arrays),
    or to build new functions of several arguments based on a function of one
    argument (reusing the one-argument function's code).

    Parameters
    ----------
    pyfunc : callable
        A Python function, or a user-defined function.
    otypes : str or list of dtypes, optional
        Desired output type(s) of the vectorized function.  If not given
        (the default) the output type is inferred from the type of the
        output values of `pyfunc`.
    doc : str, optional
        The docstring for the vectorized function.  If None (the default),
        then the docstring is the same as that of `pyfunc`.
    excluded : set, optional
        Set of strings, each designating a keyword that cannot be
