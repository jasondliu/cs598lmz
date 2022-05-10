import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
import time
import gc
import sys
import os
import platform

# TODO:
#   - use sqlite3.Row instead of fetchall()
#   - use sqlite3.Connection.iterdump()

from . import util
from . import constants
from . import sqlite3_helpers

from .util import (
    log_error,
    log_debug,
    log_info,
    log_warn,
    log_exception,
    log_critical,
    )

from .sqlite3_helpers import (
    get_sqlite_version,
    get_sqlite_version_number,
    )


def get_sqlite_lib_path():
    # Find the location of the sqlite3 lib
    # TODO: Use the sqlite3 module to find the lib path
    if sys.platform == 'darwin':
        # TODO: Check if this is correct
        return ctypes.util.find_library('sqlite3')
    elif sys.platform == 'win32':
        # TODO
