import mmap
# Test mmap.mmap.__init__, a Python implementation doesn't
# exist without the C implementation.

import os
import tempfile
import unittest
from test import support
from io import BytesIO

class MapTests(unittest.TestCase):
    _filename = os.path.join(tempfile.gettempdir(), 'mmap_file')
    _length = 1024

    def setUp(self):
        f = open(self._filename, 'wb+')
        try:
            f.write(b'\0' * self._length)
        finally:
            f.close()

    def tearDown(self):
        os.unlink(self._filename)

    def _open(self):
        f = open(self._filename, 'rb+')
        return f, mmap.mmap(f.fileno(), 0)

    def test_init_with_size(self):
        f = open(self._filename, 'wb+')
        try:
            f.write(b'\0' * self._length)
            f.close()
            f =
