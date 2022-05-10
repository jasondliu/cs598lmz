import io
# Test io.RawIOBase

import io
import unittest
import warnings
import weakref

from test import test_support


# An inherited io object that records all arguments passed to its methods.

class RecordingIO(io.RawIOBase):

    def __init__(self, buf):
        self._records = []
        self.buf = buf

    def readinto(self, b):
        self._checkClosed()
        rv = super(RecordingIO, self).readinto(b)
        self._records.append(('readinto', b, rv))
        return rv

    def write(self, b):
        self._checkClosed()
        rv = super(RecordingIO, self).write(b)
        self._records.append(('write', b, rv))
        return rv

    def writelines(self, lines):
        self._checkClosed()
        rv = super(RecordingIO, self).writelines(lines)
        self._records.append(('writelines', lines, None))
        return rv

    def seek
