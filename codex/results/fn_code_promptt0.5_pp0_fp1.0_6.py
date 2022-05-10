fn = lambda: None
# Test fn.__code__.co_flags
_test_fn.__code__.co_flags = 0

# See https://docs.python.org/3/library/inspect.html#inspect.getcallargs
# for details on how callargs() works.
#
# This code is modified from the inspect module in the Python standard
# library.

def _check_is_multivalue_arg(name, value):
    """
    Check whether a parameter name and value correspond to a multivalue
    argument.

    Parameters
    ----------
    name : str
        The name of the parameter.
    value : object
        The value of the parameter.

    Returns
    -------
    is_multivalue_arg : bool
        Whether the parameter name and value correspond to a multivalue
        argument.
    """
    if name in _multivalue_special_params:
        return True
    elif name.endswith(_multivalue_special_params_suffixes):
        return True
    elif isinstance(value, Iterable) and not isinstance(value, str):
       
