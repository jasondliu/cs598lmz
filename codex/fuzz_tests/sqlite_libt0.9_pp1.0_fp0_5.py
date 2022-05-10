import ctypes
import ctypes.util
import threading
import sqlite3
import re
import zlib
import json
import base64
import ssl

from . import util
from . import error
from . import config
from . import keyvalue


class Store(object):
    _stores = {}
    _stores_lock = threading.RLock()

    @property
    def _store_path(self):
        p = '%s/%s' % (self.sources_dir, self.package.src)
        if self.package.nth_instance != 1:
            return p + '_%d' % self.package.nth_instance
        return p

    @property
    def _db_path(self):
        return self._store_path + '.db'

    @property
    def _db(self):
        if not hasattr(self, '_db_connection'):
            self._db_connection = sqlite3.connect(self._db_path)
            self._db_connection.row_factory = sqlite3.Row

        return self._db_connection

    def __init__(self, package, sources
