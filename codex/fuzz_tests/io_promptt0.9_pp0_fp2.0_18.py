import io
# Test io.RawIOBase

import unittest
import array

from test.support import TESTFN, run_unittest, import_helper, unlink, \
    cpython_only, bigmemtest
from test.script_helper import assert_python_ok
from test.io_tests import BaseTestIO, BigMemTest

try:
    import _io
except ImportError:
    pass


class DummyRawIOBase(io.RawIOBase):
    """
    Example for io.RawIOBase subclass.
    """
    @cpython_only
    def __init__(self):
        io.RawIOBase.__init__(self)
        self.readable = False
        self.writable = True
        self.seekable = False
        self.readinto_called = False
        self.write_return = None

    def writable(self):
        return self._writable

    def seekable(self):
        return self._seekable

    def write(self, b):
        return self.write_return

    def readinto(self, b):
        self.
