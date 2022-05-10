import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import logging
logger = logging.getLogger(__name__)

# This is a hack to make sure that the library is loaded in the main thread
# before it is used in other threads.
# See https://github.com/pysam-developers/pysam/issues/9
_libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

# This is a hack to make sure that the library is loaded in the main thread
# before it is used in other threads.
# See https://github.com/pysam-developers/pysam/issues/9
_libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

# This is a hack to make sure that the library is loaded in the main thread
# before it is used in other threads.
# See https://github.com/pysam-developers/pysam/issues/9
