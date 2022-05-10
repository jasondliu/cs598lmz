import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno

from test import support
from test.support import TESTFN, unlink

# A mixin for testing RawIOBase
class BaseTestRawIO(object):
    # Subclasses must define the following attributes:
    # - filename: The filename to use for testing (defaults to TESTFN)
    # - mode: The mode argument to the constructor (defaults to "rb")
    # - bs: The block size to use for readinto() (defaults to 1024)
    # - bufs: The number of blocks to read/write at a time (defaults to 5)
    # - read_mode: The mode to use for reading (defaults to "rb")
    # - write_mode: The mode to use for writing (defaults to "wb")
    # - seekable: Whether the stream is seekable (defaults to True)
    # - seek_wrap: Whether the stream supports seeking past the end (defaults
    #              to True)
    # - read_data: The
