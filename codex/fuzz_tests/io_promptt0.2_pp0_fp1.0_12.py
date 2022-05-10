import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import weakref
import gc
import contextlib
import pickle
import struct
import shutil
import stat
import mmap

from test import support
from test.support import TESTFN, unlink, run_unittest, import_module
from test.support.script_helper import assert_python_ok

# Test io.RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_override_abstract_methods(self):
        # Issue #11459: check that RawIOBase methods raise a TypeError
        # when not overridden.
        with self.assertRaises(TypeError):
            io.RawIOBase().read(0)
        with self.assertRaises(TypeError):
            io.RawIOBase().readall()
        with self.assertRaises(TypeError):
            io.RawIOBase().readinto(bytearray())
        with self.assertRaises(TypeError):
            io.RawIO
