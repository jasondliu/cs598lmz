import io
# Test io.RawIOBase as base class for RawIO classes

import binascii
import _io
import os
import sys
import unittest
import weakref
from test import support
from test.support import import_helper

# As of Python 3.6, the io module has a RawIOBase class.
RawIOBase = import_helper.import_module('io').RawIOBase

#
#   Utility functions/classes
#

def make_bad_fd():
    # Create an invalid file descriptor by opening and closing a file and
    # returning its fd.
    with open(support.TESTFN, 'wb') as f:
        return f.fileno()

class MockRawIO(RawIOBase):
    """A RawIO implementation that doesn't do much.
    """
    def __init__(self):
        self._read_stack = []
        self._write_stack = []
        self.name = '<MockRawIO>'
        self.closed = False
        self.readable = self.writable = True
        self.seekable = True

    def readable
