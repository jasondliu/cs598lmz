import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import traceback
import select
import sys
import fcntl
import struct
import socket
import errno
import logging

from . import structs, constants, errors, utils, logger
from .utils import Noop

if os.name == 'nt':
    _libc = ctypes.windll.msvcrt
else:
    _libc = ctypes.CDLL(ctypes.util.find_library('c'))

_set_thread_name = getattr(_libc, 'pthread_setname_np', Noop)
_set_thread_name.argtypes = [ctypes.c_void_p, ctypes.c_char_p]


class _StdStream(object):
    def __init__(self, name):
        self.name = name
        log_file = os.environ.get('KNEAD_' + name.upper() + '_LOG') or \
            os.environ.get('KNEAD_LOG')

        if log_file:
            self._logger =
