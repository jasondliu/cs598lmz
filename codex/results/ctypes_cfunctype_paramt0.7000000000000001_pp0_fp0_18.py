import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

class _pysql_wrapper(ctypes.Structure):
    _fields_ = [('py_type', FUNTYPE),
                ('py_func', ctypes.py_object)]

def sql_func(func):
    """
    Wrapper function that allows to register a function as an SQL function.

    This function is a decorator that allows to register a python function
    as an SQL function.

    Args:
        func (function): the function to register as an SQL function.

    Returns:
        function: the decorated function.
    """
    if len(inspect.getargspec(func).args) != 3:
        raise TypeError("Function must have exactly 3 arguments")
    if not callable(func):
        raise TypeError("Function must be callable")
    def _inner(*args, **kwargs):
        if len(kwargs) > 0:
            raise TypeError("Arguments must be passed by position.")
        if len(args) < 2:
            raise TypeError("Function must be called with at least two arguments")
       
