import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/tmp/test.db", check_same_thread=False)

from . import _sqlite3


class _LazyImporter(object):
    """Lazily import a module.

    This creates a proxy for a module, which will import the module on its
    first use.
    """

    def __init__(self, module_name):
        self._module_name = module_name
        self._module = None

    def _load(self):
        if self._module is None:
            self._module = __import__(self._module_name)
        return self._module

    def __getattr__(self, attr):
        module = self._load()
        return getattr(module, attr)


datetime = _LazyImporter("datetime")
time = _LazyImporter("time")


# Threading support
_lock = threading.Lock()
_threading_local = threading.local()


