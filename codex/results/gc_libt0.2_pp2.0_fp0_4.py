import gc, weakref

from . import _gdbm
from .exceptions import error

__all__ = ["open", "open_as_dict", "open_as_array"]

class _Database(object):
    def __init__(self, filename, mode, flags):
        self._dbm = _gdbm.open(filename, mode, flags)
        self._closed = False
        self._weakref = weakref.ref(self, self._close)

    def _close(self, _):
        self.close()

    def __del__(self):
        if not self._closed:
            self.close()

    def close(self):
        if self._closed:
            raise error("Database is already closed")
        self._dbm.close()
        self._closed = True
        self._weakref = None

    def __len__(self):
        return self._dbm.size()

    def __getitem__(self, key):
        return self._dbm.get(key)

    def __setitem__(self, key, value):
        self._
