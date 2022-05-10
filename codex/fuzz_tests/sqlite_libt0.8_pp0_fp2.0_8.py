import ctypes
import ctypes.util
import threading
import sqlite3

from logging import getLogger
from fuse import FUSE, FuseOSError, Operations, LoggingMixIn
from threading import Thread
import traceback


logger = getLogger(__name__)

OSXFUSE_PATH = '/usr/local/lib/libosxfuse_i32.dylib'
LIBOSXFUSE_PATH = ctypes.util.find_library('osxfuse_i32')
LIBOSXFUSE = ctypes.cdll.LoadLibrary(OSXFUSE_PATH)


class MacOSXFuse(LoggingMixIn, Operations):
    """
    Fuse operations for Mac OS X
    """
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.db = sqlite3.connect(db_filename)
        self.root = None
        self.inodes = {}
        self.id_counter = 0
        self.path_counter = 0

        self.ctime = time.time()
        self.mtime = time.time()
        self.atime
