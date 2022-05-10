import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = io.BytesIO()
        self.r = self.f.raw

    def tearDown(self):
        self.f.close()

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.r.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.r.readinto, b'')

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.r.write, b'')

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, self.r.fileno)

    def test_isatty(self):
        self.assertFalse(self.r.isatty())

    def test_
