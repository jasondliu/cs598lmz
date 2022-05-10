import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection is well wrapped
from pysqlite2 import dbapi2 as sqlite
import time
from pyliblzma import *
from pyliblzma import _pyliblzma as _lzma
from pyliblzma import compat
from pyliblzma import check

compat.register()

# ----------------------------------------------------------------------

class TestCase(unittest.TestCase):
    def setUp(self):
        self.numOpens = 0
        self.numCloses = 0
        self.lastOpen = None
        self.lastClose = None

    def tearDown(self):
        pass

    def openClose(self, filename, flags, mode):
        self.numOpens += 1
        self.lastOpen = time.time()
        fd = os.open(filename, flags, mode)
        return fd

    def close(self, fd):
        self.numCloses += 1
        self.lastClose = time.time()
        os.close(fd)

    def test_compress(self):
        self.assertEqual(l
