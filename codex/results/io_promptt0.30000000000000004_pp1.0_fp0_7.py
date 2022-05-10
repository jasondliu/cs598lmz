import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings
from test import support
from test.support import import_module

# Skip tests if there is no os.dup().
import_module('fcntl')

try:
    import threading
except ImportError:
    threading = None

# Test RawIOBase using a memory buffer

class TestRawIO(io.RawIOBase):

    def __init__(self, test_obj):
        self._test = test_obj
        self._read_stack = []
        self._write_stack = []
        self._reads = 0
        self._writes = 0
        self._seekable = True
        self._closed = False
        self._extraneous_reads = 0
        self._extraneous_writes = 0

    def read(self, n=-1):
        self._test.assertFalse(self._closed)
        self._reads += 1
        if self._read_stack:
            rv = self._read_stack.pop(0)
