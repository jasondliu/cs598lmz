import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') is threadsafe # pylint: disable=c0111,w0141
import _sqlite3
try:
    import cPickle as pickle
except ImportError:
    import pickle

from . import (
    memory,
    util,
)

__all__ = ['connect']
_libc_path = ctypes.util.find_library('c')
_libc = ctypes.CDLL(_libc_path) if _libc_path is not None else None
_original_connection_init = sqlite3.Connection.__init__
_original_connection_commit = sqlite3.Connection.commit
_original_connection_commit_hook = sqlite3.Connection.set_commit_hook
_patch_is_applied = False


def _patch_sqlite3():
    """Ensure that sqlite3 is threadsafe."""
    assert not _patch_is_applied, 'Only call sqlite3.patch() once'
    if _libc is not None and (not sqlite3.threadsafety or
                              not sqlite
