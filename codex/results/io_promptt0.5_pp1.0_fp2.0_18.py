import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import stat
import tempfile
import platform
import errno
import struct

from test import support

# Base class for testing Raw I/O
class BaseRawIO(_io.RawIOBase):

    # Constructor.  Can raise an IOError.
    def __init__(self, *args, **kwargs):
        self._writable = kwargs.pop('writable', False)
        self._readable = kwargs.pop('readable', False)
        _io.RawIOBase.__init__(self, *args, **kwargs)

    # Optional; returns a readable and writable object
    def dup(self):
        raise NotImplementedError

    # Read up to n bytes, returned as bytes.
    def read(self, n = -1):
        raise NotImplementedError

    # Write the given buffer to the IO stream.
    def write(self, b):
        raise NotImplementedError

    # Move to a new position in the file.
