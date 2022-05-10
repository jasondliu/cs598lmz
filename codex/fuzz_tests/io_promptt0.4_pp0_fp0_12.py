import io
# Test io.RawIOBase.readinto()

import io
import os
import sys
import tempfile
import unittest
from test import support

class TestRawIO(io.RawIOBase):
    def __init__(self, source_bytes):
        self._source_bytes = source_bytes
        self._offset = 0

    def readinto(self, b):
        if self._offset >= len(self._source_bytes):
            return None
        n = len(b)
        if n > len(self._source_bytes) - self._offset:
            n = len(self._source_bytes) - self._offset
        b[:n] = self._source_bytes[self._offset:self._offset+n]
        self._offset += n
        return n

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self._offset = offset
        elif whence == 1:
            self._offset += offset
        elif whence == 2:
            self._
