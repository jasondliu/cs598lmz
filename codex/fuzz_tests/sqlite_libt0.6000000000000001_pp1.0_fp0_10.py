import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import time
from . import constants
from . import exceptions
from . import _lib

__all__ = (
    'Sqlite3',
)

logger = logging.getLogger(__name__)


class Sqlite3(_lib.Base):
    _lock = threading.Lock()

    def __init__(self, path, **kwargs):
        super().__init__(**kwargs)
        self._path = path

        self._open = False
        self._handle = None

        self._open()

    def _open(self):
        with Sqlite3._lock:
            if self._open:
                return

            self._handle = _lib.sqlite3_open(self._path.encode('utf-8'), 0)

            if self._handle == 0:
                raise exceptions.Sqlite3Error()

            self._open = True

    def _close(self):
        with Sqlite3._lock:
            if not self._open:
                return

            if self._handle:
                _lib.sql
