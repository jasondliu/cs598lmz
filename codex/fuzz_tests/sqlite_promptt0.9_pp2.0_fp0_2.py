import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:?cache=shared")

import pythoncom
import win32event
import win32api
import winerror

from . import features
from . import graphyte
from . import winserial

from .winserial import *
from .features import *
from .graphyte import *


class Errors(Exception):
    pass


class MultiDevices(object):
    """Refs:
        https://github.com/adafruit/Adafruit_Python_GPIO/blob/master/Adafruit_GPIO/I2C.py
    """

    def __init__(self, dev_addresses=[]):
        self._lock = threading.Lock()
        self.dev_addresses = [0x27 if i == 0 else i for i in dev_addresses]
        # self._cmd_seq = list(range(0x80, 0x90, 2)) + list(range(0x90, 0xA0))
        self._cmd_seq = tuple(range(0x80, 0x90, 2))
        self._cmd
