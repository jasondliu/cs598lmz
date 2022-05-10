import io
# Test io.RawIOBase

from test.support import run_unittest, import_module, check_warnings, \
    check_py3k_warnings

import unittest
from io import BytesIO, BufferedReader, BufferedWriter, BufferedRWPair, \
    BufferedRandom, TextIOWrapper
from io import DEFAULT_BUFFER_SIZE, SEEK_SET, SEEK_CUR, SEEK_END
import os
import sys
import tempfile
import warnings
import weakref

# Base class for testing io.IOBase implementation.

class BaseTestIO(unittest.TestCase):

    def setUp(self):
        self.f = self.StringIO("")

    def tearDown(self):
        self.f.close()
        self.f = None

    def test_closed_attr(self):
        self.assertFalse(self.f.closed)
        self.f.close()
        self.assertTrue(self.f.closed)

    def test_close(self):
        self.f.close()
        self.assertRa
