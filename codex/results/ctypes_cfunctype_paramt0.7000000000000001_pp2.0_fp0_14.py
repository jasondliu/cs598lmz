import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def get_pyfunc(f):
    """
    get the python function for a sympy function.
    """
    return lambdify(f.args, f.expr, 'numpy')

def get_cfunc(f):
    """
    get the c function for a sympy function.
    """
    return lambdify(f.args, f.expr, 'C')

def get_ctypes_func(f):
    """
    get the ctypes function for a sympy function.
    """
    return FUNTYPE(get_cfunc(f))

def get_dwrapper(f, t, range_=(0, 1), h=None):
    """
    wrapper the first derivative of a sympy function.
    """
    fp = f.diff(t)
    if not fp.has(t):
        return fp.evalf(subs={t: range_[1] - range_[0]})
    if h is None:
        h = 0.01

