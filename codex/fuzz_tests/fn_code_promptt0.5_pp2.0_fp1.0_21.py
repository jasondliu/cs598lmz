fn = lambda: None
# Test fn.__code__ for python 2 or 3
fn.__code__ = None

if fn.__code__ is None:
    def _get_code(func):
        return func.__code__
else:
    def _get_code(func):
        return func.__code__.co_code


def _get_arg_names(func):
    """
    Get the argument names for a function.
    """
    if six.PY2:
        return inspect.getargspec(func).args
    elif six.PY3:
        return inspect.getfullargspec(func).args
    else:
        raise RuntimeError("Unknown Python version")


def _get_default_args(func):
    """
    Get the default arguments for a function.
    """
    if six.PY2:
        return inspect.getargspec(func).defaults
    elif six.PY3:
        return inspect.getfullargspec(func).defaults
    else:
        raise RuntimeError("Unknown Python version")


def _get_kwonly_default_args(func
