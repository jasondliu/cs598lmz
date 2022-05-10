import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
import subprocess
import time
import os
import sys
import re
import filecmp
import string
import contextlib
import errno
import shutil
import weakref
import traceback
import pprint
import hashlib
import tempfile

from . import parseutil
from . import util
from . import config
from . import shellutil
from . import systeminfo

logger = util.get_logger(__name__)

# Use the ctypes.util.find_library to find the library.
_libc_path = ctypes.util.find_library('c')
_libc = ctypes.CDLL(_libc_path, use_errno=True)

_libc.setenv.restype = ctypes.c_int
_libc.setenv.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int]
_libc.unsetenv.restype = ctypes.c_int
_libc.unsetenv
