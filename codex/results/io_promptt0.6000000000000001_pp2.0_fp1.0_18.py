import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import warnings
import abc
import errno
import functools
import select
import threading

from test import test_support
from test.test_support import TESTFN, import_module, run_unittest

support = import_module('test.support')

# Sets the default timeout for all tests to 2 seconds.
support.set_socket_timeout(2)

# test the abstract methods
class BaseIOTest(unittest.TestCase):

    def test_abc(self):
        self.assertTrue(issubclass(io.RawIOBase, io.IOBase))
        self.assertTrue(issubclass(io.BufferedIOBase, io.IOBase))
        self.assertTrue(issubclass(io.TextIOBase, io.IOBase))

        self.assertTrue(issubclass(io.FileIO, io.RawIOBase))
        self.assertTrue(issubclass(io.BytesIO, io.BufferedIOBase))
        self.assertTrue
