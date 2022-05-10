import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import logging
import time
import json
import re

from . import config
from . import utils
from . import consts
from . import db

logger = logging.getLogger(__name__)

def _get_libc_path():
    return ctypes.util.find_library("c")

def _get_libc():
    libc_path = _get_libc_path()
    if not libc_path:
        raise OSError("Can't find libc")
    return ctypes.CDLL(libc_path, use_errno=True)

def _get_libc_errno():
    libc = _get_libc()
    return ctypes.get_errno()

def _get_libc_errno_str():
    return os.strerror(_get_libc_errno())

def _get_libc_time():
    libc = _get_libc()
    return libc.time

def _get_libc_time_mon
