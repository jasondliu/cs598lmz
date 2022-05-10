import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno
import _io

from test import support
from test.support import TESTFN, unlink, run_unittest

# Base class for testing a RawIO implementation.
# Subclasses must override read(), seek(), and write().
class BaseRawIO(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.mode = 'r+'
        self.name = '<unnamed>'
        self.closed = False
        self.readable = True
        self.writable = True
        self.seekable = True
        self.tell_calls = 0
        self.seek_calls = 0
        self.read_calls = 0
        self.write_calls = 0
        self.readinto_calls = 0
        self.readline_calls = 0
        self.truncate_calls = 0
        self.flush
