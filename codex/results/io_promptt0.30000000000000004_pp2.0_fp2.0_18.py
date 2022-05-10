import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import pickle
import weakref

from test import support
from test.support import TESTFN, run_unittest, import_module

# Base class for testing io.RawIOBase
class RawIOTest:
    # Subclass must override
    def new_instance(self):
        raise NotImplementedError

    def test_read(self):
        self.assertRaises(TypeError, self.f.read)
        self.assertRaises(TypeError, self.f.read, 'x')
        self.assertEqual(self.f.read(0), b'')
        self.assertEqual(self.f.read(-1), b'')
        self.assertEqual(self.f.read(10), b'')

    def test_readinto(self):
        b = bytearray(10)
        self.assertRaises(TypeError, self.f.readinto)
        self.assertRaises(TypeError, self.f.
