import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys

from . import lirc
from . import config

class LircdDatabase(object):
    """
    This class manages a database of Lircd data.
    """

    def __init__(self, filename, callback=None):
        """
        Initialise the LircdDatabase object.
        """
        self.filename = filename
        self.callback = callback
        self.db = None
        self.lock = threading.Lock()
        self.last_update = None
        self.last_update_time = None
        self.last_update_lock = threading.Lock()

    def connect(self):
        """
        Connect to the database.
        """
        self.db = sqlite3.connect(self.filename)

    def disconnect(self):
        """
        Disconnect from the database.
        """
        self.db.close()
        self.db = None

    def commit(self):
        """
        Commit any changes to the database.
        """
        self.db.commit()

