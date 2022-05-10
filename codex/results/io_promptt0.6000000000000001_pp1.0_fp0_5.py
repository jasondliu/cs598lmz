import io
# Test io.RawIOBase

import unittest
from unittest import mock
from test import support
from test.support.script_helper import assert_python_ok

try:
    import threading
except ImportError:
    threading = None

# Base class for testing RawIOBase

class BaseTestRawIO(object):
    def setUp(self):
        self.rawio = self.RawIO()

    def test_read(self):
        self.assertRaises(NotImplementedError, self.rawio.read)
        self.assertRaises(NotImplementedError, self.rawio.read, 0)

    def test_readinto(self):
        self.assertRaises(NotImplementedError, self.rawio.readinto, bytearray())
        self.assertRaises(NotImplementedError, self.rawio.readinto, bytearray(10))

    def test_readable(self):
        self.assertEqual(self.rawio.readable(), True)

    def test_readall(self):
        self.assertRa
