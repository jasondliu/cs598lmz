import mmap
import os
import sys

from . import _compat
from . import _util

_logger = logging.getLogger(__name__)


class _File(object):
    """
    A file-like object that supports mmap.

    This class is used to wrap a file-like object and provide mmap support.
    """

    def __init__(self, f, mode='r'):
        self._f = f
        self._mmap = None
        self._mode = mode

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __getattr__(self, name):
        return getattr(self._f, name)

    def __iter__(self):
        return iter(self._f)

    def close(self):
        self._f.close()

    def fileno(self):
        return self._f.fileno()

    def flush(self):
        self._f.flush()

    def isatty(
