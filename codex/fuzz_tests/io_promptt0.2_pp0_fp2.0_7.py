import io
# Test io.RawIOBase

import io
import unittest
import os
import sys
import tempfile
import errno
import weakref
import contextlib
import gc
import _pyio as pyio

from test import support
from test.support import import_module

# Base class for testing io.RawIOBase
class BaseRawIO(io.RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def fileno(self):
        return 42

    def isatty(self):
        return False

    def close(self):
        pass

    def seek(self, offset, whence=0):
        return 0

    def tell(self):
        return 0

    def truncate(self, pos=None):
        return 0

    def readinto(self, b):
        return 0

    def read(self, n=-1):
        return b""

    def write(self, b):
        return 0

    def detach(self):
        return None

    def readall
