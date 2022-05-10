import mmap
# Test mmap.mmap(0, 4096)

from mmap import *
from os import O_RDWR, O_CREAT
from os import strerror
from sys import stderr, exc_info
from tempfile import mkstemp
from unittest import TestCase, TestSuite, main

# Don't try to map more than the size of the temp file.
MAP_MAX_SIZE = 65536

class TestMmap(TestCase):
    def setUp(self):
        # Obtain a temporary file name.
        fd, self.filename = mkstemp(text=False)
        f = os.fdopen(fd, "w+b")
        # Create a file which we can mmap.
        try:
            f.write(b"\0" * MAP_MAX_SIZE)
        finally:
            f.close()

        self.size = MAP_MAX_SIZE

        # Open the file for reading.  We could mmap it directly,
        # but we open it first to get a real file object.
        f = open(self.filename, "rb")
        f
