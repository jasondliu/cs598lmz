import gc, weakref
import threading

from . import _lazy_import

_lazy_import.lazy_imports()

# -----------------------------------------------------------------------------
# --- Utility functions
# -----------------------------------------------------------------------------

def _get_function_name(func):
    """
    Returns the name of a function, including the module name.
    """
    return func.__module__ + "." + func.__name__

def _get_function_arguments(func):
    """
    Returns the arguments of a function.
    """
    argspec = inspect.getargspec(func)
    return argspec.args[1:]

# -----------------------------------------------------------------------------
# --- Base class for all objects
# -----------------------------------------------------------------------------

class _Object(object):
    """
    Base class for all objects.
    """

    def __init__(self):
        self._lock = threading.Lock()

    def _lock_object(self):
        self._lock.acquire()

    def _unlock_object(self):
        self._lock.release()

# -----------------------------------------------------------------------------
# --- Base class for all objects with a name
