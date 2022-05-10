import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import bigaddrspacetest

import io
from io import RawIOBase, BlockingIOError
import os, sys, select
from _thread import start_new_thread

TESTFN = support.TESTFN

# Base class for testing RawIOBase
class BaseRawIOTest:

    def setUp(self):
        self.f = self.RawIO()
        support.unlink(TESTFN)

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(TESTFN)

    def test_basic(self):
        self.assertEqual(self.f.readable(), True)
        self.assertEqual(self.f.writable(), True)
        self.assertEqual(self.f.seekable(), True)
        self.assertEqual(self.f.isatty(), False)
        self.assertEqual(self.f.fileno(), None)
        self.assertRaises(UnsupportedOperation, self
