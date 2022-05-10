import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect is safe
import sqlite3.connect
# Test sqlite3.DataError is safe
import sqlite3.DataError
import itertools
from collections import OrderedDict
import os

# Data.Text
from . import text as clib_text

# Data.Maybe
from . import maybe as clib_maybe

# Utils
from . import primitives as clib_primitives
from . import formatting as clib_formatting
from . import directories as clib_directories
from . import enums as clib_enums

_BLOB_DEFAULT_EXTENSION = '.blob'


# UNSAFE
def _blob_get(file_path, encoding='utf-8', mode='rb'):
    with open(file_path, mode=mode) as file:
        return file.read()


# UNSAFE
def _blob_set(text, file_path, encoding='utf-8', mode='wb'):
    with open(file_path, mode=mode) as file:
        file.write(text)


# UN
