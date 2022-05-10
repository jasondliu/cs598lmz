import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

def make_funtype(n):
    """
    >>> make_funtype(0)(fun)()
    'fun'
    >>> make_funtype(1)(fun, None)()
    'fun'
    >>> make_funtype(2)(fun, None, None)()
    'fun'
    """
    return FUNTYPE(n)

def make_argument_type(n):
    """
    >>> make_argument_type(0)(fun)()
    'fun'
    >>> make_argument_type(1)(fun, None)()
    'fun'
    >>> make_argument_type(2)(fun, None, None)()
    'fun'
    """
    return ctypes.CFUNCTYPE(ctypes.py_object, *([ctypes.py_object] * n))

def make_argument_type_and_call(n):
    """
    >>> make_argument_type_and_call(0)(fun)()
    'fun'
    >>> make_argument_type_and_call(1
