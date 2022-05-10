import io
# Test io.RawIOBase.readinto
import socket
import threading
import unittest
import weakref

import test.support
from test.support import TESTFN, run_unittest, reap_threads

# Self-test of io.RawIOBase methods

class RawIOTest(unittest.TestCase):
    def setUp(self):
        self.f = io.BytesIO(b"abc\ndef\nxyzzy\nfoo\x00bar\nanother line")

    def test_read(self):
        self.assertEqual(self.f.read(4), b"abc\n")
        self.assertEqual(self.f.read(4), b"def\n")
        self.assertEqual(self.f.read(4), b"xyzz")
        self.assertEqual(self.f.read(100), b"y\nfoo\x00bar\nanother line")
        self.assertEqual(self.f.read(1), b"")

    def test_readinto(self):
        b = bytearray
