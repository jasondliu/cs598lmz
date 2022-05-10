import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def makefunction(expression, name, lambda_fun=None, lib=None, fun=None,
                 fun_type=FUNTYPE):
    """Make a C function from a mathematical expression.

    Parameters
    ----------
    expression : str
        Mathematical expression.  'x' will be the only independent
        variable.
    name : str
        Function name.
    lambda_fun : python function, optional
        If not None, use this function instead of creating a new one.
    lib : ctypes.cdll, optional
        Library where the function will be loaded.
    fun : ctypes.CDLL.function, optional
        Pointer to function.
    fun_type : ctypes.CFUNCTYPE, optional
        Type of function pointer.

    Returns
    -------
    lib : ctypes.cdll
    fun : ctypes.CDLL.function

    Examples
    --------
    >>> lib, fun = makefunction("sin(x)", "mysin")
    >>> lib.mysin(0.0)
    0
