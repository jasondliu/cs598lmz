fn = lambda: None
# Test fn.__code__

import inspect
import sys

def _check(fn, code):
    """Assert that fn.__code__ is code."""
    assert fn.__code__ is code, '%r != %r' % (fn.__code__, code)

def _f():
    pass

def _g():
    pass

def _h(x):
    pass

def _get_code(fn):
    """Get the code object from the given function."""
    return fn.__code__

def _no_code(fn):
    """Raise an exception for lack of code object."""
    raise RuntimeError('function %r has no code object' % fn.__name__)

def _test():
    _check(_f, _f.__code__)
    _check(_g, _g.__code__)
    _check(_h, _h.__code__)
    _check(_get_code, _get_code.__code__)
    _check(_no_code, _no_code.__code__)

    _f.__
