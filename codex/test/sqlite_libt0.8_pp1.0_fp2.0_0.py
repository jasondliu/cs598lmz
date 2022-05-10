import ctypes
import ctypes.util
import threading
import sqlite3
import os
from . import util


# ------------------------------------------------------------------------------
#   Logging
# ------------------------------------------------------------------------------

import logging

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------------------
#   The StorageManager
# ------------------------------------------------------------------------------

class StorageManager(object):
    """`StorageManager` is a base class for track storage backends.  It manages a
    FIFO cache of open tracks.  For each track, its file is either opened via
    `open_track`, or a cached file is returned.
    """

    _libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

    def __init__(self, max_cache=10):
        self._max_cache = max_cache
        self._tracks = {}
        self._dirty_tracks = set()
        self._dirty_tracks_mtx = threading.RLock()
        self._cache_mtx = threading.RLock()
        self._notification_cb = None
