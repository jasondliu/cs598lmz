import ctypes
import ctypes.util
import threading
import sqlite3 as sql
import time
import random
import math
import pprint
import os
import json

from collections import defaultdict

from .ffi import lib, ffi
from .errors import *

_ffi_lib = ffi.dlopen(None)

# For some reason cffi doesn't provide this one.
_ffi_lib.memset(ffi.NULL, 0, 0)

class _ThreadSafeConnection(sql.Connection):
    def __init__(self, *args, **kwargs):
        super(_ThreadSafeConnection, self).__init__(*args, **kwargs)

        self.lock = threading.Lock()

    def cursor(self):
        return _ThreadSafeCursor(self)


class _ThreadSafeCursor(sql.Cursor):
    def __init__(self, *args, **kwargs):
        super(_ThreadSafeCursor, self).__init__(*args, **kwargs)

        self.lock = self.connection.lock

