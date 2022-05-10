import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import bigmemtest

import io
import os
import sys
import tempfile
import time
import weakref

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Read method
        b = io.BytesIO(b"ABCDE")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(1), b"A")
        self.assertEqual(b.read(2), b"BC")
        self.assertEqual(b.read(3), b"DE")
        self.assertEqual(b.read(4), b"")
        self.assertEqual(b.read(1), b"")

    def test_readall(self):
        # Read all method
        b = io.BytesIO(b"ABCDE")
        self.assertEqual(b.readall(), b"ABCDE")
        self.assertEqual(b.readall(), b"")

   
