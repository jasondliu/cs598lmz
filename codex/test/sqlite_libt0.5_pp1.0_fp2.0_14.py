import ctypes
import ctypes.util
import threading
import sqlite3

from . import tables
from . import util
from . import dbutil

import logging
logger = logging.getLogger(__name__)

#
# The database class
#
class Database(object):
    def __init__(self, path, flags=0, **kwargs):
        self.path = path
        self.flags = flags
        self.kwargs = kwargs
        self.db = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def open(self):
        if self.db is not None:
            return
        self.db = sqlite3.connect(self.path, **self.kwargs)
        self.db.isolation_level = None
        self.db.row_factory = sqlite3.Row
        self.db.text_factory = str

    def close(self):
        if self.db is not None:
            self.db.close()

