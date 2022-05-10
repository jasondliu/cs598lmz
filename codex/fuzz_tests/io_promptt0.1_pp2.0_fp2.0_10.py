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
from test.support import import_helper

# Base class for testing a RawIO implementation.
# Subclasses must override read(), seek(), and write().
class BaseRawIO(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.mode = kwargs.get('mode', 'rb')
        self.name = kwargs.get('name')
        self.closed = False
        self.readable = 'r' in self.mode
        self.writable = 'w' in self.mode
        self.seekable = True
        self.tell_calls = 0
        self.seek_calls = 0
        self.read_calls = 0
        self.write_calls = 0
        self.readinto_calls = 0
        self.readall_calls = 0
        self
