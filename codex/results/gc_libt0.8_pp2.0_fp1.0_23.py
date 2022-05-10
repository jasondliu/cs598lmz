import gc, weakref
import sys
from numba.core.errors import NumbaPendingDeprecationWarning

try:
    import numba.core._dynfunc as _dynfunc_module
except ImportError:
    # Can happen if _dynfunc was not built
    _dynfunc_module = None


def _make_function(name, closure_contents, fndesc):
    """
    Compile a function.
    """
    closure = tuple(closure_contents)
    gv = cgutils.get_function(fndesc)
    if _dynfunc_module:
        # Explicitly leak the function object here to avoid refcounting
        # issues.  It is the caller's responsibility to manage the lifetime
        # of the function object.
        return _dynfunc_module._make_function(name, gv, closure, fndesc)
    else:
        return object()


class DictKeyIterator(object):
    """
    An iterator for a Python dict's key.

    We use this class to implement the dict key iterator protocol because
    Python
