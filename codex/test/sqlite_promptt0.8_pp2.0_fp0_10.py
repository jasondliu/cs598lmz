import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/dev/shm/test.db", check_same_thread=False)
from datetime import datetime
from time import time, sleep

from logging import getLogger
logger = getLogger("test")


class SharedLibrary(object):
    """
    This class is a generic wrapper for shared libraries.
    """

    def __init__(self, name, fallback=None):
        """
        Try to locate the shared library using the system path and other name if it fails.

        :param name: The name of the library to load.
        :param fallback: The name of the library to load if initial load fails.
        """
        self.name = name
        try:
            self.lib = ctypes.cdll.LoadLibrary(name)
        except OSError:
            self.lib = ctypes.cdll.LoadLibrary(fallback)
        self.lib.__getattr__ = self.get_symbol

