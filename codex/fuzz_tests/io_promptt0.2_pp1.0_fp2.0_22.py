import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import pickle
import tempfile
import warnings
from test import support
from test.support import TESTFN, unlink, run_unittest, import_module
from test.support.script_helper import assert_python_ok

# Base class for testing.  Doesn't define read or write.
class BaseTestRawIO(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.mode = 'x'
        self.name = '<%s>' % self.__class__.__name__
        self.closed = False
        self.exception = None
        self.readable = self.writable = self.seekable = False
        self.read_stack = []
        self.write_stack = []
        self.seek_stack = []
        self.tell_stack = []
        self.fileno_stack = []
        self.close_stack =
