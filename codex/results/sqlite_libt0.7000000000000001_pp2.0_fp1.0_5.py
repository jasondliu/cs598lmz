import ctypes
import ctypes.util
import threading
import sqlite3
import subprocess
import os
import logging
import signal
import sys
import traceback
import time

import fcntl, termios, struct

from xlib import X, XK

logger = logging.getLogger(__name__)

class XlibError(Exception):
    pass

class XlibLock(threading.Lock):
    pass

def _get_libx11():
    """
    Returns reference to X11 library
    """
    libx11 = ctypes.cdll.LoadLibrary(ctypes.util.find_library('X11'))
    libx11.XInitThreads()
    return libx11

class Xlib(object):
    """
    Xlib wrapper class
    """
    _lock = XlibLock()

    _libx11 = _get_libx11()

    def __init__(self):
        """
        Initialize Xlib
        """

        self._display = None
        self._default_screen = None
        self._default_root = None
        self._check_events_callback =
