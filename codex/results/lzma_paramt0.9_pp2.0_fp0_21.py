from lzma import LZMADecompressor
LZMADecompressor.names


def _get(d, key, default):
    return d.get(key, default) if d is not None else default


def protect(func, *args, **kwargs):
    """Protect a function from raising exceptions

    Returns a new function that wraps the original function and prevents it
    from crashing the workers. Worker exceptions rise, but do not cause
    the whole interpreter to exit as they normally do.
    Also enables tracing on the process, which protects against segmentation
    faults, and installs a very efficient error handling mechanism.

    This function is a simple wrapper, if you want to inject debug code,
    you can use the ``safe_apply`` function.

    Example
    -------
    >>> def f(x):
    ...     a = x.decode('utf-8')  # this could cause a crash
    ...     return a.lower()
    >>> ff = protect(f)
    >>> ff('FOO')
    'foo'
    """
    from .util import debug, debug_setup
    from .metrics import time
    debug_setup()

    def g(*args2,
